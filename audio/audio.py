import pyaudio
import wave
from pydub.playback import play
from pydub import AudioSegment
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
        
        token = get_random_string(length=6)
        print("token")
        print(contador)
        
        print("2222")
        print(id_usuario)
        print('Estoy en audio.py')
        # # Definicion de parametros
        # FORMAT = pyaudio.paInt16  # formato de los samples
        # CHANNELS = 2  # Numero de canales
        # RATE = 44100                    #
        # CHUNK = 1024
        # duracion = 5
        global archivo
        print('global archivo')
        # f"archivos_media/voz/grabacion{token}.wav"
        archivo = 'AudioPrueba2.wav';
        # iniciamos "pyaudio"
        global audio
        audio = pyaudio.PyAudio()
        print(audio);
        print('global audio');

        global stream
        stream = audio.open(format=FORMAT, channels=CHANNELS,
                            rate=RATE, input=True,
                            frames_per_buffer=CHUNK);
        
        print(stream);
        print('stream');

        # INICIO DE GRABACION

        print("grabando....");
        global frames
        frames = []

        for i in range(0, int(RATE/CHUNK*duracion)):
            data = stream.read(CHUNK)
            frames.append(data)

        # detenemos grabacion
        stream.stop_stream()
        stream.close()
        audio.terminate()
        print("grabacion terminada")
        
        
        
         #creamos/guaramos el archivo de audio
         
        waveFile = wave.open(archivo, 'wb')
        waveFile.setnchannels(CHANNELS)
        waveFile.setsampwidth(audio.get_sample_size(FORMAT))
        waveFile.setframerate(RATE)
        waveFile.writeframes(b''.join(frames))
        waveFile.close()
        
        #print(waveFile)
        
        
        
        # Abrir el archivo MP3
        #mp3_file = wave.open('song.wav', "rb")
        #print(mp3_file)
        
        # Leer los datos del archivo MP3
        #mp3_data = mp3_file.readframes(mp3_file.getnframes())
        
        # Cerrar el archivo MP3
        #mp3_file.close()
        #print(mp3_data)
        # Ahora puedes hacer algo con los datos de audio en la variable "mp3_data"

        
        
        
        
        #audio = AudioSegment.from_wav("song.wav")
        #print(audio)
        
        
        

        #sound = AudioSegment.from_file("ff.wav", format="wav")
        #play(sound)
        #print(sound)
      
        
        # audio2 = AudioSegment.from_mp3("click1.mp3")
        
        
        
        
        
        with open(archivo, "rb") as file:
        # Lee los datos del archivo
            data = file.read()
            print(data)
            print("------------")
        # Convierte los datos en un objeto binario
        binary_data = bytes(data)
        #print(binary_data);
        
        
        
        
        db.insert_metronomo(archivo,  data)  #
        # db.update_audio(archivo)
        
        
        
        

        


