import random as r

class Ticket:
    def __init__(self, match, seats, codes, attendance) -> None:
        self.match_name = match
        self.seats = seats
        self.codes = codes
        self.attendance = attendance

    def generate_codes(self, db, n_sets):
        codes=[]
        i = 0
        while i < n_sets:
            nums = ["0", "1", "2", "3", "4", "5", " 6", "7", "8", "9", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "x", "y", "z"]
            while True:
                code = r.choices(nums, k = 5)
                if code in db:
                    continue
                else:
                    code = "".join(code)
                    codes.append(code)
                break
            i += 1
        self.codes = codes

    def change_attendance(self):
        self.attendance = True

    def dicc(self):
        return{
            "type": self.type,
            "price": self.price,
            "match_name": self.match,
            "seats": self.seats,
            "codes": self.codes,
            "attendance": self.attendance,
        }

class TicketGeneral(Ticket):
    type = "General"
    price = "35"

class TicketVip(Ticket):
    type = "VIP"
    price = "75"