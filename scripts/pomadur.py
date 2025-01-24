import threading
import time
import os
from pyfiglet import Figlet


# Configure pyfiglet
figlet = Figlet(font="slant")


def clear_screen():
  os.system("cls" if os.name == "nt" else "clear")


class Pomadur:
  """It is my own class for Pomadur app"""

  def __init__(self,
               work_minutes,
               break_minutes,
               big_break_time,
               pomodors_before_big_break) -> None:
    # Gets arguments
    self.work_minutes = work_minutes
    self.break_minutes = break_minutes
    self.big_break_time = big_break_time
    self.pomodors_before_big_break = pomodors_before_big_break

    # Threads objects
    self.pomadur_thread = None
    self.pomadur_seeker_thread = None

    # For check if thread is alive
    self.pomadur_alive = False

    # For check if pomodoro ended
    self.pomadur_ended = False

  def draw_border(self, border_length=1, border_sym='=') -> None:
    for i in range(border_length):
      print(border_sym, end='')

    print()

  def display_pomadur_info(self, mode, minutes) -> None:
    seconds = minutes * 60

    # List of pomadur info
    info = [
      f"Mode: {mode}",
      f"Minutes: {minutes}",
      f"Total seconds: {seconds}",
      f"Big break after: {self.pomodors_left_before_big_break}",
    ]

    # Get the longest line
    border_length = int(len(max(info, key=len)))

    print()

    # Draw pomadur info with beautiful borders
    self.draw_border(border_length)

    for current_info in info:
      print(current_info)

    self.draw_border(border_length)

  def start_pomadur_seeker(self) -> None:
    """Watches, switches and starts new threads for Pomodoros"""

    # Pomadur mode at start by default
    current_mode = "work"

    # Gets number of pomodoros before big break
    self.pomodors_left_before_big_break = self.pomodors_before_big_break

    # Start thread with default mode
    self.pomadur_thread = threading.Thread(target=self.start_pomadur, args=(current_mode,))
    self.pomadur_thread.start()

    # This loop will work infinity while until it is stopped
    while self.pomadur_alive:
      # Checks if pomodoro timer ended
      if self.pomadur_ended:
        # Kills pomodoro timer thread
        self.pomadur_thread.join()
        
        # Now pomodoro not ended
        self.pomadur_ended = False

        # Modes switcher
        if current_mode == "work":
          # Counts down pomodoros to big break for working pomodoros only
          self.pomodors_left_before_big_break -= 1

          # Start big break if pomdoros before big break = 0,
          # otherwise start regular break
          if self.pomodors_left_before_big_break == 0:
            current_mode = "bigbreak"
          else:
            current_mode = "break"
        elif current_mode == "break":
          current_mode = "work"
        elif current_mode == "bigbreak":
          # Resets the pomodoro counter before the big break
          self.pomodors_left_before_big_break = self.pomodors_before_big_break

          # Next pomodoro mode after big break is work
          current_mode = "work"

        # Start new timer
        self.pomadur_thread = threading.Thread(target=self.start_pomadur, args=(current_mode,))
        self.pomadur_thread.start()

      time.sleep(1)

  def start_pomadur(self, mode="work") -> bool:
    """
    Starts pomdoro with specific mode and countdown seconds like timer

    args:
      mode:
        Maybe "work" for regular timer,
        "break" for regular break and
        "bigbreak" for big break

    return:
      False if mode not found
    """

    # Gets pomadur mode and minutes for it's mode
    if mode == "work":
      pomadoro_minutes = self.work_minutes
    elif mode == "break":
      pomadoro_minutes = self.break_minutes
    elif mode == "bigbreak":
      pomadoro_minutes = self.big_break_time
    else:
      return False

    # Gets pomodoro total seconds
    pomadoro_seconds = pomadoro_minutes * 60

    # Copy variable for show minutes and seconds in info
    # because minutes value changing in loop
    pomadoro_minutes_copy = pomadoro_minutes

    seconds_counter = 0

    # Pomadur main logic
    for second in range(pomadoro_seconds):
      pomadoro_minutes_string = f"{pomadoro_minutes}"
      seconds_counter_string = f"{seconds_counter}"

      # Add leading zero for minutes
      if pomadoro_minutes < 10:
        pomadoro_minutes_string = f"0{pomadoro_minutes}"

      # Add leading zero for seconds
      if seconds_counter < 10:
        seconds_counter_string = f"0{seconds_counter}"

      if seconds_counter == 0:
        pomadoro_minutes -= 1
        seconds_counter = 60

      # Draw pomadur time
      self.display_pomadur_info(mode, pomadoro_minutes_copy)
      print(figlet.renderText(f"{pomadoro_minutes_string}:{seconds_counter_string}"), end="\r")

      seconds_counter -= 1

      time.sleep(1)

      # Clear terminal
      clear_screen()

    self.pomadur_ended = True

    print("=======")
    print(" ended ")
    print("=======")

  def start(self) -> None:
    """Starts pomodoro seeker for pomodoro control"""

    self.pomadur_alive = True

    clear_screen()

    self.pomadur_seeker_thread = threading.Thread(target=self.start_pomadur_seeker, args=())
    self.pomadur_seeker_thread.start()

  def stop(self):
    """Stops all pomodoro threads"""

    self.pomadur_alive = False

    self.pomadur_thread.join()
    self.pomadur_seeker_thread.join()
