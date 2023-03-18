import connector


class Bell(connector.Listener):
    def __init__(self, material):
        super().__init__()
        self.material = material

    def notify(self, notification: connector.Notification):
        print(f"Ring ring goes the {self.material} bell! :)")


class Button(connector.Connectable):
    def __init__(self):
        super().__init__()

    def push(self):
        self.notify_all(connector.Notification("ButtonPress", {}))


button = Button()
bell = Bell("Gold")
bell2 = Bell("Brass")
button.add_listener(bell2)
button.add_listener(bell)
button.push()
