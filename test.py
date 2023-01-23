import pyaudio
import wave
 
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
CHUNK = 1024
RECORD_SECONDS = 5
WAVE_OUTPUT_FILENAME = "file.wav"
 
audio = pyaudio.PyAudio()
 
# start Recording
stream = audio.open(format=FORMAT, channels=CHANNELS,
                rate=RATE, input=True,
                frames_per_buffer=CHUNK)
print ("recording...")
frames = []
 
for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
    data = stream.read(CHUNK)
    frames.append(data)
print ("finished recording")
 
 
# stop Recording
stream.stop_stream()
stream.close()
audio.terminate()
 
waveFile = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
waveFile.setnchannels(CHANNELS)
waveFile.setsampwidth(audio.get_sample_size(FORMAT))
waveFile.setframerate(RATE)
waveFile.writeframes(b''.join(frames))
waveFile.close()









# import pyaudio

# # Open two audio streams, one for the microphone and one for PC sound
# p = pyaudio.PyAudio()
# microphone_stream = p.open(format=pyaudio.paInt16, channels=1, rate=44100, input=True, input_device_index=1)
# pc_sound_stream = p.open(format=pyaudio.paInt16, channels=2, rate=44100, input=True, input_device_index=0)

# # Start recording
# data_microphone = microphone_stream.read(1024)
# data_pc_sound = pc_sound_stream.read(1024)

# # Close the streams
# microphone_stream.stop_stream()
# microphone_stream.close()
# pc_sound_stream.stop_stream()
# pc_sound_stream.close()
# p.terminate()

# # Write the data to a file
# with open("recording.wav", "wb") as outfile:
#     outfile.write(data_microphone + data_pc_sound)