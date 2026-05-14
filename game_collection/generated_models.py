# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

class Users(models.Model):
    id = models.BigAutoField(primary_key=True)
    first_name = models.CharField(max_length=20, blank=True, null=True)
    last_name = models.CharField(max_length=20, blank=True, null=True)
    username = models.CharField(unique=True, max_length=35)
    email = models.CharField(unique=True, max_length=30)
    password = models.CharField(max_length=16)

    class Meta:
        managed = False
        db_table = 'users'


class Developers(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=20, blank=True, null=True)
    date_active = models.DateField(blank=True, null=True)
    about = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'developers'


class Genres(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(unique=True, max_length=20)

    class Meta:
        managed = False
        db_table = 'genres'


class Games(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    genre = models.ForeignKey('Genres', models.DO_NOTHING, blank=True, null=True)
    developer = models.ForeignKey(Developers, models.DO_NOTHING, blank=True, null=True)
    release_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'games'


class Badges(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    game = models.ForeignKey('Games', models.DO_NOTHING, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    rarity = models.CharField(max_length=6)

    class Meta:
        managed = False
        db_table = 'badges'


class GamesPlayed(models.Model):
    id = models.BigAutoField(primary_key=True)
    game = models.ForeignKey(Games, models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey('Users', models.DO_NOTHING, blank=True, null=True)
    hours_played = models.IntegerField()
    notes = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'games_played'

class UserBadges(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey('Users', models.DO_NOTHING, blank=True, null=True)
    badge = models.ForeignKey(Badges, models.DO_NOTHING, blank=True, null=True)
    unlocked_at = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_badges'


