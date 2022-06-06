from ..job_options_classes import *


contract_type_list = ['Permanent', 'Training', 'Volunteer', 'Training', 'Other']

working_hours_list = ['Full_time', 'Part_time']

#  Create a  list of FuelType for serializing
contract_type = [ContractType(i) for i in contract_type_list]

working_hours = [WorkingHours(i) for i in working_hours_list]

#  create a list of  tuple for the django dropdowns
contract_type_dropdown = [(i, i) for i in contract_type_list]

working_hours_dropdown = [(i, i)  for i in working_hours_list]


