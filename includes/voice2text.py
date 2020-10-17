import speech_recognition as sr

def getWord(AUDIO_FILE, words, pos):
        r = sr.Recognizer()
        with sr.AudioFile(AUDIO_FILE) as source: 
        	audio = r.record(source)
        try:
                print("The audio file contains : " + r.recognize_google(audio)) 
                words[pos] = r.recognize_google(audio)
                return
        except sr.UnknownValueError: 
                print("Google Speech Recognition could not understand audio")
        except sr.RequestError as e: 
                print("Could not request results from Google Speech Recognition service; {0}".format(e))
        words[pos] = ' '
