import csv

file = r"C:\Users\kekoj\Data Analytics Class\Module Challenges\Challenge 3\PyPoll\Resources\election_data.csv"
output_file_path = "election_results.txt"  # Specify the path for the output text file

ballot_id_col = "Ballot ID"
candidates_col = "Candidate"

candidate_votes = {}

total_votes = 0

with open(file, 'r') as csvfile:
    csv_reader = csv.reader(csvfile)

    header = next(csv_reader, None)

    for row in csv_reader:
        ballot_id = row[header.index(ballot_id_col)]
        candidate_name = row[header.index(candidates_col)]

        if ballot_id:
            total_votes += 1

            if candidate_name:
                if candidate_name in candidate_votes:
                    candidate_votes[candidate_name] += 1
                else:
                    candidate_votes[candidate_name] = 1

winner = ""
winner_votes = 0

# Open a new output file for writing
with open(output_file_path, 'w') as output_file:
    output_file.write("Election Results\n")
    output_file.write("-------------------------\n")
    output_file.write(f"Total Votes: {total_votes}\n")
    output_file.write("-------------------------\n")

    for candidate, votes in candidate_votes.items():
        percentage = (votes / total_votes) * 100
        output_file.write(f"{candidate}: {percentage:.3f}% ({votes})\n")

        if votes > winner_votes:
            winner = candidate
            winner_votes = votes

    output_file.write("-------------------------\n")
    output_file.write(f"Winner: {winner}\n")
    output_file.write("-------------------------\n")