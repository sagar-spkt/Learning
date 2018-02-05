import speech_recognition as sr

mic_name = 'Microphone (WO Mic Device)'

sample_rate = 48000

chunk_size = 2048

r = sr.Recognizer()

mic_list = sr.Microphone.list_microphone_names()

for i, microphone_name in enumerate(mic_list):
    if microphone_name == mic_name:
        device_id = i

with sr.Microphone(device_index=device_id, sample_rate=sample_rate, chunk_size=chunk_size) as source:
    r.adjust_for_ambient_noise(source)
    print("Say Something")
    audio = r.listen(source)

    try:
        text = r.recognize_google(audio)
        print("you said: " + text)

    except sr.UnknownValueError:
        print("Speech Recognition could not understand audio")

    except sr.RequestError as e:
        print("Could not request results")
