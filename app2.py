from flask import Flask
from pygame import mixer
import os   

mixer.init()
app = Flask(__name__)


class App:
    def __init__(self):
        mixer.init()
        self.music_folder = 'C:/PycharmProject/MusicServer/MusicProject'
        self.play_music()

    def play_music(self):
        for file_name in os.listdir(self.music_folder):
            if file_name.endswith('.mp3'):  # Puedes ajustar la extensión de archivo según tus necesidades
                file_path = os.path.join(self.music_folder, file_name)
                mixer.music.load(file_path)
                mixer.music.play()
        return 'Reproduciendo Musica'

    def stop_music(self):
        mixer.music.stop()
        return 'Musica detenida'


my_app = App()

@app.route('/play')
def play_music():
    return my_app.play_music()

@app.route('/stop')
def stop_music():
    return my_app.stop_music()

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080)
