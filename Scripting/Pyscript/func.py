#PETS - POSTIONAL ARGUMENTS
def describe_pets(pet_name, animal_type='dog'):
    """Display information about your pet"""
    print(f"\nI have {animal_type}")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

my_pet = describe_pets('harry', 'hamster')
my_pet = describe_pets(pet_name='harry', animal_type='hamster') # default value argument
my_pet = describe_pets(animal_type='hamster', pet_name='harry') # keyword argument
my_pet = describe_pets('willie') # default value argument
my_pet = describe_pets(pet_name='willie') # default value argument
my_pet = describe_pets()

print(my_pet)

