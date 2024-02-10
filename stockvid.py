import random
from pexelsapi.pexels import Pexels
api_key = 'Z8dYwKNsRLJxzUQgbiYA0d03swA54ljD87BmwC1wPMjKKK7hkQwGqxF4'
pexel = Pexels(api_key)
#topic-----------------
# videotopic = 'fefefefefe'
ans = [False, 'Neither', 0]
length = random.randrange(15,30)
#topic-----------------

"""
generateVideo returns a list:
    list = [True, link, duration]; if video exists
    list = [False, link, 0]; if photo is being returned
    list = [False, Neither, 0]; if neither photo, nor video exists

"""

def generateVideo(videotopic, list=ans, length=15):            

    ourvideo = pexel.search_videos(query=videotopic, orientation='portrait', size='small', locale='en-US', page=1, per_page=10)
    corrvideo = False
    foundvideo = False
    if (ourvideo['total_results']>0):       #video exists
        
        for i in range(len(ourvideo['videos'])):
            if (ourvideo['videos'][i]["duration"]>=length and ourvideo['videos'][i]["duration"]<35):
                corrvideo = True
                foundvideo = True
                list[1] = (ourvideo['videos'][i]["video_files"][0]["link"])
                list[2] = (ourvideo['videos'][i]["duration"])
                
                break

        if (corrvideo==False):
            list[1] = (ourvideo['videos'][0]["video_files"][0]["link"])
            list[2] = (ourvideo['videos'][0]["duration"])
            foundvideo = True

    else:
        
        ourphoto = pexel.search_photos(query=videotopic, orientation='portrait', size='large', locale='en-US', page=1, per_page=10)
        if (len(ourphoto['photos'])>0):
            list[1] = (ourphoto['photos'][0]['src']['original'])
        else:
            list[1] = ("Neither")
            
    list[0] = foundvideo

    return list
    

        

    
    
    