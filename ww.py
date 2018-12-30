from random import randint
import string

character_category_choice_list = ["lowcase","uppercase","number","symbole"]
character_category_response_list = []

"1. Enter the Password Lenght"
while True:
    try:
        password_lenght_entered = abs(int(input("Password Lenght?")))
        if 0 <= password_lenght_entered < 6:
          print("higher")
        elif 6 <= password_lenght_entered <= 15:
          print("weak")
          character_category_response_list.append(password_lenght_entered)
          break
        elif 16 <= password_lenght_entered <=30:
          print("strong")
          character_category_response_list.append(password_lenght_entered)
          break
        elif password_lenght_entered >= 50:
          print("lower")
    except ValueError :
        print("error")
        continue

"2. Choose the Categories of Characters"
a = 0

while a < len(character_category_choice_list):
  while True:
    try:
      character_included_input = int(input(character_category_choice_list[a] + " ?"))
      if character_included_input == 1:
        print(character_category_choice_list[a] + " : True")
        a += 1
        character_category_response_list.append(character_included_input)
        break
      elif character_included_input == 0:
        print(character_category_choice_list[a] + " : False")
        a += 1
        character_category_response_list.append(character_included_input)
        break
    except ValueError:
      print("yah or nah")
      continue
  if len(character_category_response_list) == len(character_category_choice_list) + 1:
    print(character_category_response_list)

"3. Create a String with all the Character Categories selected"
character_category_string_list = (string.ascii_lowercase,string.ascii_uppercase,string.digits,string.punctuation)
chosen_character_string = ""
b = 0

while b < len(character_category_string_list):
  while True:
    if character_category_response_list[b+1] == 1:
      chosen_character_string += character_category_string_list[b]
      b += 1
      break
    elif character_category_response_list[b+1] == 0:
      b += 1
      break
  if b == len(character_category_string_list):
    print(chosen_character_string)

"4. Generated a Password"
password_generated = ""
c = 0

while c < character_category_response_list[0]:
  while True:
    password_generated += chosen_character_string[randint(0,len(chosen_character_string))]
    c += 1
    break
  if c == character_category_response_list[0]:
    print(password_generated)
    