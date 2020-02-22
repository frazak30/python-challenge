# Import modules
import os
import csv

# declare variables 
votes = 0
Khan_votes = 0
Correy_votes = 0
Li_votes = 0
OTooley_votes = 0
Khan_pct = 0
Correy_pct = 0
Li_pct = 0
OTooley_pct = 0
result_total = []
results_sorted = []
winner = "" 

# declare list for candidates 
candidates = []

# declare path to csv
csvpath = os.path.join("dataset","election_data.csv")

#print(csvpath)

with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

   # skip header
    next(csvreader)
   
    # Read each row of data after the header
    for row in csvreader: 

      # get votes for each candidate
      if row[2] == "Khan" : 
        Khan_votes += 1
      elif row[2] == "O'Tooley" :
        OTooley_votes += 1
      elif row[2] == "Correy" :
        Correy_votes += 1
      elif row[2]  == "Li" :
        Li_votes += 1

      candidates.append(row)

# get overall number of votes
votes = len(candidates) 

# get percentages for each candidates
Khan_pct = format((Khan_votes / votes) * 100, ".3f")
Correy_pct = format((Correy_votes / votes) * 100, ".3f")
Li_pct = format((Li_votes / votes) * 100, ".3f")
OTooley_pct = format((OTooley_votes / votes) * 100, ".3f")
result_total = sorted([OTooley_votes, Khan_votes, Li_votes, Correy_votes], reverse=True)
results_sorted.append(result_total.sort)

def candidatePosition(i):
  result_string = ""
  if OTooley_votes == result_total[i]:
    return f"OTooley: {OTooley_pct}% ({OTooley_votes})"
  elif  Correy_votes == result_total[i]:
    return f"Correy: {Correy_pct}% ({Correy_votes})"
  elif Khan_votes == result_total[i]:
    return f"Khan: {Khan_pct}% ({Khan_votes})"
  elif  Li_votes == result_total[i]:
    return f"Li: {Li_pct}% ({Li_votes})" 


def winner(): 
  if OTooley_votes == result_total[0]:
    return "OTooley"
  elif  Correy_votes == result_total[0]:
    return "Correy"
  elif Khan_votes == result_total[0]:
    return "Khan"
  elif  Li_votes == result_total[0]:
    return "Li" 


# print formatted results
print("Election Results")
print("--" * 20)
print(f"Total Votes: {votes}")
print("--" * 20)
print(candidatePosition(0))
print(candidatePosition(1))
print(candidatePosition(2))
print(candidatePosition(3))
print("--" * 20)
print(f"Winner: {winner()} ")
print("--" * 20)


# # open a new text file with "write" mode.
file = open("election_results.txt", "w")

# # write the results to the text file
file.write("Election Results\n")
file.write("--" * 20)
file.write(f"\nTotal Votes: {votes}\n") 
file.write("--" * 20)
file.write(f"\n{candidatePosition(0)}")
file.write(f"\n{candidatePosition(1)}")
file.write(f"\n{candidatePosition(2)}")
file.write(f"\n{candidatePosition(3)}\n")
file.write("--" * 20)
file.write(f"\nWinner: {winner()}\n")
file.write("--" * 20)

# make sure the file is closed
file.close()

