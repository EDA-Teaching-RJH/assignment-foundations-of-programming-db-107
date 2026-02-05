#fleet_Manager.py

init_database():
#Returns 4 lists pre-populated with at least 5 Star Trek characters and their data.

display_menu():
#Queries users full name, Prints the options and current student logged in and returns the user's choice.

add_members(names, ranks, divs, ids):

#Validates ID is unique.
#Validates Rank is a valid TNG rank.
#Appends data to all 4 lists.

remove_member(names, ranks, divs, ids):

#Asks for an ID.
#Finds the index.
#Removes the entry from _all 4 lists_ to keep them in sync.

update_rank(names, ranks, ids):

#Finds a member by ID.
#Updates their rank string.

display_roster(names, ranks, divs, ids):
    
#Iterates through the lists using `range(len(names))`.
#Prints a formatted table of all crew.

search_crew(names, ranks, divs, ids):
    
#Asks for a search term.
#Prints any crew member whose name contains that term.

filter_by_division(names, divs):
    
#Asks user for "Command", "Operations", or "Sciences".
#Prints only members in that division using `match` or `if` .

count_officers(ranks)`:
    
#Counts how many "Captain" and "Commander" ranks exist and returns the integer.


main = fleet_manager()

    