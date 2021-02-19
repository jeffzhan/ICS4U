import astronomy as a

e = a.Planet("earth", "terrestrial", 365, 12, 5)

print(e.name())
print(e.orbit_day())

e.change_orbit_day(366)
print(e.orbit_day())

print(e.get_num_moons())
e.change_number_moons(45)
print(e.get_num_moons())

e.add_moon(54)


