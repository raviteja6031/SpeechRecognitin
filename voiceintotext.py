import pyaudio
import wave
import speech_recognition as sr
import subprocess

def say(text):
    subprocess.call("PowerShell -Command Add-Type –AssemblyName System.Speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak('"+ text +"')",shell=True)

def play_audio(filename):
    chunk = 1024
    wf = wave.open(filename, 'rb')
    pa = pyaudio.PyAudio()

    stream = pa.open(
        format=pa.get_format_from_width(wf.getsampwidth()),
        channels=wf.getnchannels(),
        rate=wf.getframerate(),
        output=True
    )

    data_stream = wf.readframes(chunk)

    while data_stream:
        stream.write(data_stream)
        data_stream = wf.readframes(chunk)

    stream.close()
    pa.terminate()
play_audio("./intro.wav")

r = sr.Recognizer()
def initSpeech():
    print("Listening...")
    play_audio("./middle.wav")

    with sr.Microphone() as source:
        print("Say Something")
        audio = r.listen(source)

    play_audio("./stop.wav")

    command = ""

    try:
        command = r.recognize_google(audio)
        print("Your command:")
        print(command)
        say('hai my name is rambo and you said that '+command)
        with open('speech.txt','w+') as f:
            f.write('You said that "'+command+'"')
    except:
        print("Couldn't understand you, bro.")
if __name__ == "__main__":
    initSpeech()
