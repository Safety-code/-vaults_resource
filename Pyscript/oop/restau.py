class Restaurant:
    def __init__(self,restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type


    def describe_restaurant(self):
        print(f"The name of the restaurant is {self.restaurant_name} and have varieties of {self.cuisine_type}")

    def open_restaruant(self):
        """Describes when the restaurant opens"""
        print(f"The restaurant,br {self.restaurant_name} is open... ")

#first instance of the class retaurant 
restaurant = Restaurant("Pizzaman", "jollof rice")
print(f"{restaurant.restaurant_name}, sells chicken pizza")
print(f"{restaurant.cuisine_type} is the most popular meal sold by {restaurant.restaurant_name} ")

#Calling the methods
restaurant.describe_restaurant()
restaurant.open_restaruant()


#second instance
my_restaurant = Restaurant("God is Love", "local dishes")

my_restaurant.describe_restaurant()

#third instance
your_restaurant = Restaurant("\nSnapfingers", "pizza")

your_restaurant.describe_restaurant()