from  ..pet_option_classes import *

age_list = ['0-3 months', '3-6 months', '6-12 months']

dog_breed_list = ['Bulldog', 'German Shepherd']

cat_breed_list = ['Rex', 'Bengal']

#  Create a  list of FuelType for serializing
age = [PetAge(i) for i in age_list]

dog_breed = [DogBreed(i) for i in dog_breed_list]

cat_breed = [CatBreed(i) for i in cat_breed_list]
#  create a list of  tuple for the django dropdowns
age_dropdown = [(i, i) for i in age_list]

dog_breed_dropdown = [(i, i)  for i in dog_breed_list]

cat_breed_dropdown = [(i, i)  for i in cat_breed_list]




