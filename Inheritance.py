class AfricanCountry:
    continent = "Africa"
    def __init__(self, name, capital, population, area, language, currency):
        self.name = name
        self.capital = capital
        self.population = population
        self.area = area
        self.language = language
        self.currency = currency

    def describe(self):
        return f"Country Name: {self.name}, Capital: {self.capital}, Population: {self.population}, Area: {self.area} sq km, Languages: {self.language}, Currency: {self.currency}, Location: {AfricanCountry.continent}"


class Kenya(AfricanCountry):
    def unique_feature(self):
        return "Kenya's President is Dr. William Ruto."

class Uganda(AfricanCountry):
    def unique_feature(self):
        return "Uganda's President is Yoweri Museveni."
    
# Creating an instance of Kenya
kenya = Kenya("Kenya", "Nairobi", 53771296, 580367, "Swahili and English", "Kenyan Shilling")

# Creating an instance of Uganda
uganda = Uganda("Uganda", "Kampala", 45741007, 241038, "English and Swahili", "Ugandan Shilling")


# Using describe method inherited from AfricanCountry
print(kenya.describe())
print(uganda.describe())

# Using unique_feature method specific to Kenya
print(kenya.unique_feature())
print(uganda.unique_feature())