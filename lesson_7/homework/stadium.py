class Stadium:
    def __init__(self, name, date, country, city, location):
        self.__name = name
        self.__date = date
        self.__country = country
        self.__city = city
        self.__location = location

    def show_info(self):
        print(f"{self.__name} was created in {self.__date} in the city of {self.__city}, "
              f"{self.__country} is located on {self.__location} ")

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self,name):
        self.__name = name

    @property
    def date(self):
        return self.__date

    @date.setter
    def date(self, date):
        self.__date = date

    @property
    def country(self):
        return self.__country

    @country.setter
    def country(self, country):
        self.__country = country

    @property
    def city(self):
        return self.__city

    @city.setter
    def city(self, city):
        self.__city = city

    @property
    def location(self):
        return self.__location

    @location.setter
    def location(self, location):
        self.__location = location

nsc = Stadium (
    name="Olimpiyskiy National Sports Complex",
    date=1923,
    country="Ukraine",
    city="Kyiv",
    location="Velyka Vasylkivska str. 55"
)

narendra = Stadium (
    name="Narendra Modi Stadium(Sardar Vallabhbhai Patel Stadium or Motera Cricket Stadium)",
    date=1983,
    country=" India",
    city="Ahmedabad",
    location="	Motera, Ahmedabad, Gujarat"
)

nsc.show_info()
narendra.show_info()