import text_to_speech
import video
import gptTotext
import stockvid
import translatetext
import main
import os

def createVideo(title, val):
    print(val)
    response = gptTotext.generate_script(title)[1]
    # response = "Rainforests are home to over half of the world's plant and animal species, making them incredibly diverse and important ecosystems. Protecting rainforests is crucial for the preservation of our planet's biodiversity."
    vid_link = stockvid.generateVideo(title)[1]
    print(vid_link)
    video.save_video(vid_link)
    
    if(val):           #it is Hindi
        response = translatetext.translate_text(response, 'hi')
        
        
    
    length = text_to_speech.generate_audio(response)

    print(video.generate_subtitles("temp\\record.mp3"))
    video.combine_videos(['temp\\raw.mp4'], length)

    video.generate_video("temp\\final.mp4", "temp\\record.mp3", "temp\\raw.srt")

