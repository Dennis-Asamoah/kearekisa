import imp
from ..property_option_classes import *

property_type_list = ['Residential','Commercial', 'Industrial', 'Raw Land', 'Other']

seller_type_list = ['Owner', 'Seller', 'Other']

#  transmission_list = ['Maneul','Automatic','Other']

broker_fee_list = ['Yes', 'No']

furnishing_list = ['Furnished', 'UnFurnished']

#  Create a  list of FuelType for serializing
property_type = [PropertyType(i) for i in property_type_list]

seller_type = [SellerType(i) for i in seller_type_list]

broker_fee = [BrokerFee(i) for i in broker_fee_list]

Furnishing = [Furnishing(i) for i in furnishing_list]

#  create a list of  tuple for the django dropdowns
property_type_dropdown = [(i, i) for i in property_type_list]

seller_type_dropdown = [(i, i)  for i in seller_type_list]

broker_fee_dropdown = [(i, i)  for i in broker_fee_list]

furnishing_dropdown = [(i, i)  for i in furnishing_list]
