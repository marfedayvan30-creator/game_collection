from django.urls import path
from django.http import HttpResponse
from .views import * 

urlpatterns = [
    path('test/', functions),

    #Users
    ##GET
    path('users', return_all_users),
    path('users/<int:user_id>/games_played', return_all_games_played),
    ##POST
    path('users/create', create_user),
    ##DELETE
    path('users/delete/<int:user_id>', delete_user),
    ##PATCH
    path('users/update/<int:user_id>', update_user),

    #Games
    ##GET
    path('games', return_all_games),
    ##POST
    path('games/add', add_game),
    ##DELETE
    path('games/delete/<int:game_id>', delete_game),
    ##PATCH
    path('games/update/<int:game_id>', patch_game),

    #Developers
    ##GET
   path('dev', return_all_devs),
    ##POST
    path('dev/add', add_dev),
    ##DELETE
    path('dev/delete/<int:dev_id>', delete_dev),
    ##PATCH
    path('dev/update/<int:dev_id>', update_dev),

]
