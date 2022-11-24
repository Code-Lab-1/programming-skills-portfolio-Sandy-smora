## Exercise 2: Movie Tickets: :ballot_box_with_check:

tickets1 = "How old are you?"
tickets2 = "\n Enter 'quit' once finished"

while True:
    age = input(tickets1)
    if age == "quit":
        break
    age = int(age)

    if age < 3:
        print("Your tickets is free")
    elif age < 13:
        print("Your ticket is $10")
    else:
        print("Your ticket is $15")
