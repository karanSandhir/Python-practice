import speech_recognition as sr

# List all available microphones
for index, name in enumerate(sr.Microphone.list_microphone_names()):
    print(f"{index}: {name}")
