from __future__ import print_function
import happybase

connection = happybase.Connection('azure-cluster.newprolab.com')
print("connected")

table_name = 'sergey.chekanskiy'
families = {'data': {'max_versions': 4096}}

connection.create_table(table_name, families)

print("table {0} created".format(table_name))
