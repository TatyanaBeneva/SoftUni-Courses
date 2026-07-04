country_names = input().split(", ")
capital_names = input().split(", ")

country_dict = {country: capital for country, capital in zip(country_names, capital_names)}
# country_dict = dict(zip(country_names, capital_names))
# country_dict = {country_names[index]: capital_names[index] for index in range(len(country_names))}

for key, value in country_dict.items():
    print(f"{key} -> {value}")