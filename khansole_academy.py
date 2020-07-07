import random

MAX_NUM = 90
MIN_NUM = 10
ANSWERS_REQUIRED = 3

# this will keep track of the answers the get right in a row
correct_answers = 0

# optional function to get random number to make it look cleaner
# repeated code can be simplified into functions like this
def get_random_number():
  return random.randint(MIN_NUM, MAX_NUM)

def main():
  # This will fail when correct_answers is 3, then the program is over
  while correct_answers < ANSWERS_REQUIRED:
    # you can do it the way you were doing it before too,
    # the function is optional
    num1 = get_random_number()
    num2 = get_random_number()
    expected_answer = num1 + num2

    # save this as a string still since we want to use the
    # string version to print later
    answer = input(str(num1) + "+" + str(num2))
    print("Your answer: " + answer)

    if int(answer) == num1 + num2:
      # This will make it closer to exiting the while loop
      print("Correct")
      correct_answers += 1
    else:
      print("Incorrect, The expected answer is " + str(expected_answer))
      # Reset there answers back to zero, this will keep the program going
      correct_answers = 0




main()