#Import the datetime class form the datetime module

# import datetime
# #use the now() attribute on the datetime class to get the  present time.
# now = datetime.datetime.now()
# #print the present time
# print(f'The time right now is {now}')

# import datetime as dt
# now = dt.datetime.now()
# print('The time right now is ', now)

import csv
import os
#assign a file to a variable
file_to_load = os.path.join('election_results.csv')
# with open(file_to_load) as election_data:
#     print(election_data)

#create a file to write to
file_to_save = os.path.join('election_analysis.txt')
# open(file_to_save, 'w')

# outfile = open(file_to_save, 'w')
# outfile.write('Hello World')
# outfile.close()

# use the with statement instead of open() and close()
# with open(file_to_save, 'w') as txt_file:
#     #txt_file.write('Hello World')
#     txt_file.write('Counties in the  Election\n')
#     txt_file.write('---------------------\n')
#     txt_file.write('Arapahoe\nDenver\nJefferson')

######### read file 
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
    # for row in file_reader:
    #     print(row[0])

  ### skip and print header row
    headers = next(file_reader)
    print(headers)



