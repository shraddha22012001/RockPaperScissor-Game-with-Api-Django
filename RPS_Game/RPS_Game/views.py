from django.shortcuts import render
from django.http import HttpResponse
from django.core.serializers import serialize
import json
import random           

def home(request):
    return render(request,"home.html")

def game(request):
    return render(request,"game.html")

def index(request):
    userans=request.GET['userans']
    gamelist = ['rock', 'paper', 'scissor']
    computerans = random.choice(gamelist)
    if userans == computerans:
        winner = "No one"
    elif userans == "rock":
        if computerans == "scissor":
            winner = "You"
        else:
            winner = "Computer"
    elif userans == "paper":
        if computerans == "rock":
            winner = "you"
        else:
            winner = "Computer"
    elif userans == "scissor":
        if computerans == "paper":
            winner = "you"
        else:
            winner = "Computer"
    resultdict={'winner':winner,'userchoice':userans,'computerchoice':computerans}
    json_response=json.dumps(resultdict,indent=5)
    return HttpResponse(json_response,content_type='application/json')   

