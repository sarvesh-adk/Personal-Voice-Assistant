# Voice Assistant "Leo" 🎙️  

This is a Python-based voice assistant named "Leo" that listens for specific wake words, processes speech input, generates responses using OpenAI's GPT-3, and replies using text-to-speech (TTS).  

## Features ✨  
- **Wake Word Detection**: Responds to wake words like "hi leo," "hey leo," etc.  
- **Speech Recognition**: Converts user speech to text using Google Speech Recognition.  
- **AI-Powered Responses**: Generates responses using OpenAI's GPT-3 API.  
- **Text-to-Speech (TTS)**: Converts the generated response into speech using Google Text-to-Speech (gTTS).  
- **Audio Playback**: Plays the response audio using the `playsound` library.  

## Requirements 🛠️  

### Python Libraries  
Install the following Python libraries:  
- `openai`  
- `speech_recognition`  
- `gtts`  
- `playsound`  

You can install these using `pip`:  

pip install openai speechrecognition gtts playsound

## API Key

    Interact with Leo:
        Say a wake word like "hi leo" to activate the assistant.
        Ask questions or give commands.
        Say "stop" or "bye" to end the conversation.

    Audio Feedback:
    The assistant will respond with audio playback of its replies.

 ## Customization ⚙️

    Wake Words:
    Modify the wake_words list in the script to add or change the words that trigger the assistant.

    Response Settings:
    Adjust GPT-3 settings like max_tokens and temperature in the get_response function to customize response length and creativity.

## Limitations 🚧

    Requires a stable internet connection for speech recognition and GPT-3 API calls.
    Limited by the capabilities of the Google Speech Recognition and OpenAI GPT-3 APIs.

## License 📜

This project is open-source and available under the MIT License.

## Acknowledgments 🙌

    OpenAI GPT-3 for powering intelligent responses.
    Google Speech Recognition for accurate speech-to-text conversion.
    gTTS for text-to-speech conversion.
    Playsound for audio playback.

