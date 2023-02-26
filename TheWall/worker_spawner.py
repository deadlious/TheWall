import os
import sys
import argparse
from multiprocessing import Pool
import sqlite3
import itertools
from time import sleep


FIELDS = ['profile', 'section', 'initialHeight', 'currentHeight', 'taskID']
DB = sqlite3.connect('db.sqlite3')
DB_CURSOR = DB.cursor()


def build_section(section):
    DB_CURSOR.execute(
        """
        UPDATE SupplyManager_thewall SET TASKID = ? WHERE PROFILE = ? AND SECTION = ?
        """,
        [os.getpid(), section['profile'], section['section']]
    )
    DB.commit()
    sleep(1)
    DB_CURSOR.execute(
        """
        INSERT INTO SupplyManager_BUILDHISTORY(PROFILE, SECTION, DAY, ICE, COINS) 
        VALUES(?,?,?,?,?)
        """,
        [section['profile'], section['section'], section['day'], 195, 1900*195]
    )
    DB_CURSOR.execute(
        """
        UPDATE SupplyManager_thewall SET TASKID = ?, CURRENTHEIGHT = ? WHERE PROFILE = ? AND SECTION = ?
        """,
        [0, section['currentHeight']+1, section['profile'], section['section']]
    )
    DB.commit()
    

def main(num_teams: int):
    with Pool(num_teams) as p:
        for day in itertools.count(start=1):
            the_wall = DB_CURSOR.execute(
                """
                SELECT PROFILE, SECTION, INITIALHEIGHT, CURRENTHEIGHT, TASKID 
                FROM SupplyManager_thewall
                WHERE CURRENTHEIGHT < 30
                  AND TASKID = 0
                ORDER BY PROFILE, SECTION
                LIMIT ?
                """,
                (num_teams,),
            ).fetchall()
            if not the_wall:
                break
            the_wall = [dict(zip(FIELDS, _)) for _ in the_wall]
            p_list = p.map(build_section, [{**_, 'day': day} for _ in the_wall])


if __name__ == '__main__':
    args_parser = argparse.ArgumentParser()
    args_parser.add_argument('--num-teams', type=int)
    args = args_parser.parse_args(sys.argv[1:])
    main(num_teams=args.num_teams)
