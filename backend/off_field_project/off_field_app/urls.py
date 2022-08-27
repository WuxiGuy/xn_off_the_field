from django.urls import path
from .views import *

urlpatterns = [
    '''
    paths of the website. each path call a method in view which 
    sends the information that need to be displayed.
    put method after "view.".
    '''

    path('home/', view.homeStart, name="homePage"),
    path('team/', view.reviseTeam, name="teamPage"),
    path('training/', view.getTrainingPlan, name="training"),
    path('challenge/', view.challengeInfo, name="Challenge"),
    path('mypage/', view.updatePlayerProfile, name="myPage"),
    path('mypage/signup', view.profileSignUp, name="myPageSignUp"),
    path('mypage/signin', view.profileSignIn, name="myPageSignIn")
]
