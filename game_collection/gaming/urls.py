from django.urls import path
from django.http import HttpResponse
from .views import * 

urlpatterns = [
    path('test/', functions),
    path('test-post/', simple_post_function),

    #Users
    ##GET
    path('users', return_all_users),
    path('users/<int:user_id>/games_played', return_all_games_played),
]
