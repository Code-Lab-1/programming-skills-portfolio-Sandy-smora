## Exercise 5: No Pastrami :ballot_box_with_check:

sandwich = ["chicken", "pastrami", "beef", "turkey", "pastrami", "vegan", "pastrami"]
done_sandwich = []

print("Unfortunately, we're all out of pastrami")
while 'pastrami' in sandwich:
    sandwich.remove('pastrami')

print("\n")
while sandwich:
    not_done = sandwich.pop()
    print(f"The {done_sandwich} is not done yet.")
    done_sandwich.append(done_sandwich)

print("\n")
for sandwich in done_sandwich:
    print(f"Your {done_sandwich} is done")