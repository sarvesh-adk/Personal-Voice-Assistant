import openai # type: ignore
import speech_recognition as sr # type: ignore
from gtts import gTTS # type: ignore
import playsound # type: ignore

# Set up OpenAI API credentials 
openai.api_key = "YOU_API_KEY"

# Set up the speech recognizer
r = sr.Recognizer()

def text_to_speech(text, filename="output.mp3"):
    """
    Converts text to speech and saves the output as an mp3 file.
    """
    tts = gTTS(text=text, lang="en")
    tts.save(filename)

def play_audio(filename):
    """
    Plays the specified audio file.
    """
    playsound.playsound(filename)

def speech_to_text():
    """
    Listens for speech input and returns the text transcription.
    """
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        print("Listening...")
        audio = r.listen(source, phrase_time_limit=3)

        try:
            text = r.recognize_google(audio)
            print(f"You said: {text}")
            return text
        except sr.UnknownValueError:
            print("Could not understand audio")
        except sr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition service; {e}")

# Generating response using OpenAI GPT-3
def get_response(prompt):
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=200,
        n=1,
        stop=None,
        temperature=0.7,
    )
    return response.choices[0].text.strip()

# Define the wake words
wake_words = ["hi leo", "hey leo", "hello", "listen", "leo"]

end = False

# Define the conversation loop
while True:
    # Listen for the wake words
    print("Waiting for wake word...")
    text = speech_to_text()
    if text is None: continue
    text = text.lower()
    if any(wake_word in text for wake_word in wake_words):
        print("Wake word detected!")
        response = "How can I help you?"

        # Keep the conversation going until the user says "stop"
        while True:
            print(response)
            text_to_speech(response, "response.mp3")
            play_audio("response.mp3")

            # Listen for the user's response
            user_input = speech_to_text()
            if user_input is None: continue
            user_input = user_input.lower()

            # Exit the conversation loop if the user says "stop" or "bye"
            if "stop" in user_input or "bye" in user_input:
                print("Bye!")
                end = True
                break

            # Generate a response with ChatGPT
            # prompt = f"Conversation:\nUser: {user_input}\nPeter:"
            response = get_response(user_input)
        
        if end: break

    else:
        print("Could not detect wake word. Listening again...")