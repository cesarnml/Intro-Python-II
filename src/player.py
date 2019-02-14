
class Player:
    def __init__(self, name, room):
        self.name = name
        self.room = room
        self.items = []

    def __str__(self):
        return f"{self.name} is {self.room.name}"

    def check_inventory(self):
        if len(self.items) > 0:
            player_items = "\n".join([str(item) for item in self.items])
        else:
            player_items = "nothing"
        print(f"\nYour inventory contains:\n{player_items}\n")

    def drop_item(self, item):
        self.items = list(
            filter(lambda i: i.name is not item.name, self.items))

    def take_item(self, item):
        self.items.append(item)
