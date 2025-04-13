class Kenya:
    location = "East Africa"    # Class variable shared by all instances

    def __init__(self, name="Kenya", capital="Nairobi", population=53771296, area=580367, language="Swahili and English", currency="Kenyan Shilling"):
        # Using the constructor to set instance attributes
        self.name = name
        self.capital = capital
        self.population = population
        self.area = area
        self.language = language
        self.currency = currency

    def describe(self):
        # A method to describe the country
        return f"Country Name: {self.name}, Capital: {self.capital}, Population: {self.population}, Area: {self.area} sq km, Languages: {self.language}, Currency: {self.currency}, Location: {Kenya.location}"


# Creating an instance of Kenya using default values
country = Kenya()

# Printing the description of the country
print(country.describe())