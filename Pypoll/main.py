import os

import csv


pypoll_csv = os.path.join('Resources', 'election_data.csv')


voter_id = []
county = []
candidate = []
khanvotes = []
correyvotes = []
livotes = []
otooleyvotes = []

total = 0


with open(pypoll_csv, newline="") as csvfile:
   
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)

    for row in csvreader:
        
        voter_id.append(row[0])
        county.append(row[1])
        candidate.append(row[2])
        total = (candidate)


    for x in total:
           
        if x == "Khan":
            khanvotes.append(candidate)
           
        elif x == "Correy":
            correyvotes.append(candidate)
            
        elif x == "Li":
            livotes.append(candidate)
            
        elif x == "O'Tooley":
             otooleyvotes.append(candidate)



khanpercent = round((len(khanvotes) /len(total)) * 100, 4)

correypercent = round((len(correyvotes) / len(total)) * 100, 4)

lipercent = round((len(livotes) / len(total)) * 100, 4)

otooleypercent = round((len(otooleyvotes) / len(total)) * 100, 4)

y = set(total)

Winner = max(set(total),key=total.count)

print('Election Results')
print('----------------------------')
print(f'Total Votes: {len(voter_id)}')
print('----------------------------')
print(f"Khan: {khanpercent}%  ({(len(khanvotes))})")
print(f"Correy: {correypercent}%  ({(len(correyvotes))})")
print(f"Li: {lipercent}%  ({(len(livotes))})")
print(f"O'Tooley: {otooleypercent}%  ({(len(otooleyvotes))})")
print('----------------------------')
print(f'Winner: {(Winner)}')
print('----------------------------')

Output_file = os.path.join('Resources', 'Output_folder', 'output.txt')

with open(Output_file, 'w') as txt_file:
    txt_file.write("Election Results\n")
    txt_file.write("----------------------------\n")
    txt_file.write(f"Total Votes: {len(voter_id)}\n")
    txt_file.write("----------------------------\n")
    txt_file.write(f"Khan: {khanpercent}%  ({(len(khanvotes))})\n")
    txt_file.write(f"Correy: {correypercent}%  ({(len(correyvotes))})\n")
    txt_file.write(f"Li: {lipercent}%  ({(len(livotes))})\n")
    txt_file.write(f"O'Tooley: {otooleypercent}%  ({(len(otooleyvotes))})\n")
    txt_file.write("----------------------------\n")
    txt_file.write(f"Winner: {(Winner)}\n")
    txt_file.write("----------------------------\n")