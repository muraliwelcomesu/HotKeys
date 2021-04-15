'''
Created on Sep 7, 2020

@author: MURENGAR
'''
import pyttsx3
import winsound

def beep():
    frequency = 2500  # Set Frequency To 2500 Hertz
    duration = 100  # Set Duration To 1000 ms == 1 second
    winsound.Beep(frequency, duration)

def PlayResponse(audio):
    print(audio)
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    en_voice_id = "com.apple.speech.synthesis.voice.Alex"
    #en_voice_id = "com.apple.speech.synthesis.voice.damayanti"
    engine.setProperty('voice', en_voice_id)
    #engine.setProperty("voice", voices[1].id)
    #engine.save_to_file(audio, "output.mp3")
    engine.say(audio)
    engine.runAndWait()

if __name__ == '__main__':
    l_file = input('Enter the file with complete path  to Read')
    fp = open(l_file,'r')
    for lines in fp:
        PlayResponse(lines)
    print('Completed')
        