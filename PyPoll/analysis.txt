import os   #allows code to interact with operating systems
import csv  #states the code will be using a csv file
election_csv = os.path.join("resources","election_data.csv")    #defining variable as path to data source

with open(election_csv, 'r') as csv_file:   #making the data source a readable csv file
    election_original = csv.reader(csv_file)    #defining variable as readable file

    header = next(election_original)    #creating a header to store header row as next row
    total_votes = 0     #initialise total_votes variable as 0
    cand_a = None       #initialising variables for the 3 candidates
    cand_b = None
    cand_c = None
    cand_a_votes = 0    #initialising variables to count each candidates votes
    cand_b_votes = 0
    cand_c_votes = 0
    lead = 0            #initialise TRACKING variable to store the highest vote count
    winner = None       #initialise TRACKING variable to store the winner, based off vote count
    

    #create for loop to create values for total_votes, as well as label each column (though not all of which will be used)

    for row in election_original:   
        total_votes += 1
        voter_id = row[0]
        county = row[1]
        candidates =row[2]

        #utilise if function within for loop to identify the 3 unique candidates

        if cand_a is None:  
            cand_a = candidates
        elif candidates != cand_a and cand_b is None:
            cand_b = candidates
        elif candidates != cand_a and candidates != cand_b:
            cand_c = candidates

        #utilise if function within for loop to count each vote for candidates

        if candidates == cand_a:    
            cand_a_votes += 1
        elif candidates == cand_b:
            cand_b_votes += 1
        elif candidates == cand_c:
            cand_c_votes += 1

        #utilise if functions within for loop to determine the highest vote count

        if cand_a_votes > cand_b_votes:
            lead = cand_a_votes
        else:
            lead = cand_b_votes
        if cand_c_votes > lead:
            lead = cand_c_votes
        
        #utilise if function within for loop to determine the winning candidate based off their corresponding vote count

        if lead == cand_a_votes:
            winner = cand_a
        elif lead == cand_b_votes:
            winner = cand_b
        elif lead == cand_c_votes:
            winner = cand_c
        
    #create percentage value for each candidates votes & round down to 2 decimal places for appropriate display of data

    cand_a_percent = cand_a_votes/total_votes*100
    cand_b_percent = cand_b_votes/total_votes*100
    cand_c_percent = cand_c_votes/total_votes*100
    cand_a_percent = round(cand_a_percent,2)
    cand_b_percent = round(cand_b_percent,2)
    cand_c_percent = round(cand_c_percent,2)
   
    #final display template

    print("Election Results")
    print("")
    print("------------------")
    print("Total Votes:",total_votes)
    print("")
    print("------------------")
    print("")
    print(f"{cand_a} {cand_a_percent}% ({cand_a_votes})")
    print(f"{cand_b} {cand_b_percent}% ({cand_b_votes})")
    print(f"{cand_c} {cand_c_percent}% ({cand_c_votes})")
    print("")
    print("------------------")
    print("")
    print("Winner:", winner)
    print("")
    print("------------------")