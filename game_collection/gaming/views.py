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

#PATCH request for updating a game    
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
    
#GET request for displaying all devs
def return_all_devs(request):
    if request.method == 'GET':
        devs = Developers.objects.all()
        devs_serialized = []

        for dev in devs:
            devs_serialized.append(
                {
                    'dev_id': dev.id,
                    'name': dev.name,
                    'date_active': dev.date_active,
                    'about': dev.about
                }
            )
        
        return JsonResponse(devs_serialized, safe=False)
    else:
        return HttpResponse('This is a GET only endpoint!', status=405)

##POST request for adding new dev
def add_dev(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        
        dev = Developers.objects.create(
            name = data['name'],
            date_active = data['date_active'],
            about = data['about']
        )

        return JsonResponse(
            {
                'name': dev.name,
                'date_active': dev.date_active,
                'about': dev.about
            }
        )
    else:
        return HttpResponse('This is a POST only endpoint!', status=405)
 
##DELETE request for deleting a dev
def delete_dev(request, dev_id):
    if request.method == 'DELETE':
        dev = get_object_or_404(Developers, pk = dev_id)

        dev.delete()
        return HttpResponse(f'Developer id: {dev_id} has been deleted.', status=200)
    else:
        return HttpResponse('This is a DELETE only endpoint!')
    
##PATCH request for updating a dev
def update_dev(request, dev_id):
    if request.method == 'PATCH':
        dev = get_object_or_404(Developers, pk=dev_id)
        data = json.loads(request.body)

        if 'name' in data:
            dev.name = data['name']
        if 'date_active' in data:
            dev.date_active = data['date_active']
        if 'about' in data:
            dev.about = data['about']

        return JsonResponse(
            {
                'id': dev.id,
                'name': dev.name,
                'date_active': dev.date_active,
                'about': dev.about
            }
        )
    else:
        return HttpResponse('This is a PATCH endpoint only!', status=405)

##GET request for displaying all genres
def return_all_genres(request):
    if request.method == 'GET':
        genres = Genres.objects.all()
        genres_serialized = []

        for genre in genres:
            genres_serialized.append(
                {
                    'name': genre.name
                }
            )
        return JsonResponse(genres_serialized, safe=False)
    else:
        return HttpResponse('This is a GET only endpoint', status=405)

##POST request for adding a genre
def add_genre(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        
        genre = Genres.objects.create(
            name = data['name']
        )
        return JsonResponse({
            'id': genre.id,
            'name': genre.name
        })
    else:
        return HttpResponse('This is a post only endpoint!', status=405)
    
##DELETE request for deleting a genre
def delete_genre(request, genre_id):
    if request.method == 'DELETE':
        genre = get_object_or_404(Genres, pk=genre_id)

        genre.delete()
        return HttpResponse(f'Genre id: {genre_id} has been deleted', status=200)
    else:
        return HttpResponse('This is a DELETE only endpoint!', status=405)

    
