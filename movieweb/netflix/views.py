from django.shortcuts import render
import requests
def callnetflix():
    url = "https://streaming-availability.p.rapidapi.com/search/basic"

    querystring = {"country":"us","service":"netflix","type":"movie","genre":"18","page":"1","output_language":"en","language":"en"}
    querystring2 = {"country":"us","service":"netflix","type":"movie","genre":"18","page":"2","output_language":"en","language":"en"}
    querystring3 = {"country":"us","service":"netflix","type":"movie","genre":"18","page":"3","output_language":"en","language":"en"}

    headers = {
        'X-RapidAPI-Key': 'fd6dc4209bmshc74187fe0f549aep17c527jsncb2175b0b2e7',
        'X-RapidAPI-Host': 'streaming-availability.p.rapidapi.com'
    }

    response = requests.request("GET", url, headers=headers, params=querystring)
    response2 = requests.request("GET", url, headers=headers, params=querystring2)
    response3 = requests.request("GET", url, headers=headers, params=querystring3)
    data = response.json()
    data2 = response2.json()
    data3 = response3.json()
    imgurl = []
    title = []
    imdbrating = []
    released = []
    imdbid = []
    dict =  {}
    for i in range(len(data['results'])):
        imdbrating.append(data['results'][i]['imdbRating'])
    for i in range(len(data['results'])):
        title.append(data['results'][i]['title'])
    for i in range(len(data['results'])):
        imgurl.append(data['results'][i]['posterURLs']['original'])
    for i in range(len(data['results'])):
        released.append(data['results'][i]['year'])
        
    for i in range(len(data2['results'])):
        imdbrating.append(data2['results'][i]['imdbRating'])
    for i in range(len(data2['results'])):
        title.append(data2['results'][i]['title'])
    for i in range(len(data2['results'])):
        imgurl.append(data2['results'][i]['posterURLs']['original'])
    for i in range(len(data2['results'])):
            released.append(data2['results'][i]['year'])
            
            
    for i in range(len(data3['results'])):
        imdbrating.append(data3['results'][i]['imdbRating'])
    for i in range(len(data3['results'])):
        title.append(data3['results'][i]['title'])
    for i in range(len(data3['results'])):
        imgurl.append(data3['results'][i]['posterURLs']['original'])
    for i in range(len(data3['results'])):
        released.append(data3['results'][i]['year'])
        
        



    imgurl = zip(imgurl,title)
    # dict.update({'title':title})
    dict.update({'imgurl':imgurl})
    dict.update({'released':released})
    dict.update({'imdbrating':imdbrating})
    dict.update({'imdbid':imdbid})
    return dict


def netflix(request):
    data = callnetflix()
    return render(request,'netflix.html',data)
