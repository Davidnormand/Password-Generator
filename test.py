"trying to make sure that we have at least one character by categories"
import string

character_category_response_list = [16,1,1,1,1]
character_category_string_list = (string.ascii_lowercase,string.ascii_uppercase,string.digits,string.punctuation)

password_generated = str("abcde")

b = 1
d = 0
e = 0

while b < len(character_category_string_list):
    if character_category_string_list[b] == 0:
        b += 1
        break
    elif character_category_string_list[b] == 1:
        while d < len(password_generated):
            while True:
                e += character_category_string_list[b].find(password_generated[d])
                d += 1
                break
        if len(password_generated) == -e:
            print("repeat")
        else:
            print("ok")
        b += 1
        break