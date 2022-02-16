# importing libraries 
import speech_recognition as sr 


# initialize the recognizer
r = sr.Recognizer()

# sr.Microphone.list_microphone_names() # all available mics


with sr.Microphone() as source:
    # read the audio data from the default microphone
    r.adjust_for_ambient_noise(source) # კალიბრაცია / ხმაურის ამოცნობა

    print("Speek... ")
    audio_data = r.record(source, duration=5)
    print("Recognizing...")

    try:
        # convert speech to text
        response = r.recognize_google(audio_data, show_all=True, language="ka_GE")
        print(response)

        with open("text.txt", 'w') as f:
            f.write(response)
    except:
        print("Can't recogize what you said")