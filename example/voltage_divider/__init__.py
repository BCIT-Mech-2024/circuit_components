from circuit_components.resistor import Resistor

battery_voltage = 24

loads = [
    Resistor(resistance=15000, power=0.01),
    Resistor(resistance=2700, power=0.01),
    Resistor(resistance=1000, power=0.01),
    Resistor(resistance=3900, power=0.01),
    Resistor(resistance=8200, power=0.01),
]

defined_loads = [r.calculate() for r in loads]

positive_current = sum([r._current for r in defined_loads[:2]])
negative_current = sum([r._current for r in defined_loads[2:]])

max_current = max(positive_current, negative_current)
bleed_current = max_current * 0.109
total_current = max_current + bleed_current

dividers = [
    Resistor(voltage=battery_voltage - defined_loads[0]._voltage - defined_loads[4]._voltage),
    Resistor(voltage=defined_loads[0]._voltage - defined_loads[1]._voltage),
    Resistor(voltage=defined_loads[1]._voltage),
    Resistor(voltage=defined_loads[2]._voltage),
    Resistor(voltage=defined_loads[3]._voltage - defined_loads[2]._voltage),
    Resistor(voltage=defined_loads[4]._voltage - defined_loads[3]._voltage),
]

dividers[0]._current = total_current
dividers[1]._current = total_current - defined_loads[0]._current
dividers[2]._current = dividers[1]._current - defined_loads[1]._current
dividers[3]._current = total_current - defined_loads[2]._current - defined_loads[3]._current - defined_loads[4]._current
dividers[4]._current = dividers[3]._current + defined_loads[2]._current
dividers[5]._current = dividers[4]._current + defined_loads[3]._current

defined_dividers = [r.calculate() for r in dividers]

print("Loads")
for i in range(0, 5):
    print(defined_loads[i])

print("dividers")
for i in range(0, 5):
    print(defined_dividers[i])

