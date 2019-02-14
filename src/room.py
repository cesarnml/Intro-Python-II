class Room:
    def __init__(self, name, desc, items):
        self.name = name
        self.desc = desc
        self.items = items

    def print_items(self):
        if len(self.items) > 0:
            room_items = "\n".join([str(item) for item in self.items])
        else:
            room_items = "nothing"
        print(f"You look around the room and find:\n{room_items}")

    def remove_item(self, item):
        self.items = list(
            filter(lambda i: i.name is not item.name, self.items))

    def add_item(self, item):
        self.items.append(item)
