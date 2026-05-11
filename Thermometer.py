class Thermometer:
    def __init__(self, celsius):
        self._celsius = celsius
        self._history = []
        
    @property
    def celsius(self):
        if self._celsius < -273.15:
            raise ValueError("Invalid temperature")
        return self._celsius
        
    @celsius.setter
    def celsius(self, value):
        self._history.append(self._celsius)
        self._celsius = value
        
    @property
    def fahrenheit(self):
        return (self._celsius * 9/5) + 32
        
    def get_history(self):
        return self._history
        
t = Thermometer(celsius=25)
print(t.celsius)
print(t.fahrenheit)

