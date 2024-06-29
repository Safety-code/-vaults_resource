class User:
    """Describes a user profile"""
    def __init__(self, first_name, last_name, birth_date):
        self.first_name = first_name
        self.last_name = last_name
        self.birth_date = birth_date

    def describe_user(self):
        print(f"The user's name is {self.first_name} {self.last_name}")
        print(f"The user was born on {self.birth_date}")

    
    def greet_user(self):
        print(f"Hello, {self.first_name} {self.last_name}")


#first user instance

first_user = User("Joseph", "Mensah", "23rd June, 1999")
print(f"The user {first_user.first_name} {first_user.last_name} was born on {first_user.birth_date}")