import threading
import time


class Pomadur:
  """It is my own class for Pomadur app"""

  def __init__(self, work_minutes, break_minutes, big_break_time):
    self.work_minutes = work_minutes
    self.break_minutes = break_minutes
    self.big_break_time = big_break_time

    self.pomadur_thread = None
    self.pomadur_alive = False

  def start_pomadur(self):
    work_seconds = self.work_minutes * 60

    for second in range(work_seconds):
      if second >= work_seconds:
        self.pomadur_alive = False

      print(second)

      time.sleep(1)

  def start(self):
    self.pomadur_alive = True

    self.pomadur_thread = threading.Thread(target=self.start_pomadur, args=())
    self.pomadur_thread.start()

  def stop(self):
    self.pomadur_alive = False
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
