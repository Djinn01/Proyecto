class ManageMS:
    def get_countries(matches, stadiums):
        stadium_matches = []
        cities = []
        for match in matches:
            if match.stadium_id not in stadium_matches:
                stadium_matches.append(match.stadium_id)
        for matches1 in stadium_matches:
            for stadium in stadiums:
                if stadium.id == matches1:
                    if stadium.id not in cities:
                        cities.append(stadium.city)
        print(cities)
        choice = input("Which country do you want to select?")
        if choice in cities:
            print(f"Matches in {choice}:")
            for match in matches:
                for stadium in stadiums:
                    if stadium.id == match.stadium_id and stadium.city == choice:
                        print(f"\tMatch ID: {match.id}")
                        print(f"\tMatch Number: {match.number}")
                        print(f"\tHome Team: {match.home}")
                        print(f"\tAway Team: {match.away}")
                        print(f"\tDate: {match.date}")
                        print(f"\tGroup: {match.group}")
                        print("\n")
        else:
            print("No matches found in this country")
            ManageMS.get_countries(matches, stadiums)
    
    def get_stadium(matches, stadiums):
        stadium_matches = []
        stadiums_names = []
        for match in matches:
            if match.stadium_id not in stadium_matches:
                stadium_matches.append(match.stadium_id)
        for matches1 in stadium_matches:
            for stadium in stadiums:
                if stadium.id == matches1:
                    if stadium.id not in stadiums_names:
                        stadiums_names.append(stadium.name)
        print(stadiums_names)
        choice = input("Which stadium do you want to select?")
        if choice in stadiums_names:
            print(f"Matches in {choice}:")
            for match in matches:
                for stadium in stadiums:
                    if stadium.id == match.stadium_id and stadium.name == choice:
                        print(f"\tMatch ID: {match.id}")
                        print(f"\tMatch Number: {match.number}")
                        print(f"\tHome Team: {match.home}")
                        print(f"\tAway Team: {match.away}")
                        print(f"\tDate: {match.date}")
                        print(f"\tGroup: {match.group}")
                        print("\n")
        else:
            print("No matches found in this stadium")
            ManageMS.get_stadium(matches, stadiums)
    
    def get_date(matches):
        match_date = []
        for match in matches:
            if match.date not in match_date:
                match_date.append(match.date)
        print(match_date)
        choice = input("Which date do you want to select?")
        if choice in match_date:
            for match in matches:
                if match["date"] == choice:
                    print(f"\tMatch ID: {match.id}")
                    print(f"\tMatch Number: {match.number}")
                    print(f"\tHome Team: {match.home}")
                    print(f"\tAway Team: {match.away}")
                    print(f"\tDate: {match.date}")
                    print(f"\tGroup: {match.group}")
                    print("\n")
        else:
            print("No matches found on this date")
            ManageMS.get_date(matches)



    def manageMS(matches, stadiums):
        print("\nSelect your search criteria")
        print("1. By State name")
        print("2. By Stadium Name")
        print("3. By Date Name")
        print("4. Leave")
        choice = input("Enter your choice: ")
        if choice == "1":
            ManageMS.get_countries(matches, stadiums)
        elif choice == "2":
            ManageMS.get_stadium(matches, stadiums)
        elif choice == "3":
            ManageMS.get_date(matches)
        elif choice == "4":
            ...
        else:
            print("Invalid choice")
            ManageMS.manageMS()