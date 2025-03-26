class StatC:
    
    def __init__(self, name, curr_value, max_value):
        self._name = name
        self._curr_value = curr_value
        self._max_value = max_value

    @property
    def name(self):
        return self._name

    @property
    def curr_value(self):
        return self._curr_value
    
    @property
    def max_value(self):
        return self._max_value
    
    @property
    def overall_value(self):
        return f"{self._curr_value}/{self._max_value}"
    
    @max_value.setter
    def max_value(self, new_value):
        self._max_value = new_value

    def decrement(self, value):
        if self._curr_value - value < 0:
            self._curr_value = 0
        else:
            self.curr_value -= value

    def increment(self, value):
        if self._curr_value + value > self._max_value:
            self._curr_value = self._max_value
        else:
            self.curr_value += value

