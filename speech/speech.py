import pyttsx3

file_location = "speech\speech.txt"

def read_aloud_from_file(filename):
    # Read the text from the file with utf-8 encoding
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            text = file.read()
    except FileNotFoundError:
        print("The file 'speech.txt' was not found.")
        return
    except UnicodeDecodeError:
        print("There was an issue decoding the file. Check for unsupported characters.")
        return

    # Initialize the text-to-speech engine
    engine = pyttsx3.init()
    
    # Set properties if needed (e.g., rate, volume)
    engine.setProperty('rate', 150)  # Speed of speech
    engine.setProperty('volume', 0.9)  # Volume 0-1

    # Speak the text
    engine.say(text)
    engine.runAndWait()

# Run the function
read_aloud_from_file(file_location)
