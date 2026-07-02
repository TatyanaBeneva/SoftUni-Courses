country_names = input().split(", ")
capital_names = input().split(", ")

country_dict = {country: capital for country, capital in zip(country_names, capital_names)}

for key, value in country_dict.items():
    print(f"{key} -> {value}")