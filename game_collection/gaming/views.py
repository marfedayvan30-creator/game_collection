from django.http import HttpResponse, JsonResponse
from .models import *
from django.shortcuts import get_object_or_404

# Create your views here.
def functions(request):
    return HttpResponse("Francis is gay, this is not a test!")

def simple_post_function(request):
    if request.method == 'POST':
        decoded_data = request.body.decode('utf-8')
        print(decoded_data)
        return HttpResponse('Data was received')
    else:
        return HttpResponse('This is a POST only endpoint!', status=405)
    
def return_all_users(request):
    users = Users.objects.all()
    users_serialized = []

    for user in users:
        users_serialized.append(
            {
                "id": user.id,
                "first name": user.first_name,
                "last_name": user.last_name,
                "username": user.username,
                "email": user.email,
                "password": user.password
            }
        )
    print(users_serialized)
    return JsonResponse(users_serialized, safe=False)

def return_all_games_played(request, user_id):
    user= get_object_or_404(Users, pk=user_id)

    games_played = GamesPlayed.objects.filter(user=user)
    played_serialized = []
 

    for game in games_played:
        played_serialized.append(
            {
                "id": game.id,
                "Game id": game.game.id,
                "Game": game.game.name, 
                "Genre": game.game.genre.name,
                "User id": game.user.id,
                "Hours Played": game.hours_played,
                "Notes": game.notes 
            }
        )
        
    return JsonResponse({
            "user_id": user_id,
            "user_first_name": user.first_name,
            "user_last_name": user.last_name,
            "user_username": user.username,
            "games_played": played_serialized
                        })