#fleet_Manager.py

#init_database():
#Returns 4 lists pre-populated with at least 5 Star Trek characters and their data.

n = ["Jean-Luc", "Spock", "Kathryn", "Montgonmery", "Worf"]
#captain =  ["Jean-Luc","Kathryn"]
#commander = ["Spock"]
#lcommander = ["Montgomery","Worf"]
r = ["Captain", "Commander", "Captain", "Lieutenant Commander", "Lieutenant Commander"]
d = ["Command", "Science", "Command", "Operations (Engineering)", "Operations (Security)"]
p = ["SP-937-215", "S-179-276", "NJ-573-219", "SE-197-54T", "KCD-445-31"]



#display_menu():
#Queries users full name, Prints the options and current student logged in and returns the user's choice.
#LIST OF OPTIONS

active = True


def fleet_manager():
    fname = input("Forname: ").capitalize()
    sname = input("Surname: ").capitalize()
    user = (fname + " " + sname) 
    print("\nBOOTING SYSTEM...")
    print("...")
    print("Welcome", user, "Select an option to continue")
    

    loading = 0
    while loading < 9:
        print("\nLoading module " + str(loading))
        break 
    
    
    while True:
        print("\n--- MENU ---")
        print("1. Display members")
        print("2. Add members")
        print("3. Remove members")
        print("4. Update ranks")
        print("5. Search members")
        print("6. Filter by Division")
        print("7. Count ranks")
        print("9. Exit")
        
        
        opt = input("Select Option: ")

        if opt == "1":
            print("Current Member List")

            for i in range(len(n)):
                print(n[i] + " - " + r[i] + " - " + d[i] + " - " + p[i])
#issue with "r[i]"


#add_members(names, ranks, divs, ids)

#Validates ID is unique.
#Validates Rank is a valid TNG rank.
#Appends data to all 4 lists.
        elif opt == "2":
            new_name = input("Enter Name: ")
            new_rank = input("Enter Rank: ")
            new_div = input("Enter Division: ")
            new_id = input("Enter ID in format ##-###-##(#)" "Enter ID: ")

            
            n.append(new_name)
            print("New Member Added.")

            r.append(new_rank)
            print("New Rank added.")

            d.append(new_div)
            print("New Division added.")
            
            p.append(new_id)
            print("New ID added.")

#calculate_payroll(ranks)`:
    
#    -   Iterates through the ranks list.
        
#    -   Assigns a credit value to ranks (e.g., Captain = 1000, Ensign = 200).
        
#    -   Returns the total cost of the crew.



#remove_member(names, ranks, divs, ids):

#Asks for an ID.
#Finds the index.
#Removes the entry from _all 4 lists_ to keep them in sync.
        elif opt == "3":
            remove = input("Enter Name to Remove ")

            idx = n.index(remove)
            n.pop(idx)
            idx = r.index(remove)
            r.pop(idx)
            idx = d.index(remove)
            d.pop(idx)
            idx = p.index(remove)
            p.pop(idx)
            
            print("Removed Member.")
            
#update_rank(names, ranks, ids):

#Finds a member by ID.
#Updates their rank string.
        #elif opt == "4":

#display_roster(names, ranks, divs, ids):
    
#Iterates through the lists using `range(len(names))`.
#Prints a formatted table of all crew.
        #elif opt == "5":

#search_crew(names, ranks, divs, ids):
    
#Asks for a search term.
#Prints any crew member whose name contains that term.
        #elif opt == "6":

#filter_by_division(names, divs):
    
#Asks user for "Command", "Operations", or "Sciences".
#Prints only members in that division using `match` or `if` .
        elif opt == "7":

            div = input("Input division: ").capitalize()  
            
            if div == "Command":
                print("Jean-Luc","\nKathryn")
            
            elif div == "Science":
                print("Spock")
            
            elif div == "Operations":
                print("Montgomery (Engineering)","\nWorf (Security)")
            
            else:
                print("Invalid","\nEnter a Valid Division")

#count_officers(ranks)`:
    
#Counts how many "Captain" and "Commander" ranks exist and returns the integer.
        elif opt == "8":
            count = 0
            for i in range(len(n)):
                if r[i] in ["Captain"]:
                    count += 1
            print("\nNumber of captains: " + str(count))
            for i in range(len(n)):
                if r[i] in ["Commander"]:
                    count += 1
            print("Number of Commanders: " + str(count))


        elif opt == "9":
            print("Shutting down.")
            break
            
        else:
            print("Invalid Option.")

fleet_manager()
    