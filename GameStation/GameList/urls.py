from django.urls import path
from GameList.controllers import game_controller, platform_controller, genre_controller, publisher_controller, developer_controller, official_web_controller, home_controller

urlpatterns = [
    path('', home_controller.index, name='home_index'),
	path('game', game_controller.index, name='game_index'),	
	path('platform', platform_controller.index, name='platform_index'),
    path('genre', genre_controller.index, name='genre_index'),	
    path('publisher', publisher_controller.index, name='publisher_index'),	
    path('developer', developer_controller.index, name='developer_index'),	
    path('official_web', official_web_controller.index, name='official_web_index'),		
]