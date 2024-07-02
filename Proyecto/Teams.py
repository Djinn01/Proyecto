class Team:
    def __init__(self, team_id, team_name, team_code, team_group):
        self.team_id = team_id
        self.team_name = team_name
        self.team_code = team_code
        self.team_group = team_group

    def show_attribute(self):
        print(f"id ==> {self.team_id}")
        print(f"name ==> {self.team_name}")
        print(f"code ==> {self.team_code}")
        print(f"group ==> {self.team_group}")
    
    def dicc(self):
        return{
            "team_id": self.team_id,
            "team_name": self.team_name,
            "team_code": self.team_code,
            "team_group": self.team_group
        }
