from django.shortcuts import render

from django.http import HttpResponse
# Create your views here.
'''
classes that used in urls.py by getting request when a url is called.
Return the information that needs to be shown to client.
type of HTTTP request(GET, POST, PUT, DELETE)
The class below is an example for "My page"
'''
@api_view(['GET', 'PUT'])
def updatePlayerProfile(request):
    '''
    GET list of player information, PUT new information.
    '''
    if request.method == 'PUT': 
        playerNmae = request.POST.get('userName');
        desiredSkill = request.POST.get('title');
        seasonStartDate = request.POST.get('seasonStartDate') ;
        seasonEndDate = request.POST.get('seasonEndDate');
        playerAge = request.POST.get('playerAge');
        trainingExperience = request.POST.get('trainingExperience');
        chooseTrainingLevel = request.POST.get('chooseTrainingLevel');
        chooseTrainingDays = request.POST.get('chooseTrainingDays');
        Note.objects.create(
            '''
            Registered Positions:
            Registered Sports:
            ...
            '''
        )
    return HttpResponse({"status": 'xxxx'}) 

@api_view(['POST'])
def profileSignUp(request, pk):
    # create an account and saving user id and password
    # by pk(primary key).


@api_view(['GET'])
def profileSignIn(request, pk):
    # sign in account by input name and password.


