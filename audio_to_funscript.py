'''
Created on Sat May 26 21:47:45 2018 @author: justfortheNSFW

Detailed info on onset methods here: https://aubio.org/manpages/latest/aubioonset.1.html

Available onset methods:
default, energy, hfc, complex, phase, specdiff, kl, mkl, specflux

'''

from create_funscript import create_funscript
from aubio import source, onset, tempo

class audio_to_funscript:
    def __init__(self, path, file, method):
        self.win_s = 512 # fft size
        self.hop_s = win_s // 2 # hop size
        self.samplerate = 44100 #44100 is standard for mp3 and seems to work for mp4
        self.path = path # String containing the directory eg 'C:/Users/justfortheNSFW/Downloads/'
        self.file = file # String containing the file name eg 'PMV - Lola Myluv.mp4'
        self.fileName = path + file
        self.funscriptFile = create_funscript("1.0",'false',99) #initialise the funscript object to start writing to
        self.s = source(self.fileName, self.samplerate, self.hop_s) #this creates an object over which to iterate from a source file, seems to work fine with both mp3 and mp4s
        self.o = onset("complex", self.win_s, self.hop_s, self.samplerate) # an onset is the start of a beat, note or sound, you get vastly different outputs when you mess with the variables for method 'hfc' and 'complex' are good ones
        self.isProcessed = False
        print(self.file+' accquired')
        
    def printOnsetVariables(self):
        print('awhitening: '+str(self.o.get_awhitening()))
        print('compression: '+str(self.o.get_compression()))
        print('silence: '+str(self.o.get_silence()))
        print('delay_ms: '+str(self.o.get_delay_ms()))
        print('threshold: '+str(self.o.get_threshold()))
        print('minioi_ms: '+str(self.o.get_minioi_ms()))
    
    def assignOnsetVariables(self, **kwargs):
        if len(kwargs) < 1:
            print("Default variables assigned")
            return self.assignOnsetVariables(threshold=0.15, delay_ms=26.69, silence=-70, compression=1.0, awhitening=1, minioi_ms=50)
        
        updates = []
              
        for kwarg in kwargs:
            if kwarg == 'threshold':
                self.o.set_threshold(kwargs[kwarg]) #float default 0.15
                updates.append({kwarg,kwargs[kwarg]})
            if kwarg == 'delay_ms':
                self.o.set_delay_ms(kwargs[kwarg]) # default 26.69
                updates.append({kwarg,kwargs[kwarg]})
            if kwarg == 'silence':
                self.o.set_silence(kwargs[kwarg]) # int default -70
                updates.append({kwarg,kwargs[kwarg]})
            if kwarg == 'compression':
                self.o.set_compression(kwargs[kwarg]) # float 1.0 default
                updates.append({kwarg,kwargs[kwarg]})
            if kwarg == 'awhitening':
                self.o.set_awhitening(kwargs[kwarg]) # int 1 default
                updates.append({kwarg,kwargs[kwarg]})
            if kwarg == 'minioi_ms':
                self.o.set_minioi_ms(kwargs[kwarg]) # int 50 default
                updates.append({kwarg,kwargs[kwarg]})
                
        return updates

    def processAudio(self):
        # total number of frames read
        if self.isProcessed:
            Print("you've already processed the audio")
            exit
        
        total_frames = 0
        pos = 99
        while True:
            samples, read = self.s()
            if o(samples):
                pos = abs(pos-99)
                self.funscriptFile.addAction(pos,int(self.o.get_last_ms()))
                
            total_frames += read
            if read < self.hop_s: break
        
        self.isProcessed = True
        print('You have successfully processed the audio')

    def outputFile(self):
        #outputs the funscript file, this assumes the source file extension is a full stop followed by 3 characters
        self.funscriptFile.outputFile(path, file[0:len(file)-4])
        print("file has been output to:" + path)
