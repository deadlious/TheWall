from django.urls import path
from . import views

urlpatterns = [
    path('profiles/<int:profile>/days/<int:day>', views.profile_ice_used_for_day),
    path('profiles/<int:profile>/overview/<int:day>', views.profile_cost_for_day),
    path('profiles/overview/<int:day>', views.day_cost_overview),
    path('profiles/overview/', views.cost_total),
]
