#importar
import requests
import json
import os
from Stadium import Stadium
from Restaurant import Restaurant
from Products import Product
from Teams import Team
from Matches import Matches
from Tickets import Ticket, TicketVip, TicketGeneral
from Client import Client
from ManageMS import ManageMS
from ManageT import ManageT
from ManageA import ManageA
from ManageR import ManageR
from ManageRS import ManageRS
from Statistics import Statistics



class App:
    #vacio las listas
    stadiums_db_ob = []
    restaurants_db_ob = []
    products_db_ob = []
    teams_db_ob = []
    matches_db_ob = []
    stadiums_db = []
    restaurants_db = []
    products_db = []
    teams_db_ob = []
    matches_db = []
    clients_db_ob = []


    def load_api(self):
        url_teams = "https://raw.githubusercontent.com/Algoritmos-y-Programacion/api-proyecto/main/teams.json"
        url_stadiums = "https://raw.githubusercontent.com/Algoritmos-y-Programacion/api-proyecto/main/stadiums.json"
        url_matches = "https://raw.githubusercontent.com/Algoritmos-y-Programacion/api-proyecto/main/matches.json"
        resp_teams = requests.get(url_teams)
        resp_stadiums = requests.get(url_stadiums)
        resp_matches = requests.get(url_matches)
        db_teams = json.loads(resp_teams.text)
        db_stadiums = json.loads(resp_stadiums.text)
        db_matches = json.loads(resp_matches.text)
        return db_teams, db_stadiums, db_matches
    
    def create_obs(self, db_teams, db_stadiums, db_matches):
        for t in db_teams:
            team = Team(t["id"], t["code"], t["name"], t["group"])
            self.teams_db_ob.append(team)
        for s in db_stadiums:
            rest = []
            for r in s["restaurants"]:
                products = []
                for p in r["products"]:
                    product = Product(p["name"], p["quantity"],p["price"], p["stock"], p["adicional"])
                    self.products_db_ob.append(product)
                    products.append(product)
                restaurante = Restaurant(t["name"],products)
                self.restaurants_db_ob.append(restaurante)
            stadium = Stadium(s["id"], s["name"], s["city"], s["capacity"], rest)
            self.stadiums_db_ob.append(stadium)
        for m in db_matches:
            match = Matches(m["id"], m["number"], m["home"]["id"], m["away"]["id"], m["date"], m["group"],m["stadium_id"])
            self.matches_db_ob.append(match)


    

    def show_restaurant():
        ...
    def upload_txt(self):
        teams_db_dicc = []
        stadiums_db_dicc = []
        matches_db_dicc = []
        clients_db_dicc = []
        for team in self.teams_db_ob:
            teams_db_dicc.append(vars(team))
        for match in self.matches_db_ob:
            matches_db_dicc.append(vars(match))
        for stadium in self.stadiums_db_ob:
            stadiums_db_dicc.append(stadium.dicc())
        for client in self.clients_db_ob:
            clients_db_dicc.append(client.dicc())
        db ={
            "teams": teams_db_dicc,
            "stadiums": stadiums_db_dicc,
            "matches": matches_db_dicc,
            "clients": clients_db_dicc,
        }
        with open("database.txt", "w") as file:
            file.write(json.dumps(db))

    def load_txt(self):
        teams_db_ob = []
        matches_db_ob = []
        stadiums_db_ob = []
        clients_db_ob = []
        with open("database.txt", "r") as file:
            db = json.load(file)
        self.teams_db_ob = [Team(**dicc) for dicc in db["teams"]]
        self.matches_db_ob = [Matches(**dicc) for dicc in db["matches"]]
        self.stadiums_db_ob = [Stadium(**dicc) for dicc in db["stadiums"]]
        self.clients_db_ob = [Client(**dicc) for dicc in db["clients"]]

    
    def start(self):
        if os.path.exists("database.txt"):
            with open("database.txt", "r") as file:
                n = len(file.read())
            if n>1:
                self.load_txt()
            else:
                db_teams, db_stadiums, db_matches = self.load_api()
                self.create_obs(db_teams, db_stadiums, db_matches)
        else:
            db_teams, db_stadiums, db_matches = self.load_api()
            self.create_obs(db_teams, db_stadiums, db_matches)

        while True:
            print("\nMenu:")
            print("1. Matches and Stadium Management")
            print("2. Tickets Managament")
            print("3. Attendance Management")
            print("4. Restaurant Managament")
            print("5. Restaurant Sales Management")
            print("6. Statistics")
            print("7. Leave")
            choice = int(input("Ingrese una opción: "))
            if choice == 1:
                print(self.stadiums_db_ob)
                ManageMS.manageMS(self.matches_db_ob, self.stadiums_db_ob)
            elif choice == 2:
                ManageT.ticket_seller(self.matches_db_ob, self.stadiums_db_ob, self.clients_db_ob)
            elif choice == 3:
                ...                       
            elif choice == 4:
                ManageR.manageR(self.stadiums_db_ob)           
            elif choice == 5:
                ...
            elif choice == 6:
                ...
            elif choice == 7:
                self.upload_txt()
                break           
            else:
                print("\nOpción inválida")



        print("Bienvenido a la Aplicación de Gestión de Futbol")



    
    




