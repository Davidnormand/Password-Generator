countries={'TW':'Taiwan','JP':'Japan','AUS':'Australia'}

def add_country():

    while True:
        new_short=raw_input('Country Name in short:')
        new_full=raw_input('Country Name in full:')
        countries[new_short]=new_full
        answer=raw_input('want to add more?')
        if answer in ('yes'):
            return True 
        if answer in ('no'):
            return False

    print countries

add_country()