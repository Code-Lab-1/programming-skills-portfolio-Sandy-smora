## Exercise 4: Rivers :ballot_box_with_check:

major_river = {
    "Nile": "Egypt",
    "Amazon": "South America",
    "Mississippi": "United States",
    "Yellow River": "China",
}

for major_river, country in major_river.items():
    print(f"The {major_river.title()} flows through {country.title()}.")
