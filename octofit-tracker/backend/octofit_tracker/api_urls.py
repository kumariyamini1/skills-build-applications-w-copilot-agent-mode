from django.urls import path
from django.http import JsonResponse

def users(request):
    return JsonResponse({'message': 'users endpoint'})

def teams(request):
    return JsonResponse({'message': 'teams endpoint'})

def activities(request):
    return JsonResponse({'message': 'activities endpoint'})

def leaderboard(request):
    return JsonResponse({'message': 'leaderboard endpoint'})

def workouts(request):
    return JsonResponse({'message': 'workouts endpoint'})

urlpatterns = [
    path('users/', users),
    path('teams/', teams),
    path('activities/', activities),
    path('leaderboard/', leaderboard),
    path('workouts/', workouts),
]
