"""
    Below is a simple random number guessing game with 3 credits given at max
"""

import random as r

random_number = r.randint(0, 100) 
count = 0
# The above values must live outsite the loop to avoid changing/renewing


print(f"The Random Number Guessing Game\n")

while True:
    if count != 3:
        try:
            guessed_number = int(input(f"Predict the random value: "))
        except ValueError:
            count += 1
            print(f"Invalid input!\ntry again, {3 - count} tries left.\n")
            if count == 3:
                print(f"You lose!!!\nThe random number was {random_number}\n")
                break
        else:
            if guessed_number == random_number:
                print(f"You Win!!!\nyou have guessed the correct number\n")
                break
            elif guessed_number < random_number:
                count += 1
                print(f"Incorrect!!!\nyour guessed number is slightly less than the correct one\ntry again {3 - count} tries left.\n")
                
                if count == 3:
                    count +=1
                    print(f"You lose!!!\nThe random number was {random_number}\n")
                    break
            else:
                count += 1
                print(f"Incorrect!!!\nyour guessed number is slightly higher than the correct one\ntry again {3 - count} tries left.\n")
                
                if count == 3:
                    print(f"You lose!!!\nThe random number was {random_number}\n")
                    break

# --- --- --- --- --- --- --- --- --- --- --- ---