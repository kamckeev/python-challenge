import os
import csv
csvpath = os.path.join('..', 'PyPoll', 'election_data2.csv')
with open(csvpath, newline= '') as csvfile:
    csvreader=csv.reader(csvfile, delimiter=',')
    
    csv_header = next(csvfile)
         
    candidates= []
    counties = []
    voter_ID= []
    for i in csvreader:
        candidates.append(i[2])
        counties.append(i[1])
        voter_ID.append(i[0])
    row_count = len(voter_ID)
    
    # A complete list of candidates who received votes
    candidate_list= (set(candidates))
    print(candidate_list)
    Khan= [i for i in candidates if i == 'Khan']
    Khan_votes=(len(Khan))
    print(f'Khan: {Khan_votes}')

    Li=[i for i in candidates if i == 'Li']
    Li_votes=(len(Li))
    print(f'Li: {Li_votes}')

    Correy=[i for i in candidates if i == 'Correy']
    Correy_votes=(len(Correy))
    print(f'Correy: {Correy_votes}')

    OTooley= [i for i in candidates if i == "O'Tooley"]
    OTooley_votes=(len(OTooley))
    print(f"O'Tooley: {OTooley_votes}")



   
           
   
   

    #printout:
    #print('{:*^50}'.format('Election Results'))
    #print()
    # number of votes
    #print('{:^30}'.format(f'The total number of votes cast was {row_count} votes!'))
    #print('{:^50}'.format('~'))

    # ***
    # The percentage of votes each candidate won
    # ***
    #The winner of the election based on popular vote
    # the winner: name
    # ***
    # some cool asci picture maybe? Related to voting
    # ***

