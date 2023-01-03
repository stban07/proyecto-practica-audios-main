import pyaudio
import wave
from audio.dbherlper import DBHelper
from django.utils.crypto import get_random_string
from os import system


db = DBHelper()

contador = 1
FORMAT = pyaudio.paInt16  # formato de los samples
CHANNELS = 1  # Numero de canales
RATE = 44100                    #
CHUNK = 1024
duracion = 5


class Audio:

    def grabarAudio(self, id_usuario):
        # Crear token
        print(contador)
        token = get_random_string(length=6)
        print(id_usuario)
        print('Estoy en audio.py')
        # # Definicion de parametros
        # FORMAT = pyaudio.paInt16  # formato de los samples
        # CHANNELS = 2  # Numero de canales
        # RATE = 44100                    #
        # CHUNK = 1024
        # duracion = 5
        global archivo
        archivo = f"archivos_media/voz/grabacion{token}.wav"

        # iniciamos "pyaudio"
        global audio
        audio = pyaudio.PyAudio()

        global stream
        stream = audio.open(format=FORMAT, channels=CHANNELS,
                            rate=RATE, input=True,
                            frames_per_buffer=CHUNK)

        # INICIO DE GRABACION

        print("grabando....")
        global frames
        frames = []

        for i in range(0, int(RATE/CHUNK*duracion)):
            data = stream.read(CHUNK)
            frames.append(data)

        print("grabacion terminada")

        # detenemos grabacion
        stream.stop_stream()
        stream.close()
        audio.terminate()

        # creamos/guaramos el archivo de audio
        waveFile = wave.open(archivo, 'wb')
        waveFile.setnchannels(CHANNELS)
        waveFile.setsampwidth(audio.get_sample_size(FORMAT))
        waveFile.setframerate(RATE)
        waveFile.writeframes(b''.join(frames))

        waveFile.close()

        db.insert_metronomo(id_usuario, archivo)  #
        db.update_audio(archivo)
