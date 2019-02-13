
class Player:
    def __init__(self, name, room):
        self.name = name
        self.room = room
        self.items = []

    def __str__(self):
        return f"{self.name} is {self.room.name}"

    def check_inventory(self):
        if len(self.items) > 0:
            player_items = ", ".join([item for item in self.items])
        else:
            player_items = "nothing"
        print(f"Your inventory contains: {player_items}.")

    def drop_item(self, item):
        self.items = list(
            filter(lambda i: i.name is not item.name, self.items))

    def take_item(self, item):
        self.items.append(item)
