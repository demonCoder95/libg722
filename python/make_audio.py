import wave

audio_data = None
with open('g722.output', 'rb') as f:
    audio_data = f.read()

with wave.open("g722.wav", "wb") as f:
    f.setframerate(8000)
    f.setnchannels(1)
    f.setsampwidth(2)
    f.writeframesraw(audio_data)

print("Done")