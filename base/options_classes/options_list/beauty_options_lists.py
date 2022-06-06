from ..beauty_options_classes import *


hair_list = ['Hair Colouring', 'Relaxers', 'Hair Treatment']

#  body_type_list = ['Sedan','Hatchback', 'SUV', 'Bakkie', 'Sports', 'Other']

gender_list = ['Men', 'Woman', 'Unisex']

age_group_list = ['Adult', 'Children', 'Baby']

skin_type_list = ['Normal', 'Dry', 'Oily', 'Sensitive', 'All']

shoe_size_list = [str(i/2) for i in range(4, 31)] + ['Other']

#  START
number_list = [str(i*2) for i in range(2, 19)]

ss =['(XS)', '(S)', '(S)', '(S/M)', '(XS)', '(M)', '(M)', '(L/M)', '(L)', '(L)', '(XL)', '(XL)', '(XL)'
'(2XL)', '(2XL)', '(3XL)', '(3XL)', '(4XL)',
]

dress_sizes_list = [str(i)+x for i,x in zip(number_list, ss)] +['N/A', 'Other']
#  END     

general_sizes_list = ['XS', 'S', 'M', 'L', 'XL', 'XXL', 'XXXL', 'XXXXL', 'N/A', 'Other'] 

#  Create a  list of FuelType for serializing
hair = [Hair(i) for i in hair_list]

gender = [Gender(i) for i in gender_list]

age_group = [AgeGroup(i) for i in age_group_list]

skin_type = [SkinType(i) for i in skin_type_list]

shoe_sizes = [ShoeSize(i) for i in shoe_size_list]

dress_sizes = [DressSize(i) for i in dress_sizes_list]

general_sizes = [GeneralSize(i) for i in general_sizes_list]

#  create a list of  tuple for the django dropdowns
hair_dropdown = [(i, i) for i in hair_list]

gender_dropdown = [(i, i)  for i in gender_list]

age_group_dropdown = [(i, i)  for i in age_group_list]

skin_type_dropdown = [(i, i)  for i in skin_type_list]

shoe_sizes_dropdown = [(i, i) for i in shoe_size_list]

dress_sizes_dropdown = [(i, i)  for i in dress_sizes_list]

general_dropdown = [(i, i)  for i in general_sizes_list]
