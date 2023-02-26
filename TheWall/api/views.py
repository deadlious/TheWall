from rest_framework.response import Response
from rest_framework.decorators import api_view
from SupplyManager.models import BuildHistory


@api_view(['GET'])
def profile_ice_used_for_day(request, profile: int, day: int):
    ice_used = sum(_.ice for _ in BuildHistory.objects.filter(profile=profile, day=day).all())
    return Response({"day": str(day), "ice_amount": f"{ice_used:,}"})


@api_view(['GET'])
def profile_cost_for_day(request, profile: int, day: int):
    coins_used = sum(_.coins for _ in BuildHistory.objects.filter(profile=profile, day=day).all())
    return Response({"day": str(day), "cost": f"{coins_used:,}"})


@api_view(['GET'])
def day_cost_overview(request, day: int):
    coins_used = sum(_.coins for _ in BuildHistory.objects.filter(day=day).all())
    return Response({"day": str(day), "cost": f"{coins_used:,}"})


@api_view(['GET'])
def cost_total(request):
    coins_used = sum(_.coins for _ in BuildHistory.objects.all())
    return Response({"day": None, "cost": f"{coins_used:,}"})