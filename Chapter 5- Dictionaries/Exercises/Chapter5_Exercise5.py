## Exercise 5: Pets :ballot_box_with_check:

pets = []

pet = {
    "Animal breed": "Himalayan cat",
    "Pet name": "Ancelin",
    "Owner": "Me",
    "Weight": "4 kg",
    "Diet": "Meat",
}
pets.append(pet)

pet = {
    "Animal breed": "Newfoundland dog",
    "Pet name": "Toffe",
    "Owner": "Me",
    "Weight": " 60 kg",
    "Diet": "Meat",
}
pets.append(pet)

for pet in pets:
    print(f"\nLet me tell you about by pet aka the love of my life, {pet['Pet name'].title()}:")
    for key, value in pet.items():
        print(f"\t{key}: {value}")