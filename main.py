import os
import wave
import json
import vosk
#
# инициализируем модель распознавания речи
model = vosk.Model("model/big_model_ru")
#https://alphacephei.com/vosk/models

# открываем аудиофайл и создаем объект для чтения данных
filename = "audio.wav"
os.system(f'ffmpeg -i {filename} -acodec pcm_s16le -ar 16000 {filename}.wav')
wf = wave.open(f"{filename}", "rb")

# создаем объект распознавания речи
rec = vosk.KaldiRecognizer(model, wf.getframerate())
# читаем данные из аудиофайла и передаем их на распознавание
t=''
while True:
    data = wf.readframes(4000)
    if len(data) == 0:
        break
    if rec.AcceptWaveform(data):
        result = json.loads(rec.Result())
        t += result['text']
        print(result["text"])
print(t)

# получаем окончательный результат распознавания

result = json.loads(rec.FinalResult())
print(result)


# закрываем аудиофайл
wf.close()
