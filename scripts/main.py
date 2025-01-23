from pomadur import Pomadur


def main():
  # Setup pomodoro minutes
  work_time = 1
  break_time = 1
  big_break_time = 1
  pomodors_before_big_break = 2

  # Starts pomodoro counter
  pomadur = Pomadur(work_time, break_time, big_break_time, pomodors_before_big_break)
  pomadur.start()

if __name__ == "__main__":
  main()
