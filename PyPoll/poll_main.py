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
    #print(candidate_list)
    Khan= [i for i in candidates if i == 'Khan']
    Khan_votes=(len(Khan))
    Khan_percent= round((Khan_votes/row_count)*100)
    #print(f'Khan: {Khan_votes}')

    Li=[i for i in candidates if i == 'Li']
    Li_votes=(len(Li))
    Li_percent= round((Li_votes/row_count)*100)
    #print(f'Li: {Li_votes}')

    Correy=[i for i in candidates if i == 'Correy']
    Correy_votes=(len(Correy))
    Correy_percent =round((Correy_votes/row_count)*100)
    #print(f'Correy: {Correy_votes}')

    OTooley= [i for i in candidates if i == "O'Tooley"]
    OTooley_votes=(len(OTooley))
    OTooley_percent = round((OTooley_votes/row_count)*100)
    #print(f"O'Tooley: {OTooley_votes}")

    #dict(["OTooley": OTooley_votes]), {Correy: Correy_votes}, {Li: Li_votes}, {Khan: Khan_votes})

   
           
   
   

    #printout:
    print('{:*^50}'.format('Election Results'))
    print('{:^30}'.format(f'The total number of votes cast was {row_count} votes!'))
    print('{:^50}'.format('~'))
# The percentage of votes each candidate won
    print(f'Khan had {Khan_percent}% of the vote, ({Khan_votes} votes)')
    print(f'Li had {Li_percent}% of the vote, ({Li_votes} votes)')
    print(f'Correy had {Correy_percent}% of the vote, with ({Correy_votes} votes)')
    print(f"O'Tulley had {OTooley_percent}% of the vote, with ({Khan_votes} votes)")
    print('{:^50}'.format('~'))
   #The winner of the election based on popular vote
    # the winner: name
    print(f'The winner was: (function needed to search for greatest numbrr of votes')
    print('{:*^50}'.format(''))

    

    

