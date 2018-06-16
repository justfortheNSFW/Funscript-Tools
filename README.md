# Funscript-Tools

Hey people, donations in XMR to this address: 427zxTu5XprGVXw5boeNkLYZh2E3TVz2fFVnpGZ452h1XBwP9BZy6r7YWnmdoTSAVW6ayR5dWHmyDJqzeR4gfKhbVhpckxM

This repository will hold all python scripts I've developed to facilitate the creation of .funscript files.

It will revolve around a base create_funscript class that will take time and position arguements and output a .funscript file when called.

I have added the audio_to_funscript class that will take either a mp3 or mp4 file and uses the aubio library's onset detection to automatically generate a funscript file to match the audio/movie. The result is less consistant than I had hoped initially and the next thing I am planning to add will be something based on opencv and targeting the beat meters in cock hero videos.

I've written this in Python 3.6.1

Dependancies:
aubio https://aubio.org/manual/latest/python_module.html#python  
scriptplayer https://github.com/FredTungsten

Misc Useful whls:  

pyHook-1.5.1-cp36-cp36m-win_amd64.whl  
pyserial-3.4-py2.py3-none-any.whl  
pygame-1.9.3-cp36-cp36m-win_amd64.whl  

