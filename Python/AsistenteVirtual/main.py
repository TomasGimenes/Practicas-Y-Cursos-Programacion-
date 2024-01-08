import openai, pyttsx3, time
import speech_recognition as sr

openai.api_key = "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"

engine = pyttsx3.init()

def transcibe_audio_to_test(filename):
    recognizer = sr.Recognizer()
    with sr.AudioFile(filename) as source:
        audio = recognizer.record(source)
    try:
        return recognizer.recognize_google(audio, language="es")
    except:
        print("No se ah escuchado")

def generate_response(prompt):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=4000,
        n=1,
        stop=None,
        temperature=0.5,
    )
    return response ["chices"][0]["text"]

def speak_text(text):
    engine.say(text)
    engine.runAndWait()

voices = engine.getProperty('voices')
spanish_voice = None
for voice in voices:
    if "spanish" in voice.languages:
        spanish_voice = voice.id
if spanish_voice is not None:
    engine.setProperty('voice', spanish_voice)


def main():
    while True:
        print("Di 'Hola' para empezar a grabar")
        with sr.Microphone() as source:
            recognizer = sr.Recognizer()
            audio = recognizer.listen(source)
            try:
                transciption = recognizer.recognize_google(audio, language="es")
                if transciption.lower()=="hola":
                    filename = "input.wav"
                    print("Dime que quieres loquita")
                    with sr.Microphone() as source:
                        recognizer = sr.Recognizer()
                        source.pause_threshold=1
                        audio = recognizer.listen(source,phrase_time_limit=None,timeout=None)
                        with open(filename,"wb") as f:
                            f.write(audio.get_wav_data())
                    text = transcibe_audio_to_test(filename)
                    if text:
                        print(f"Yo: {text}")
                        
                        response = generate_response(text)
                        print(f"El bot ese dice: {response}")
                        
                        speak_text(response)
            except Exception as e:
                print("AHHHHH error : {}".format(e))

if __name__ == "__main__":
    main()
                