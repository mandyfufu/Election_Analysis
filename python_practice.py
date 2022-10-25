# print("Hello World")
# actor ={'name':'Tom Cruise'}
# print(f'{actor["name"]}')

# counties = ['Arapahoe', 'Denver', 'Jefferson']
# if counties[1] == 'Denver':
#     print(counties[1])

# if counties[3] != 'Jefferson':
#     print(counties[2])

# my_votes = int(input('How many votes did you get in the election?'))
# total_votes = int(input("What is the total votes in the election?"))
# percentage_votes = (my_votes /total_votes)*100
# #print('I received ' + str(percentage_votes)+'% of the votes.')
# print(f'I received {percentage_votes}% of the total votes.')

# #nested if-else statement
# score =int(input('What is your test score?' ))
# if score >= 90:
#     print('Your grade is an A.')
# else:
#     if score >= 80:
#         print('Your grade is a B.')
#     else:
#             if score >= 70:
#                 print('Your grade is a C.')
#             else:
#                 if score >= 60:
#                     print('Your grade is a D.')
#                 else:
#                     print('Your grade is an F.')


# # if-elif-statements
# score = int(input('What is your test score?'))
# if score >= 90:
#     print('Your grade is an A.')
# elif score >= 80:
#     print('Your grade is a B.')
# elif score >= 70:
#     print('Your grade is a C.')
# elif score >= 60:
#     print('Your grade is a C.')
# else:
#     print('Your grade is an F.')

# # membership / logical operators
# counties = ['Arapahoe', 'Denver', 'Jefferson']
# if 'El Paso' in  counties:
#     print('El Paso is in the list of counties.')
# else:
#     print('El Paso is not in th elist of counties.')
# if 'Arapahoe' in counties and 'El Paso' in counties:
#     print('Arapahoe and El Paso are in the list of counties.')
# else:
#     print('Arapahoe or El Paso is not in the list of counites.')

########################## Loops

# x=0
# while x <= 5:
#     print(x)
#     x = x+1

# count = 7
# while count < 1:
#     print('Hello World')
    
# counties = ['Arapahoe', 'Denver', 'Jefferson']
# for x in counties: 
#     print(x)

# numbers = [0,1,2,3,4]
# for num in numbers:
#     print(num)

# range fx, will perform same as above
# for x in range(5):
#     print(x)

# counties = ['Arapahoe', 'Denver', 'Jefferson']
# for i in range(len(counties)):
#     print(counties[i])

# #iterate through a tuple
# counties_tuple = ('Arapahoe','Denver','Jefferson')
# for county in counties_tuple:
#     print(county)

##### iterate through a dictionary
# counties_dict = {'Arapahoe':422829, 'Denver':463353, 'Jefferson': 432438}
# for county in counties_dict:
#     print(county)

# for county in counties_dict:
#     print(counties_dict[county])

# for county in counties_dict:
#     print(counties_dict.get(county))

#counties_dict = {'Arapahoe':422829, 'Denver':463353, 'Jefferson': 432438}


#### print dictionary list

# voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
#                 {"county":"Denver", "registered_voters": 463353},
#                 {"county":"Jefferson", "registered_voters": 432438}]

# for county_dict in voting_data:
#     print(county_dict.items())

# for county_dict in voting_data:
#     print(county_dict['registered_voters'])

# for county_dict in voting_data:
#     for value in county_dict.values():
#         print(value)

# for county_dict in voting_data:
#     print(county_dict['county'])

##### f strings

# my_votes = int(input('How many votes did you get in the election?'))
# total_votes = int(input('What is the total votes in the election?'))
# percentage_votes = (my_votes / total_votes)*100
# print(f'I received {percentage_votes}% of the total votes.')

# counties_dict = {'Anapahoe':369237, 'Denver':413229, 'Jefferson':390222}
# for county, voters in counties_dict.items():
#     print(f'{county} county has {voters} registered voters.')

# candidate_votes = int(input('How many votes did the candidate get in the election?'))
# total_votes = int(input('What is the total number of votes in the election?'))
# message_to_candidate = (
#     f'You received {candidate_votes:,} number of votes.'
#     f'The total number of votes in the election was {total_votes:,}.'
#     f'You received {candidate_votes / total_votes * 100:.2f}s% of the total votes.'
# )
# print(message_to_candidate)

# counties_dict = {'Arapahoe':422829, 'Denver':463353, 'Jefferson': 432438}
# for keys, values in counties_dict.items():
#     print(f'{keys} county has {values:,} registered voters.')

# voting_data = [{"county":"Arapahoe", "registered_voters": 422829}, {"county":"Denver", "registered_voters": 463353}, {"county":"Jefferson", "registered_voters": 432438}]
# for county_dict in voting_data:
#     for value in county_dict.values():
#         print(f"({county_dict['county']} county has {county_dict['registered_voters']:,} registered voters.")


# ###### dir() inbuilt fx that returns list of attributes and methods of any object
# counties_dict = {'Arapahoe':422829, 'Denver':463353, 'Jefferson': 432438}
# dir(counties_dict)



######################################### Challenge 

import csv
import os

# Add a variable to load a file from a path.
file_to_load = os.path.join("election_results.csv")
# Add a variable to save the file to a path.
file_to_save = os.path.join("election_analysis.txt")

# Initialize a total vote counter.
total_votes = 0
candidate_options = []
candidate_votes = {} #{'candidate_name1': votes, 'candidate_name2': votes, 'candidate_name3': votes}


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


for candidate_name, votes in candidate_votes.items():
    #votes = candidate_votes[candidate_name]
    vote_percentage = float(votes) / float(total_votes) * 100
    candidate_results = (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})")
    print(candidate_results) 


