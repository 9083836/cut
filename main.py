# class Car:
#     def __init__(self, model, year, manufacturer, engine_capacity, color, price):
#         self.model = model
#         self.year = year
#         self.manufacturer = manufacturer
#         self.engine_capacity = engine_capacity
#         self.color = color
#         self.price = price

#     def get_model(self):
#         return self.model

#     def get_year(self):
#         return self.year

#     def get_manufacturer(self):
#         return self.manufacturer

#     def get_engine_capacity(self):
#         return self.engine_capacity

#     def get_color(self):
#         return self.color

#     def get_price(self):
#         return self.price



#     def set_year(self, year):
#         self.year = year

#     def set_color(self, color):
#         self.color = color

#     def set_price(self, price):
#         self.price = price


#     def info(self):
#         info = (
#             f"Model: {self.model}\n"
#             f"Year: {self.year}\n"
#             f"Manufacturer: {self.manufacturer}\n"
#             f"Engine capacity: {self.engine_capacity}\n"
#             f"Color: {self.color}\n"
#             f"Price: {self.price} tenge\n"
#         )

#         return(info)



# toyota = Car('Supra', 2019, "Japan", 3.0, 'Violet', 33000000)
# print(toyota.info())

# # print("Модель:", toyota.get_model())
# # print("Год выпуска:", toyota.get_year())
# # print("Производитель:", toyota.get_manufacturer())
# # print("Объем двигателя:", toyota.get_engine_capacity())
# # print("Цвет:", toyota.get_color())
# # print("Цена:", toyota.get_price())

# # toyota.set_color("Black")
# # print(toyota.info())









# class Book:
#     def __init__(self, name, year, publisher, genre, autor, price):
#         self.name = name
#         self.year = year
#         self.publisher = publisher
#         self.genre = genre
#         self.autor = autor
#         self.price = price

#     def get_name(self):
#         return self.name

#     def get_year(self):
#         return self.year

#     def get_publisher(self):
#         return self.publisher

#     def get_genre(self):
#         return self.genre

#     def get_autor(self):
#         return self.autor

#     def get_price(self):
#         return self.price



#     def set_year(self, year):
#         self.year = year

#     def set_publisher(self, publisher):
#         self.publisher = publisher

#     def set_price(self, price):
#         self.price = price


#     def info(self):
#         info = (
#             f"Name: {self.name}\n"
#             f"Year: {self.year}\n"
#             f"Publisher: {self.publisher}\n"
#             f"Genre: {self.genre}\n"
#             f"Autor: {self.autor}\n"
#             f"Price: {self.price} tenge\n"
#         )

#         return(info)
    
# b = Book('Harry Potter', 1997, 'Bloomsbury, Scholastic', 'Fantasy', 'J.K. Rouling', 5000)
# print(b.info())
# print(f"Name: {b.get_name()}")
# b.set_price(10000)
# print(b.info())










class Stadion:
    def __init__(self, name, date, country, city, capacity):
        self.name = name
        self.date = date
        self.country = country
        self.city = city
        self.capacity = capacity

    def get_name(self):
        return self.name

    def get_date(self):
        return self.date

    def get_country(self):
        return self.country

    def get_city(self):
        return self.city

    def get_capacity(self):
        return self.capacity



    def set_date(self, date):
        self.date = date

    def set_capacity(self, capacity):
        self.capacity = capacity


    def info(self):
        info = (
            f"Название: {self.name}\n"
            f"Дата открытия: {self.date}\n"
            f"Страна: {self.country}\n"
            f"Город: {self.city}\n"
            f"Вместительность: {self.capacity} человек\n"
        )

        return(info)
    
s = Stadion('Сантьяго Бернабеу', "14 декабря 1947 год", 'Испания', 'Мадрид', 83186)
print(s.info())









class Class_1:
    def __init__(self, text):
        self.text = text

    def set_text(self, text):
        if text == None:
            self.text = ""
        else:
            self.text = text

class Class_2(Class_1):
    def __init__(self, text, number):
        super().__init__(text)
        self.number = number

    def set_number(self, number):
        self.number = number

    def get_number(self):
        return self.number


main = Class_1("Bear")
print(f"Text 1: {main.text}")

second = Class_2("Hello", 42)
print(f"Second text: {second.text}, number: {second.number}")

second.set_text("Updated text in SubClass")
second.set_number(99)
print(f"Second updated text: {second.text}, updated number: {second.number}")