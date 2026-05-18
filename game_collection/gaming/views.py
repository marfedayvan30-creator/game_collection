from django.http import HttpResponse, JsonResponse
from .models import *
from django.shortcuts import get_object_or_404
import json

# Create your views here.
def functions(request):
    return HttpResponse("Francis is gay, this is not a test!")

#POST request to create a user
def create_user(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        user = Users.objects.create(
            first_name = data['first_name'],
            last_name = data['last_name'],
            username = data['username'],
            email = data['email'],
            password = data['password']
        )
        return JsonResponse({
            "id": user.id,
            "first_name": user.first_name,
            "last_name": user.last_name,
            "username": user.username,
            "email": user.email,
            "password": user.password
        })
    else:
        return HttpResponse('This is a POST only endpoint!', status=405)

#GET request to show all users    
def return_all_users(request):
    if request.method != 'GET':
        return HttpResponse('This is a GET only endpoint', status=405)

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

#GET request to show all the games played per user
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

#DELETE request to remove a user using id
def delete_user(request, user_id):
    if request.method == 'DELETE':
        user = get_object_or_404(Users, pk=user_id)

        user.delete()

        return HttpResponse(f'User {user_id} has been deleted!', status=200)
    else:
        return HttpResponse('This is an DELETE only endpoint!', status=405)

#PATCH request to update user data    
def update_user(request, user_id):
    if request.method == 'PATCH':
        user = get_object_or_404(Users, pk=user_id)
        data = json.loads(request.body)

        if 'first_name' in data:
            user.first_name = data['first_name']
        if 'last_name' in data:
            user.last_name = data['last_name']
        if 'username' in data:
            user.username = data['username']
        if 'email' in data:
            user.email = data['email']
        if 'password' in data:
            user.password = data['password']
        
        user.save()
        
        return JsonResponse({
            "id": user.id,
            "first_name": user.first_name,
            "last_name": user.last_name,
            "username": user.username,
            "email": user.email,
            "password": user.password
        })
    else:
        return HttpResponse('This is a PATCH only endpoint!', status=405)

 #GET request to display all games   
def return_all_games(request):
    if request.method == 'GET':
        games = Games.objects.all()
        games_serialized = []

        for game in games:
            games_serialized.append(
                {
                    'id': game.id,
                    'name': game.name,
                    'genre': game.genre.name,
                    'developer': game.developer.name,
                    'release date': game.release_date

                }
            )
        print(games_serialized)
        return JsonResponse(games_serialized, safe=False)
    else:
        return HttpResponse('This is a GET only endpoint!', status=405)
    
#POST request to add new games
def add_game(request):
    if request.method == 'POST':
        data = json.loads(request.body)

        genre = get_object_or_404(Genres, name=data['genre'])
        developer = get_object_or_404(Developers, name=data['developer'])

        game = Games.objects.create(
            name = data['name'],
            genre = genre,
            developer = developer,
            release_date = data['release_date']
        )

        return JsonResponse({
            'id': game.id,
            'name': game.name,
            'genre': game.genre.name,
            'developer': game.developer.name,
            'release_date': game.release_date
        })
    else:
        return HttpResponse('This is a POST only endpoint', status=405)

#DELETE request for deleting a game    
def delete_game(request, game_id):
    if request.method == 'DELETE':
        game = get_object_or_404(Games, pk=game_id)
        
        game.delete()
        
        return HttpResponse(f'Game id: {game_id} has been deleted', status=200)
    else:
        return HttpResponse('This is a DELETE endpoint only!', status=405)
    
def patch_game(request, game_id):
    if request.method == 'PATCH':
        game = get_object_or_404(Games, pk=game_id)
        data = json.loads(request.body)

        if 'name' in data:
            game.name = data['name']
        if 'genre' in data:
            genre = get_object_or_404(Genres, name=data['genre'])
            game.genre = genre
        if 'developer' in data:
            developer = get_object_or_404(Developers, name=data['developer'])
            game.developer = developer
        if 'release_date' in data:
            game.release_date = data['release_date']

        game.save()

        return JsonResponse({
            'id': game.id,
            'name': game.name,
            'genre': game.genre.name,
            'developer': game.developer.name,
            'release_date': game.release_date
        })
    else:
        return HttpResponse('This is a PATCH endpoint only!', status=405)





