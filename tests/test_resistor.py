import pytest
from circuit_components.resistor import Resistor

class TestResistor:
    def test_string(self):
        test_resistor = Resistor()
        expected = "R: None\tV: None\tC: None\tP: None"
        assert test_resistor.__str__() == expected

    def test_string_with_values(self):
        test_resistor = Resistor()
        test_resistor._resistance = 10
        test_resistor._voltage = 12
        test_resistor._current = 14
        test_resistor._power = 16
        expected = "R: 10\tV: 12\tC: 14\tP: 16"
        assert test_resistor.__str__() == expected

class TestResistorAdditionSeries(TestResistor):
    _resitor1 = Resistor(resistance=300)
    _resitor2 = Resistor(resistance=600)

    def test_add_with_missing_second(self):
        with pytest.raises(ValueError):
            self._resitor1 + Resistor()

    def test_add_with_missing_first(self):
        with pytest.raises(ValueError):
            Resistor() + self._resitor2

    def test_add_resistors(self):
        assert self._resitor1 + self._resitor2 == Resistor(resistance=900)


class TestResistorAdditionParallel(TestResistor):
    _resitor1 = Resistor(resistance=300)
    _resitor2 = Resistor(resistance=600)

    def test_add_with_missing_second(self):
        with pytest.raises(ValueError):
            self._resitor1 * Resistor()

    def test_add_with_missing_first(self):
        with pytest.raises(ValueError):
            Resistor() * self._resitor2

    def test_add_resistors(self):
        assert self._resitor1 * self._resitor2 == Resistor(resistance=200)

class TestResistorCalculate(TestResistor):
    _expected_resistor = Resistor(
        resistance=2000,
        voltage=10,
        current=0.005,
        power=0.05,
    )

    def test_calculate_empty(self):
        test_resistor = Resistor()
        assert test_resistor.calculate() is None

    def test_calculate_only_resistance(self):
        test_resistor = Resistor().set_resistance(1200)
        assert test_resistor.calculate() is None

    def test_calculate_with_voltage(self):
        test_resistor = Resistor(
            resistance=2000,
            voltage=10,
        )
        assert test_resistor.calculate() == self._expected_resistor

    def test_calculate_with_current(self):
        test_resistor = Resistor(
            resistance=2000,
            current=0.005,
        )
        assert test_resistor.calculate() == self._expected_resistor

    def test_calculate_with_power(self):
        test_resistor = Resistor(
            resistance=2000,
            power=0.05,
        )
        assert test_resistor.calculate() == self._expected_resistor
