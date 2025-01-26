import time
import os
import configparser

from config import AUTHOR, APP_NAME, APP_VERSION, CONFIG_FILE
from pomadur import Pomadur


def display_logo() -> None:
  logo = f"""
$$$$$$$\\                                          $$\\                     
$$  __$$\\                                         $$ |                    
$$ |  $$ | $$$$$$\\  $$$$$$\\$$$$\\   $$$$$$\\   $$$$$$$ |$$\\   $$\\  $$$$$$\\  
$$$$$$$  |$$  __$$\\ $$  _$$  _$$\\  \\____$$\\ $$  __$$ |$$ |  $$ |$$  __$$\\ 
$$  ____/ $$ /  $$ |$$ / $$ / $$ | $$$$$$$ |$$ /  $$ |$$ |  $$ |$$ |  \\__|
$$ |      $$ |  $$ |$$ | $$ | $$ |$$  __$$ |$$ |  $$ |$$ |  $$ |$$ |      
$$ |      \\$$$$$$  |$$ | $$ | $$ |\\$$$$$$$ |\\$$$$$$$ |\\$$$$$$  |$$ |   Author: {AUTHOR}
\\__|       \\______/ \\__| \\__| \\__| \\_______| \\_______| \\______/ \\__|   Version: {APP_VERSION}
  """
                                                                          
  print(logo)
  print()
  time.sleep(3)

def create_config(config_file) -> bool:
  config = configparser.ConfigParser()

  # Create default config settings
  config["main"] = {
    "work_minutes": 25,
    "break_minutes": 5,
    "big_break_minutes": 15,
    "pomodors_before_big_break": 4,
  }

  with open(config_file, 'w', encoding="utf-8") as configfile:
    config.write(configfile)

  return True

def read_config(config_file) -> dict:
  config = configparser.ConfigParser()

  # Checks if config file not exists
  if os.path.exists(config_file) is False:
    # Config not exists create default config file
    create_config(config_file)

  # Read the config file
  config.read(config_file)

  # Gets config file values
  work_minutes = config.getint("main", "work_minutes")
  break_minutes = config.getint("main", "break_minutes")
  big_break_minutes = config.getint("main", "big_break_minutes")
  pomodors_before_big_break = config.getint("main", "pomodors_before_big_break")

  config_values = {
    "work_minutes": work_minutes,
    "break_minutes": break_minutes,
    "big_break_minutes": big_break_minutes,
    "pomodors_before_big_break": pomodors_before_big_break
  }

  return config_values

def main():
  # Show logo
  display_logo()

  # Read config file for setup program
  config_values = read_config(CONFIG_FILE)

  # Setup pomodoro minutes
  work_time = config_values["work_minutes"]
  break_time = config_values["break_minutes"]
  big_break_time = config_values["big_break_minutes"]
  pomodors_before_big_break = config_values["pomodors_before_big_break"]

  # Starts pomodoro counter
  pomadur = Pomadur(work_time, break_time, big_break_time, pomodors_before_big_break)
  pomadur.start()

if __name__ == "__main__":
  main()
