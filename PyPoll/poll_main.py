import os
import csv
csvpath = os.path.join('..', 'PyPoll', 'election_data2.csv')
with open(csvpath, newline= '') as csvfile:
    csvreader=csv.reader(csvfile, delimiter=',')
    
   
     # number of votes
    csv_header = next(csvfile)
    
    # A complete list of candidates who received votes
    # A complete list of candidates who received votes
    
    candidates= []
    counties = []
    voter_ID= []
    for i in csvreader:
        candidates.append(i[2])
        counties.append(i[1])
        voter_ID.append(i[0])
    row_count = len(voter_ID)
    candidate_list= (set(candidates))
   
    
    # A complete list of candidates who received votes
    


    
           
   
   

    #printout:
    # Election Results
    # *** 
    #print ('Total number of votes cast:')
    
    #print(f'The total amount of votes cast this election was {row_count} votes!')
    # ***
    # Corey, Khan, Li, O'Tuley canidates, list them in order of percentages of votes received
    # ***
    #print('Our candidates!:')
   # print(list(candidate_list))
    # the winner: name
    # ***
    # some cool asci picture maybe? Related to voting
    # ***

