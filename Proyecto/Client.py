class Client:
    def __init__(self, name, id, age, tickets, compras, total_spent, total_seats):
        self.name = name
        self.id = id
        self.age = age
        self.tickets = tickets
        self.compras = compras
        self.total_spent = total_spent
        self.total_seats = total_seats
    def append_tickets(self, tickets):
        self.tickets.append(tickets)
    def tickets_dicc(self):
        tickets_dicc = []
        for ticket in self.tickets:
            tickets_dicc.append(ticket.dicc())
        return tickets_dicc
    def append_compras(self):
        compras = []
        for compra in self.compras:
            compra.append(compra.dicc())
        return compras
    def sum_diff_matches(self):
        matches = []
        for ticket in self.tickets:
            if ticket.match not in matches:
                matches.append(ticket.match)
        print(matches)
        return len(matches)
    def dicc(self):
        return {
            'name': self.name,
            'id': self.id,
            'age': self.age,
            'tickets': self.tickets_dicc(),
            'compras': self.append_compras(),
            'total_spent': self.total_spent,
            'total_seats': self.total_seats
        }