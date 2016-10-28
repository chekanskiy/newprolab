from __future__ import print_function
import happybase

connection = happybase.Connection('azure-cluster.newprolab.com')
print("connected")

my_name = 's.chekanskiy'

table = connection.table(my_name)


# Put one item in the Table
# table.put('111', {'data:links': 'test_data'})

# Delete table
# connection.delete_table(my_name, disable=True)

# Print all tables
#print(connection.tables())

# Get row by key
# print(table.row('1179018957'))
