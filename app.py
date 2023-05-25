from flask import Flask
from pygame import mixer
import os   

mixer.init()
app = Flask(__name__)

@app.route('/')
def home():
    return '¡Bienvenido!'

@app.route('/play')
def play_music():
    '''music_folder = 'C:/PycharmProject/MusicServer/MusicProject'
    for file_name in os.listdir(music_folder):
        if file_name.endswith('.mp3'):  # Puedes ajustar la extensión de archivo según tus necesidades
            file_path = os.path.join(music_folder, file_name)
            mixer.music.load(file_path)'''
    mixer.music.load('C:/PycharmProject/MusicServer/MusicProject/X2Download.app - Flores Amarillas (128 kbps).mp3')
    mixer.music.play()
    return 'Reproduciendo Musica'

@app.route('/stop')
def stop_music():
    mixer.music.stop()
    return 'Musica detenida'

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080)
