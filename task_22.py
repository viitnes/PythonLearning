class DigitalCounter:

    def __init__(self, min_value=0, max_value=9, start_value=0):
        self.min_value = min_value
        self.max_value = max_value
        self.value = start_value

    def set_min_value(self, min_value):
        self.min_value = min_value

    def set_max_value(self, max_value):
        self.max_value = max_value

    def set_start_value(self, start_value):
        self.value = start_value

    def increment(self):
        self.value += 1
        if self.value > self.max_value:
            self.value = self.min_value

    def get_value(self):
        return self.value

counter = DigitalCounter()

counter.set_min_value(0)
counter.set_max_value(99)

counter.set_start_value(10)

counter.increment()

print(counter.get_value())
