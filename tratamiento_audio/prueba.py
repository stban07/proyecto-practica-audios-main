import speech_recognition as sr
audio = "grabacioniI0o1F.wav"
re = sr.Recognizer()

with sr.AudioFile(audio) as source:

    info_audio = re.record(source)
    texto = re.recognize_google(info_audio, language="es-ES")
    print(texto)
