class Subject:
    def __init__(self):
        self.observers = []

    def attach(self, obs):
        self.observers.append(obs)

    def notify(self, msg):
        for o in self.observers:
            o.update(msg)

class Observer:
    def update(self, msg):
        print("Received:", msg)
