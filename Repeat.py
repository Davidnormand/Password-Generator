"5. Repeat"
while True:
  try:
    repeat_input = int(input("Repeat"))
    while True:
      if repeat_input == 1:
        print("a")
        break
      elif repeat_input == 0:
        break
  except ValueError:
    continue