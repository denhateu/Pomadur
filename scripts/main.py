import threading
import time


class Pomadur:
  """It is my own class for Pomadur app"""

  def __init__(self, work_minutes, break_minutes, big_break_time):
    self.work_minutes = work_minutes
    self.break_minutes = break_minutes
    self.big_break_time = big_break_time

    self.pomadur_thread = None

  def start_pomadur(self, mode="work"):
    # Gets pomadur mode and minutes for it's mode
    if mode == "work":
      pomadoro_minutes = self.work_minutes
    elif mode == "break":
      pomadoro_minutes = self.break_minutes
    elif mode == "bigbreak":
      pomadoro_minutes = self.big_break_time

    pomadoro_seconds = pomadoro_minutes * 60

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

  def start(self):
    self.pomadur_thread = threading.Thread(target=self.start_pomadur, args=("work",))
    self.pomadur_thread.start()

  def stop(self):
    self.pomadur_thread.join()


def main():
  # Setup pomodoro minutes
  work_time = 1
  break_time = 5
  big_break_time = 15

  # Starts pomodoro counter
  pomadur = Pomadur(work_time, break_time, big_break_time)
  pomadur.start()

if __name__ == "__main__":
  main()
