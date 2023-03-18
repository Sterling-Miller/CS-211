import connector


class KitchenObject(connector.Connectable):

    def __init__(self):
        super().__init__()
        self.is_power = True
        self.current_temp = 0

    def report_temp(self):
        self.notify_all(connector.Notification('Temperature', {'value': self.current_temp}))


class Refrigerator(KitchenObject):

    def __init__(self):
        super().__init__()
        self.contents = []
        self.current_temp = 3

    def insert_item(self, item):
        self.current_temp += 1
        self.contents.append(item)
        self.report_temp()

    def contents(self) -> list:
        return self.contents()


class TempMonitor(connector.Listener):

    def __init__(self, min_temp: float, max_temp: float):
        self.min = min_temp
        self.max = max_temp

    def notify(self, notification: connector.Notification):
        if notification.msg_kind != 'Tempeture':
            return

        new_temp = notification.msg_arg['values']

        if new_temp >= self.min and new_temp <= self.max:
            print("The temp is all good")

def main():
    fridge = Refrigerator(0, 6)
    monitor = TempMonitor()
    fridge.add_listener(monitor)
