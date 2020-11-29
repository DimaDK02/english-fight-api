from django.urls import path

from game.views.game_view import GameView
from game.views.user_view import UsersView

urlpatterns = [
    path('user', UsersView.as_view()),
    path('game', GameView.as_view()),
]
