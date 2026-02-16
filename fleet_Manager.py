#fleet_Manager.py

#init_database():
#Returns 4 lists pre-populated with at least 5 Star Trek characters and their data.

n = ["Jean-Luc", "Spock", "Kathryn", "Montgonmery", "Worf"]
#captain =  ["Jean-Luc","Kathryn"]
#commander = ["Spock"]
#lcommander = ["Montgomery","Worf"]
r = ["Captain", "Commander", "Captain", "Lieutenant Commander", "Lieutenant Commander"]
d = ["Command", "Science", "Command", "Engineering", "Security"]
id = ["SP-937-215", "S-179-276", "NJ-573-219", "SE-197-54T", "KCD-445-31"]



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
        print("5. Payrole")
        print("6. Search Members")
        print("7. Filter by Division")
        print("8. Count ranks")
        print("9. Exit")
        

#display_roster(names, ranks, divs, ids):
    
#Iterates through the lists using `range(len(names))`.
#Prints a formatted table of all crew.
        opt = input("Select Option: ")

        if opt == "1":
            print("Current Member List")

            for i in range(len(n)):
                print(n[i] + " - " + r[i] + " - " + d[i] + " - " + id[i])


#add_members(names, ranks, divs, ids)

#Validates ID is unique.
#Validates Rank is a valid TNG rank.
#Appends data to all 4 lists.
        elif opt == "2":
            new_name = input("Enter Name: ").capitalize()
            new_rank = input("Enter Rank: ").capitalize()
            new_div = input("Enter Division: ").capitalize()
            new_id = input("Enter ID in format ##(#)-###-##(#)" "Enter ID: ").upper()

            
            n.append(new_name)
            print("New Member Added.")

            r.append(new_rank)
            print("New Rank added.")

            d.append(new_div)
            print("New Division added.")
            
            id.append(new_id)
            print("New ID added.")


#remove_member(names, ranks, divs, ids):

#Asks for an ID.
#Finds the index.
#Removes the entry from _all 4 lists_ to keep them in sync.
        elif opt == "3":
            remove = input("Enter Name to Remove: ").capitalize()

            idx = n.index(remove)
            n.pop(idx)
            r.pop(idx)
            d.pop(idx)
            id.pop(idx)
            
            print("Removed Member.")
            

#update_rank(names, ranks, ids):

#Finds a member by ID.
#Updates their rank string.
        elif opt == "4":
            locate = input("Enter Members Name To Update: ").capitalize()
            
            idx = n.index(locate)
            new_rank = input("Enter New Rank: ").capitalize()
            r[idx] = new_rank
            print("Rank Updated:", new_rank)
            

#calculate_payroll(ranks)`:
    
#    -   Iterates through the ranks list.
        
#    -   Assigns a credit value to ranks (e.g., Captain = 1000, Ensign = 200).
        
#    -   Returns the total cost of the crew.
        elif opt == "5":
            captain = int(2500)
            commander = int(1750)
            lcommander = int(1000)
            
            total = 0
            for rank in r:
                if rank == "Captain":
                    total += captain
                if rank == "Commander":
                    total += commander
                if rank == "Lieutenant Commander":
                    total += lcommander

            print("Total Credits: ", total)


#search_crew(names, ranks, divs, ids):
    
#Asks for a search term.
#Prints any crew member whose name contains that term.
        elif opt == "6":
            jean_luc = 'Jean-Luc - Captain - Command - SP-937-215'
            kathryn = 'Kathryn - Captain - Command - NJ-573-219'
            spock = 'Spock - Commander - Science - S-179-276'
            montgonmery = 'Montgonmery - Lieutenant Commander - Engineering - SE-197-54T'
            worf = 'Worf - Lieutenant Commander - Security - KCD-445-31'
            
            term = input("Input Members Info To Search: ").capitalize()

            match term:
                case "Jean-Luc"|"SP-937-215":
                    print(jean_luc)
                
                case "Kathryn"|"NJ-573-219":
                    print(kathryn)

                case "Spock"|"Commander"|"Science"|"S-179-276":
                    print(spock)
                
                case "Montgonmery"|"Engineering"|"SE-197-54T":
                    print(montgonmery)
                
                case "Worf"|"Security"|"KCD-445-31":
                    print(worf)
                
                case "Captain":
                    print(jean_luc,"\n",kathryn)
                
                case "Command":
                    print(jean_luc,"\n", kathryn)

                case "Lieutenant":
                    print(montgonmery, "\n", worf)

                case _:
                    print("Invalid, Name Not Found")
            

#search = input("Search term related to members: ").capitalize()
#for i in range(len(n)):
#if search == n.index:
#print(n[i] + " - " + r[i] + " - " + d[i] + " - " + id[i])


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