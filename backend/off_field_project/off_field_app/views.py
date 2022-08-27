from django.shortcuts import render

from django.http import HttpResponse
# Create your views here.
'''
classes that used in urls.py by getting request when a url is called.
Return the information that needs to be shown to client.
type of HTTTP request(GET, POST, PUT, DELETE, etc.)
The class below is an example for "My page"

Get Put Post Delete
'''

@api_view() # put type of request(GET, POST, PUT, DELETE, etc.) between parenthese
def homeStart(request):
    # select "I am a coach" or "I am an athelete"
    # jump to mypage/signin after selection

@api_view() # put type of request(GET, POST, PUT, DELETE, etc.) between parenthese
def reviseTeam(request):
    # delete or add team

@api_view() # put type of request(GET, POST, PUT, DELETE, etc.) between parenthese
def challengeInfo(request):
    # display challenges

@api_view(['GET', 'PUT'])
def updatePlayerProfile(request):
    # display user's information which can also be revised
    return HttpResponse() 

@api_view(['POST'])
def profileSignUp(request, pk):
    # create an account and saving user id and password
    # by pk(primary key).

@api_view(['GET'])
def profileSignIn(request, pk):
    # sign in account by input name and password.


