from ..vehicle_options_classes import *


fuel_type_list = ['Diesel','CNG', 'Other', 'Electric', 'Other']

body_type_list = ['Sedan','Hatchback', 'SUV', 'Bakkie', 'Sports', 'Other']

transmission_list = ['Manual','Automatic','Other']

#  owner_list = ['Diesel','CNG', 'Other', 'Electric', 'Other']

mileage_list = ['0-15000', '15001-30000', '30001-45000']

condition_list = ['New', 'Used']

fuel_type_list = ['Diesel','CNG', 'Other', 'Electric', 'Other']

number_of_owners_list = ['Zero', 'firstOwner','2+ Owners']

fuel_type_list = ['Diesel','CNG', 'Other', 'Electric', 'Other']

vehicle_colour_list = ['White', 'Grey', 'Black', 'Silver', 'Red', 'Blue']

make_list = ['Toyata', 'Honda', 'VW', 'Ford', 'Hyundai']

model_list = ['Camry', 'Other']

#  Create a  list of FuelType for serializing
fuel_type = [FuelType(i) for i in fuel_type_list]

body_type = [BodyType(i) for i in body_type_list]

transmission = [Transmission(i) for i in transmission_list]

condition = [VehicleCondition(i) for i in condition_list]

fuel_type = [NumberOfOwners(i) for i in fuel_type_list]

vehicle_color = [VehicleColour(i) for i in vehicle_colour_list]

#  create a list of  tuple for the django dropdowns
fuel_type_dropdown = [(i, i) for i in fuel_type_list]

body_type_dropdown = [(i, i)  for i in body_type_list]

transmission_dropdown = [(i, i)  for i in transmission_list]

condition_dropdown = [(i, i)  for i in condition_list]

fuel_type_dropdown = [(i, i)  for i in fuel_type_list]

vehicle_colour_dropdown = [(i, i)  for i in vehicle_colour_list]