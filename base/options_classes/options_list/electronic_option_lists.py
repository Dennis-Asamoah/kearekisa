from ..electronic_options_classes import *

brand_list = ['Apple','Huawei', 'Samsung', 'Huawei', 'Oppo', 'Philips', 'Cannon']

condition_list = ['New', 'Used']

#  Create a  list of FuelType for serializing
brand = [Brand(i) for i in brand_list]

Condition = [Condition(i) for i in condition_list]

#  create a list of  tuple for the django dropdowns
brand_dropdown = [(i, i) for i in brand_list]

condition_dropdown = [(i, i)  for i in condition_list]


