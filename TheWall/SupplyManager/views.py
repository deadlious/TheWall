from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import TheWall, BuildHistory
import itertools
import subprocess


def index_page(request):
    # print(unquote(request.read().split(b'&')[1]))
    if not request.POST:
        TheWall.objects.all().delete()
        BuildHistory.objects.all().delete()
        return render(request, "index.html")
    else:
        for profile, profile_data in enumerate(request.POST.get('profile_data', '').split('\n'), start=1):
            for section, section_height in enumerate(map(int, profile_data.strip().split()), start=1):
                TheWall(profile=profile, section=section, initialHeight=section_height, currentHeight=section_height).save()
        return redirect('/sm/confirm/', request=request)


def confirmation_page(request):
    the_wall = TheWall.objects.all().order_by('profile', 'section')
    wall = [
        [section.initialHeight for section in sections]
        for profile, sections in itertools.groupby(the_wall, key=lambda x: x.profile)
    ]
    if not request.POST:
        maxlen = max(map(len, wall))
        for profile in wall:
            if (current_len := len(profile)) < maxlen:
                profile.extend(['']*(maxlen - current_len))

        return render(
            request,
            'confirm.html',
            context={
                "wall": enumerate(wall, start=1),
                "num_sections": range(1, maxlen+1),
            }
        )
    else:
        num_teams = request.POST.get('num_teams', len(wall))
        subprocess.Popen(['python', 'worker_spawner.py', f'--num-teams={num_teams}'])
        return HttpResponse(content="<html><body><p>Wall plan submitted to builders</p></body></html>")
