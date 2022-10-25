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
#outfile.write('Hello World')
# outfile.close()

# use the with statement instead of open() and close()
# with open(file_to_save, 'w') as txt_file:
#     #txt_file.write('Hello World')
#     txt_file.write('Counties in the  Election\n')
#     txt_file.write('---------------------\n')
#     txt_file.write('Arapahoe\nDenver\nJefferson')

# 1. Initialze a total vote counter

######### read file, creates empty list and uses not in to grab unique candidate names

    
# total_votes = 0
# candidate_options = []
# county_options = []

# with open(file_to_load) as election_data:
#      file_reader = csv.reader(election_data)
#      headers = next(file_reader)

#     for row in file_reader:
#         total_votes +=1
#         candidate_name = row[2]
#         county_name = row[1]
#         if candidate_name not in candidate_options:
#             candidate_options.append(candidate_name)
#         if county_name not in county_options:
#             county_options.append(county_name)
# print(candidate_options)
# print(county_options)

######### 

### print the entier file
    # for row in file_reader:
    #  print(row)

### prints the first 10 rows
    # i=0
    # for row in file_reader:
    #     print(row)
    #     i += 1
    #     if i >= 10:
    #         break



  ### skip and print header row
  #print(headers)
    
### for loop to print total voters
#     for row in file_reader:
#         #2 Add to the total vote count
#         total_votes +=1
# print(total_votes)  #369711


############ get distinct candidate names + vote counts
total_votes = 0
candidate_options = []
candidate_votes = {} #{'candidate_name1': votes, 'candidate_name2': votes, 'candidate_name3': votes}
# winning_candidate = ''
# winning_count = 0
# winning_percentage = 0


with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
    headers = next(file_reader)

    for row in file_reader:
        total_votes +=1  # same as total_votes = total_votes + 1
        candidate_name = row[2]
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)
            candidate_votes[candidate_name] = 0
        candidate_votes[candidate_name] +=1
print(total_votes)
print(candidate_options)
print(candidate_votes)



# with open(file_to_save, "w") as txt_file:
#         election_results = (
#             f"\nElection Results\n"
#             f"-------------------------\n"
#             f"Total Votes: {total_votes:,}\n"
#             f"-------------------------\n")
#         print(election_results, end="")
#     # Save the final vote count to the text file.
#         txt_file.write(election_results)

for candidate_name in candidate_votes:
    votes = candidate_votes[candidate_name]
    vote_percentage = float(votes) / float(total_votes) * 100
    candidate_results = (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})")
    print(candidate_results)
            #txt_file.write(candidate_results)

            # if (votes > winning_count) and (vote_percentage > winning_percentage):
            #     winning_count = votes
            #     winning_percentage = vote_percentage
            #     winning_candidate = candidate_name
            # print(f'{candidate_name}: received {vote_percentage:.1f}% ({votes:,})\n')
            

        # winning_candidate_summary = (
        #     f"-------------------------\n"
        #     f"Winner: {winning_candidate}\n"
        #     f"Winning Vote Count: {winning_count:,}\n"
        #     f"Winning Percentage: {winning_percentage:.1f}%\n"
        #     f"-------------------------\n")
        # print(winning_candidate_summary)
        # txt_file.write(winning_candidate_summary)






        
   















