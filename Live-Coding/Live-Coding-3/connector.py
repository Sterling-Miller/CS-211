"""Notifier interface, for wiring listener to model"""


class Notification:
    """An event notification from a Connectable to a Listener (concrete class)"""
    def __init__(self, msg_kind: str, msg_args: dict):
        self.msg_kind = msg_kind
        self.msg_args = msg_args


class Listener:
    """Abstract base class: Extend this to create something
    that reacts to notifications
    """
    def notify(self, notification: Notification):
        raise NotImplementedError(f"Notify method not implemented in {self.__class__}")


class Connectable:
    """Abstract base class: Extend this to enable connection"""
    def __init__(self):
        self.listeners: list[Listener] = []

    def add_listener(self, listener: Listener):
        self.listeners.append(listener)

    def notify_all(self, notification: Notification):
        for listener in self.listeners:
            listener.notify(notification)
