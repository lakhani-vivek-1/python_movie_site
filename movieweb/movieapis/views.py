from django.shortcuts import render
import requests
def callmovies():

        url = "https://ott-details.p.rapidapi.com/advancedsearch"

        querystring = {"start_year":"1970","end_year":"2022","min_imdb":"7","max_imdb":"10","genre":"action","language":"hindi","type":"movie","sort":"latest","page":"1"}

        headers = {
                "X-RapidAPI-Key": "fd6dc4209bmshc74187fe0f549aep17c527jsncb2175b0b2e7",
	"X-RapidAPI-Host": "ott-details.p.rapidapi.com"
        }

        response = requests.request("GET", url, headers=headers, params=querystring)
        data = response.json()
        imgurl = []
        title = []
        imdbrating = []
        released = []
        imdbid = []
        dict =  {}
        for i in range(len(data['results'])):
                if(str(data['results'][i]['imageurl'])[1:-1]==""):
                        continue
                else:
                        imgurl.append(str(data['results'][i]['imageurl'])[2:-2])
        for i in range(len(data['results'])):
                if(str(data['results'][i]['imageurl'])[1:-1]==""):
                        continue
                else:
                        title.append(data['results'][i]['title'])
        for i in range(len(data['results'])):
                if(str(data['results'][i]['imageurl'])[1:-1]==""):
                        continue
                else:
                        imdbrating.append(data['results'][i]['imdbrating'])
        for i in range(len(data['results'])):
                if(str(data['results'][i]['imageurl'])[1:-1]==""):
                        continue
                else:
                        released.append(data['results'][i]['released'])
        for i in range(len(data['results'])):
                if(str(data['results'][i]['imageurl'])[1:-1]==""):
                        continue
                else:
                        imdbid.append(data['results'][i]['imdbid'])
                
        imgurl = zip(title,imgurl)
        dict.update({'imgurl':imgurl})
        dict.update({'released':released})
        dict.update({'imdbrating':imdbrating})
        dict.update({'imdbid':imdbid})

        return dict
def homepage(request):
    data = callmovies()
    return render(request,'homepage.html',data)