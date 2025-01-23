import threading
import time


class Pomadur:
  def __init__(self, work_minutes, break_minutes):
    self.work_minutes = work_minutes
    self.break_minutes = break_minutes

    self.pomadur_thread = None
    self.pomadur_alive = False

  def start_pomadur(self):
    counter = 0

    while self.pomadur_alive:
      if counter >= 25:
        self.pomadur_alive = False

      print(f"counter: {counter}")

      counter += 1

      time.sleep(1)

  def start(self):
    self.pomadur_alive = True

    self.pomadur_thread = threading.Thread(target=self.start_pomadur, args=())
    self.pomadur_thread.start()

  def stop(self):
    self.pomadur_alive = False
    self.pomadur_thread.join()


def main():
  #work_time = 25
  work_time = 6
  break_time = 5

  pomadur = Pomadur(work_time, break_time)
  pomadur.start()
  #pomadur.stop()

if __name__ == "__main__":
  main()
