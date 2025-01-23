import threading
import time


class Pomadur:
  """It is my own class for Pomadur app"""

  def __init__(self, work_minutes, break_minutes, big_break_time, pomodors_before_big_break):
    self.work_minutes = work_minutes
    self.break_minutes = break_minutes
    self.big_break_time = big_break_time
    self.pomodors_before_big_break = pomodors_before_big_break

    self.pomadur_thread = None
    self.pomadur_seeker_thread = None

    self.pomadur_alive = False
    self.pomadur_ended = False

  def start_pomadur_seeker(self):
    current_mode = "work"
    self.pomodors_left_before_big_break = self.pomodors_before_big_break

    self.pomadur_thread = threading.Thread(target=self.start_pomadur, args=(current_mode,))
    self.pomadur_thread.start()

    while self.pomadur_alive:
      if self.pomadur_ended:
        self.pomadur_thread.join()
        
        self.pomadur_ended = False

        if current_mode == "work":
          self.pomodors_left_before_big_break -= 1

          if self.pomodors_left_before_big_break == 0:
            current_mode = "bigbreak"
          else:
            current_mode = "break"
        elif current_mode == "break":
          current_mode = "work"
        elif current_mode == "bigbreak":
          self.pomodors_left_before_big_break = self.pomodors_before_big_break
          current_mode = "work"

        self.pomadur_thread = threading.Thread(target=self.start_pomadur, args=(current_mode,))
        self.pomadur_thread.start()

      time.sleep(1)

  def start_pomadur(self, mode="work"):
    # Gets pomadur mode and minutes for it's mode
    if mode == "work":
      pomadoro_minutes = self.work_minutes
    elif mode == "break":
      pomadoro_minutes = self.break_minutes
    elif mode == "bigbreak":
      pomadoro_minutes = self.big_break_time

    pomadoro_seconds = pomadoro_minutes * 60

    print()
    print("================")
    print(f"Mode: {mode}")
    print(f"Minutes: {pomadoro_minutes}")
    print(f"Total seconds: {pomadoro_seconds}")
    print(f"Big break after: {self.pomodors_left_before_big_break}")
    print("================")
    print()

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
      print(f"{pomadoro_minutes_string}:{seconds_counter_string}")

      seconds_counter -= 1

      time.sleep(1)

    self.pomadur_ended = True

    print("=======")
    print(" ended ")
    print("=======")

  def start(self):
    self.pomadur_alive = True

    self.pomadur_seeker_thread = threading.Thread(target=self.start_pomadur_seeker, args=())
    self.pomadur_seeker_thread.start()

  def stop(self):
    self.pomadur_alive = False

    self.pomadur_thread.join()
    self.pomadur_seeker_thread.join()
