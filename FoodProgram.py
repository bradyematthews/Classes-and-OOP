import FoodClass as fc


customerid = 570
name = 'Danni Sellyar'
address = '97 Mitchell Way Hewitt Texas 76712'
email = 'dsellyarft@gmpg.org'
phone = '254-555-9362'
member_status = False



"""
customerid = 569
name = 'Aubree Himsworth'
address = '1172 Moulton Hill Waco Texas 76710'
email = 'ahimsworthfs@list-manage.com'
phone = '254-555-2273'
member_status = True
"""

customer1 = fc.Customer(customerid, name, address, email, phone, member_status)

# this dictionary represents transactions. The key of the dictionary is the transaction identifier.
# The Value of the dictionary is a list. The elements in each list are -
# ['Date', 'Name of item', 'Cost', 'customerid' ]

dict = {'trans1':['2/15/2023','The Lone Patty',17,569],
                'trans2':['2/15/2023','The Octobreakfast',18,569],
                'trans3':['2/15/2023','The Octoveg',16,570],
                'trans4':['2/15/2023','The Octoburger',20,570],
}

order_total = 0



print("Customer Name:", customer1.get_name())
print("Phone:", customer1.get_phone())

# ID Match
for i in dict:

    if dict[i][3] == customer1.get_customerid():
        transaction1 = fc.Transaction(dict[i][0],dict[i][1],dict[i][2],dict[i][3])
        order_total += transaction1.get_cost()
        print("Order Item:", transaction1.get_item_name(),  " Price: $", format(float(transaction1.get_cost()), '.2f'))

print("Total Cost: $", format(float(order_total), '.2f'))

# Member Status
if customer1.get_member_status() == True:
   discount = .2 * order_total
   discounted_total = order_total - discount
   print("Member Discount: $", format(float(discount), '.2f'))
   print("Total cost after Discount: $", format(float(discounted_total), '.2f'))
else:
    print()






