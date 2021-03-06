import os
import csv
candidate_raws ={}
candidates= []
csvpath = os.path.join('..', 'PyPoll', 'election_data2.csv')
with open(csvpath, newline= '') as csvfile:
    csvreader=csv.reader(csvfile, delimiter=',')
    
    csv_header = next(csvfile)
         
    for i in csvreader:
        candidates.append(i[2])
        if i[2] not in candidate_raws:
            candidate_raws[i[2]]=1
        else:
            candidate_raws[i[2]] = candidate_raws[i[2]]+1
    row_count = len(candidates)

candidate_names =list(candidate_raws)
candidate_votes= list(candidate_raws.values())

candidate_fraction= []
for i in candidate_votes:
    candidate_fraction.append((round((i/row_count)*100)))


candidate_percentage = dict(zip(candidate_names, candidate_fraction))

winner_value= max(candidate_votes)

winner_name = 'n/a'
for name, votes in candidate_raws.items(): 
    if votes == winner_value:
        winner_name= name 

#print to txt file
output_path= os.path.join('..','PyPoll', 'Poll_txt.txt')
with open(output_path, "w") as textfile:
    print('{:*^50}'.format('Election Results'), file=textfile)
    print(f'The total number of votes cast was {row_count} votes!',file=textfile )
    print('{:^50}'.format('~'), file=textfile)

    for name in candidate_names:
        print(f'Candidate {name} had {candidate_percentage[name]}% of the vote, ({candidate_raws[name]})', file=textfile)

    print('{:^50}'.format('~'),file=textfile)

    print(f'The winner was: {winner_name}',file=textfile)
    print('{:*^50}'.format(''),file=textfile)

#print to terminal
print('{:*^50}'.format('Election Results'))
print('{:^30}'.format(f'The total number of votes cast was {row_count} votes!'))
print('{:^50}'.format('~'))
for name in candidate_names:
    print(f'Candidate {name} had {candidate_percentage[name]}% of the vote, ({candidate_raws[name]})')

print('{:^50}'.format('~'))

print(f'The winner was: {winner_name}')
print('{:*^50}'.format(''))