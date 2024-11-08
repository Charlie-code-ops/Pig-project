import random
import time

OPERATORS = ["+", "-", "*"]
MIN_OPERAND = 2
MAX_OPERAND = 12
TOTAL_PROBLEMS = 10



def generate_problem():
    left = random.randint(MIN_OPERAND, MAX_OPERAND)
    right = random.randint(MIN_OPERAND, MAX_OPERAND)
    operator = random.choice(OPERATORS) #.choice is basically random of any operator listed within the list

    expr = str(left) + " " + operator + " " + str(right) #has to have str since cant read intergers
    
    #since code generates all questions, using eval function is much quicker way of checking the random expressions the player is provided with rather than using many if statements
    answer = eval(expr) #eval is a function which evaluates a string as if it were a python expression, in this case expr
    return expr, answer


wrong = 0 
input("Press Enter to start!")
print("---------------------")

start_time = time.time() #gives us the time stamp in seconds

for i in range(TOTAL_PROBLEMS):
    expr, answer = generate_problem()
    while True:
        guess = input("Problem #" + str(i + 1) + ": " + expr + " = ")
        if guess == str(answer):
            break
        wrong += 1

end_time = time.time()
total_time = round(end_time - start_time, 2)


print("---------------------")
print("Nice Work! You finished in", total_time, "seconds!")