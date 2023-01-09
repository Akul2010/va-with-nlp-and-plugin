def is_valid_command(command):
  return "weather" in command

def handle_command(command, engine):
  # Use an API or web scraper to get the current weather
  weather = get_current_weather()
  # Use the text-to-speech engine to speak the weather
  engine.say(f"The weather is currently {weather}.")
  engine.runAndWait()
