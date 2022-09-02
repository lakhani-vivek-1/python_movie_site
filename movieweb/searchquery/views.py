from django.shortcuts import render
import requests
def searchquery(name):
    url = "https://imdb8.p.rapidapi.com/auto-complete"
    querystring = {"q":f"{name}"}
    headers = {
        "X-RapidAPI-Key": "fb2e30bcddmsh7702a197c90b6f8p166413jsnc9460b03f96c",
        "X-RapidAPI-Host": "imdb8.p.rapidapi.com"
    }
    response = requests.request("GET", url, headers=headers, params=querystring)
    data = response.json()
    imgurl = []
    title = []
    imdbrating = []
    released = []
    imdbid = []
    dict =  {}
    for i in range(len(data['d'])):
        if(data['d'][i].get('i')):
            imgurl.append(data['d'][i]['i']['imageUrl'])
    for i in range(len(data['d'])):
        if(data['d'][i].get('l')):
            title.append(data['d'][i]['l'])
    for i in range(len(data['d'])):
        if(data['d'][i].get('y')):
            released.append(data['d'][i]['y'])
    for i in range(len(data['d'])):
        if(data['d'][i].get('id')):
            imdbid.append(data['d'][i]['id'])
    for i in range(len(data['d'])):
        if(data['d'][i].get('rank')):
            imdbrating.append(data['d'][i]['rank'])
    imgurl = zip(imgurl,title)
        
    dict.update({'imgurl':imgurl})
    dict.update({'released':released})
    dict.update({'imdbrating':imdbrating})
    dict.update({'imdbid':imdbid})
    
    return dict 


def showquery(request):
    name = request.POST.get('searchvalue')
    if(name == ""):
        name = "avengers"
    data = searchquery(name)
    return render(request,'query.html',data)