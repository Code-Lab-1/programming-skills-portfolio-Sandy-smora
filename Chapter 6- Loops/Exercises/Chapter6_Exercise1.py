## Exercise 1: Pizza Toppings :ballot_box_with_check:

prompt = "\n What toppings do you prefer on your pizza?"
prompt += "\n Enter 'quit' once finished"

while True:
    topping = input(prompt)
    if topping != "quit":
        print(f"{topping} is added to the pizza")
    else:
        break
