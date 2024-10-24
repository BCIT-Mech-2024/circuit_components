import math

class Resistor:

    def __init__(self, resistance=None, voltage=None, current=None, power=None):
        self._resistance = resistance
        self._voltage = voltage
        self._current = current
        self._power = power

    def set_resistance(self, resistance):
        self._resistance = resistance
        return self

    def set_voltage(self, voltage):
        self._voltage = voltage
        return self

    def set_current(self, current):
        self._current = current
        return self

    def set_power(self, power):
        self._power = power
        return self

    def calculate(self):
        if self._resistance is not None: return self._calculate_from_known_resistance()
        elif self._voltage is not None: return self._calculate_from_known_voltage()
        elif self._current is not None: return self._calculate_from_known_current()
        else: return None


    def _calculate_from_known_resistance(self):
        output = Resistor()
        if self._voltage is not None:
            output._resistance = self._resistance
            output._voltage = self._voltage
            output._current = self._voltage / self._resistance
            output._power = self._voltage**2 / self._resistance
        elif self._current is not None:
            output._resistance = self._resistance
            output._voltage = self._current * self._resistance
            output._current = self._current
            output._power = self._current**2 * self._resistance
        elif self._power is not None:
            output._resistance = self._resistance
            output._voltage = math.sqrt(self._power * self._resistance)
            output._current = math.sqrt(self._power / self._resistance)
            output._power = self._power
        else: return None
        return output

    def _calculate_from_known_voltage(self):
        output = Resistor()
        if self._current is not None:
            output._resistance = self._voltage / self._current
            output._voltage = self._voltage
            output._current = self._current
            output._power = self._voltage * self._current
        elif self._power is not None:
            output._resistance = self._voltage**2 / self._power
            output._voltage = self._voltage
            output._current = self._power / self._voltage
            output._power = self._power
        else: return None
        return output

    def _calculate_from_known_current(self):
        output = Resistor()
        if self._power is not None:
            output._resistance = self._power / self._current**2
            output._voltage = self._power / self._current
            output._current = self._current
            output._power = self._power
        else: return None
        return output

    def __eq__(self, other):
        return self._resistance == other._resistance and self._voltage == other._voltage and self._current == other._current and self._power == other._power

    def __str__(self):
        return "R: {}\tV: {}\tC: {}\tP: {}".format(
                    self._resistance, 
                    self._voltage, 
                    self._current,
                    self._power,
                )

    def __add__(self, other):
        if self._resistance is None or other._resistance is None:
            raise ValueError("Both resistors need resistances to add in series")
        output = Resistor()
        output._resistance = self._resistance + other._resistance
        return output

    def __mul__(self, other):
        if self._resistance is None or other._resistance is None:
            raise ValueError("Both resistors need resistances to add in parallel")
        output = Resistor()
        output._resistance = (1/self._resistance + 1/other._resistance)**(-1)
        return output

