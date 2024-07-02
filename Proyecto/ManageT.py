from Tickets import Ticket, TicketGeneral, TicketVip
class ManageT:

#     def create_map_general(match, stadiums):
#         clave = {0:"O",1:"X",2:"#"}
#         total_rows = (stadium.capacity[1] + 9) // 10
#         for i in range(len(total_rows)):
#             ...
#         for stadium in stadiums:
#             if match == stadium.id:
#                 print(f"{match.id}.\n {match.home} vs {match.away}\n {stadium.name}\n {stadium.city}\n \n")

#     def create_map_vip(match, stadiums):
#         for stadium in stadiums:
#             if match == stadium.id:

#                 total_seats = stadium.capacity[0] + stadium.capacity[1]
#                 total_rows = (total_seats + 9) // 10  

#                 stadium_map = [['O' for _ in range(10)] for _ in range(total_rows)]

#                 vip_count = 0
#                 general_count = 0

#                 for row in range(total_rows):
#                     for seat in range(10):
#                         if vip_count < stadium.capacity[0]:
#                             stadium_map[row][seat] = 'X'
#                             vip_count += 1
#                         elif general_count < stadium.capacity[1]:
#                             stadium_map[row][seat] = 'X'
#                             general_count += 1

#                 return stadium_map
            
#     def choose_seat(stadium_map, row, seat):
#         if row < len(stadium_map) and seat < 10:
#             if stadium_map[row][seat] == 'O':
#                 stadium_map[row][seat] = 'X'
#                 return True
#             else:
#                 print("Seat is already taken.")
#                 return False
#         else:
#             print("Invalid seat location.")
#             return False
    

    def ticket_seller(matches, stadiums):
        choice = input("Do you wish to purchase. \n1. Yes, \n2. No")
        if choice == "1":
            client_id = int(input("What is your ID?"))
            client_name = input("What is your name?")
            client_age = int(input("What is your age?"))
            print("What match do you wish to buy?")
            for match in matches:
                for stadium in stadiums:
                    if match.stadium_id == stadium.id:
                        print(f"{match.id}\n {match.home} vs {match.away}\n {stadium.name}\n {stadium.city}\n \n")  
            xd = True   
            while xd is True:
                chosed_match = []
                match_id = input("Choose a match by its id: ")
                for match in matches:
                    if match.id == match_id:
                        chosed_match.append(match)
                        xd = False
                        break
            
            
        #     print(ManageT.create_map_vip(chosed_match, stadiums))
        #     print("Choose your seat:") 
        #     while True:
        #         row = int(input("Choose a row: "))
        #         seat = int(input("Choose a seat: "))

        #         ManageT.choose_seat(stadium_map, row, seat)
                
        xd = True
        while xd is True:
                choice = input("Do you wish for:\n 1.Vip\n 2.General ")
                if choice == "1":
                    ticket_type = "vip"
                    xd = False
                elif choice == "2":
                    ticket_type = "general"
                    xd = False
                else:
                    print("Invalid choice")
                    continue
            