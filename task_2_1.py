import time

def fizzbuzz(n,last_number):
    total = last_number + n
    if total % 3 == 0 and total % 5 == 0:
        return "fizzbuzz"
    elif total % 3 == 0:
        return "fizz"
    elif total % 5 == 0:
        return "buzz"
    else:
        return str(total)

def play_game(limit=20):
    print("Welcome to fizzbuzz game!")
    print("Rules: \n1. You and the computer will take turns counting up to a limit.")
    print("2. For multiples of 3, say 'fizz' instead of the number.")
    print("3. For multiples of 5, say 'buzz' instead of the number.")
    print("4. For multiples of both 3 and 5, say 'fizzbuzz'.")
    print(f"5. The game will go up to {limit}.")
    start = input('press y to start:')
    if start.lower() != 'y':
        print("bye bye")
        return
    else:
        last_number = 0
        for i in range(1, limit + 1):
            if i % 2 == 0:
                answer = input(f"Your turn! Enter the number for {last_number + i}: ").lower()
                correct = fizzbuzz(i, last_number)
                if answer != correct:
                    print(f"HA! You lost. The correct answer was {correct}. Game over!")
                    return  
                last_number = i
            else:  
                time.sleep(1)
                comp_answer = fizzbuzz(i, last_number)
                print(f"Computer's turn for {i + last_number}: {comp_answer}")
                last_number = i
        print("yeeeeeeeeeeah! You Won.")

play_game()
    
        
