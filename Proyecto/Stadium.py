class Stadium:
    def __init__(self, id, name, city, capacity, restaurants):
        self.id = id
        self.name = name
        self.city = city
        self.capacity = capacity
        self.restaurants = restaurants

    def show_attributes(self):
        print(f"Stadium Name: {self.name}")
        print(f"City: {self.city}")
        print(f"Capacity: {self.capacity}")
        print("Restaurants:")
        for restaurant in self.restaurants:
            print(f"\tRestaurant Name: {restaurant.name}")
    
    def dicc(self):
        return {
            'id': self.id,
            'name': self.name,
            'city': self.city,
            'capacity': self.capacity,
            'restaurants': [restaurant.dicc() for restaurant in self.restaurants]
        }

