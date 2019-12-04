print("Hello World!")
help("keywords")
counties = ["Arapahoe", "Denver", "Jefferson"]
counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}
if "El Paso" in counties:
    print("El Paso is in the list of counties.")
else:
    print("El Paso is not in the list of counties.")
    
if "Arapahoe" and "El Paso" in counties:
    print("Arapahoe and El Paso are in the list of counties.")
else:
    print("Arapahoe or El Paso is not in the list of counties.")

if "Arapahoe" or "El Paso" in counties:
    print("Arapahoe or El Paso are in the list of counties.")
else:
    print("Arapahoe and El Paso is not in the list of counties.")


if "Arapahoe" or "El Paso" in counties:
    print("Arapahoe or El Paso is in the list of counties.")
else:
    print("Arapahoe and El Paso are not in the list of counties.")


for county in counties:
    print(county)

numbers = [0, 1, 2, 3, 4]
for num in numbers:
    print(num)

for num in range(5):
    print(num)

for i in range(len(counties)):
    print(counties[i])

for county in counties_dict:
    print(county)

counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}

for county in counties_dict:
    print(county)

for county in counties_dict.keys():
    print(county)

for county in counties_dict.values():
    print(county)

for county in counties_dict.keys():
    print(county)
for county, voters in counties_dict.items():
    print(county, voters)

for county, voters in counties_dict.items():
     print(f"The {county} county has {voters:,} registered voters.")

voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
                {"county":"Denver", "registered_voters": 463335},
                {"county":"Jefferson", "registered_voters": 432438}]

for county_dict in voting_data:
    print(county_dict)

for county_dict in voting_data:
    for value in county_dict.values():
        print(value)





