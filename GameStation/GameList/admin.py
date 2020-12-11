from django.contrib import admin
from GameList.models import game, genre, developer, platform, publisher, official_web

admin.site.register(game.Game)
admin.site.register(genre.Genre)
admin.site.register(developer.Developer)
admin.site.register(platform.Platform)
admin.site.register(publisher.Publisher)
admin.site.register(official_web.Official_web)
