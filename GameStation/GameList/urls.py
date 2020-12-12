from django.urls import path
from GameList.controllers import game_controller, platform_controller, genre_controller, publisher_controller, developer_controller, official_web_controller, home_controller, registration_controller

urlpatterns = [
    path('', home_controller.index, name='home_index'),
	path('game', game_controller.index, name='game_index'),
    path('game/add', game_controller.add_game, name='add_game'),
    path('game/edit/<int:game_id>', game_controller.edit_game, name='edit_game'),
    path('game/delete/<int:game_id>', game_controller.delete_game, name='delete_game'),	
	path('platform', platform_controller.index, name='platform_index'),
    path('platform/add', platform_controller.add_platform, name='add_platform'),
    path('platform/edit/<int:platform_id>', platform_controller.edit_platform, name='edit_platform'),
    path('platform/delete/<int:platform_id>', platform_controller.delete_platform, name='delete_platform'),
    path('genre', genre_controller.index, name='genre_index'),
    path('genre/add', genre_controller.add_genre, name='add_genre'),
    path('genre/edit/<int:genre_id>', genre_controller.edit_genre, name='edit_genre'),
    path('genre/delete/<int:genre_id>', genre_controller.delete_genre, name='delete_genre'),			
    path('publisher', publisher_controller.index, name='publisher_index'),
    path('publisher/add', publisher_controller.add_publisher, name='add_publisher'),
    path('publisher/edit/<int:publisher_id>', publisher_controller.edit_publisher, name='edit_publisher'),
    path('publisher/delete/<int:publisher_id>', publisher_controller.delete_publisher, name='delete_publisher'),	
    path('developer', developer_controller.index, name='developer_index'),
    path('developer/add', developer_controller.add_developer, name='add_developer'),
    path('developer/edit/<int:developer_id>', developer_controller.edit_developer, name='edit_developer'),
    path('developer/delete/<int:developer_id>', developer_controller.delete_developer, name='delete_developer'),
    path('official_web', official_web_controller.index, name='official_web_index'),
    path('official_web/add', official_web_controller.add_official_web, name='add_official_web'),
    path('official_web/edit/<int:official_web_id>', official_web_controller.edit_official_web, name='edit_official_web'),
    path('official_web/delete/<int:official_web_id>', official_web_controller.delete_official_web, name='delete_official_web'),
    path('register', registration_controller.index, name='register'),		
]