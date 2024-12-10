# Matthew Chaparro-Roldan
# Program 9: Game of the Year
# COP 2500
# November 15, 2024


def gather_names(votes):
    # Print out the directions/welcome
    print("Enter everyone's favorite games.\n")
    print("Type 'done' when finished.\n")

    # ask for the first vote
    vote_input = input()

    # while the input is not done than do....
    while vote_input != "done":
        # add the input/vote to the list
        votes.append(vote_input)
        # ask for another vote input
        vote_input = input()
    
def clean_votes(votes):
    # find the length of the votes
    # use a loop to loop through all votes
         for index in range(len(votes)):
             
        # call title on each item in the list and give it back
            votes[index] = votes[index].title()
def find_goty(votes):
    # we need 2 variables: store the goty name, and how many votes.
    game_of_year = ""
    # it doesnt matter what the name starts at, but the votes need to start at 0
    vote_count = 0

    # find the length of votes
    # loop over all the values in the list.
    for index in range(len(votes)):
        if (votes.count(votes[index]) > vote_count):
            # the highest votes becomes votes.count(votes[index])
            vote_count = votes.count(votes[index])
            # goty name becomes  votes[index]
            game_of_year = votes[index]
    # print out message telling us what the name of the goty
    print("The best game is", game_of_year)
def print_list(votes):
    # sort votes
    votes.sort()
    # print the first value in the list <---- index is 0
    # find the length of the list
    for index in range(len(votes)):
    # loop over all the values in the list, starting at 1
        if votes[index] != votes[index-1]:
            print( votes[index])
            

def main():
    # create an empty list to store the votes
    votes = []
    # gather the name of the games
    gather_names(votes)
    # clean that data
    clean_votes(votes)
    # you want to print the game with the most votes
    find_goty(votes)
    # print out a sorted list of the items
    print_list(votes)

 

main()
