## Exercise 4: Deli :ballot_box_with_check:

sandwich = ["chicken", "beef", "turkey", "vegan"]
done_sandwich = []

while sandwich:
    not_done = sandwich.pop()
    print(f"The {done_sandwich} is not done yet.")
    done_sandwich.append(done_sandwich)

print("\n")
for sandwich in done_sandwich:
    print(f"Your {done_sandwich} is done")
