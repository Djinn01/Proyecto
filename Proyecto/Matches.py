class Matches:
    def __init__(self, id, number, home, away, date, group,stadium_id):
        self.id = id
        self.number = number
        self.home = home
        self.away = away
        self.date = date
        self.group = group
        self.stadium_id=stadium_id
    def show_attribute(self):
        print(f"id==>{self.id}")
        print(f"number==>{self.number}")
        print(f"home==>{self.home}")
        print(f"away==>{self.away}")
        print(f"date==>{self.date}")
        print(f"group==>{self.group}")
        print(f"stadium==> {self.stadium_id}")
