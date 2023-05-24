# your code goes here!

#Function countdown() in countdown.py counts down from number and prints "HAPPY NEW YEAR!" - AssertionError: assert '5\n' == '5 SECOND(S)!...Y NEW YEAR!\n'

def countdown(start_countdown):
    # start_countdown = 5
    while start_countdown > 0:
        print(f'{start_countdown} SECOND(S)!')
        start_countdown -= 1
    print("HAPPY NEW YEAR!")
countdown(5)


def countdown_with_sleep(start_countdown):
     # start_countdown = 5
    while start_countdown > 0:
        print(f'{start_countdown} SECOND(S)!')
        start_countdown -= 1
    print("HAPPY NEW YEAR!")
countdown(5)