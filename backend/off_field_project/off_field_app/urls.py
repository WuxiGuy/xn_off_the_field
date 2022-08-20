from django.urls import path
from .views import *
urlpatterns = [
    path('', homePage, name="Home"),
    path('team/', teamPage, name="Team"),
    path('training/', trainingPage, name="Challenge"),
    path('challenge/', challengePage, name="Challenge"),
    path('')

    path('create_note/', createNote, name="note")
]
