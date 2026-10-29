
#############################################################################

class Star:
	def __init__(self, name, mass, radius, temperature):
		self.name = name
		self.mass = mass
		self.radius = radius
		self.temperature = temperature

	def print_info(self):
        	print(f"--- Star Information ---")
        	print(f"Name:        {self.name}")
        	print(f"Radius:      {self.radius} solar radii")
        	print(f"Mass:        {self.mass} solar masses")
        	print(f"Temperature: {self.temperature} Kelvin")

	def is_FGKM(self, t_limit=7300):
        	print(self.temperature < t_limit)

	def __str__(self):
        	return f"Star: {self.name} | Radius: {self.radius} R☉ | Mass: {self.mass} M☉ | Temperature: {self.temperature} K"

print("\n ################## \n")
sirius = Star("Sirius", 2.06, 1.71, 9940)

sirius.print_info()

siriusA = Star("Sirius A", 2.06, 1.71, 7000)

siriusA.print_info()

siriusB = Star("Sirius B", 2.06, 1.71, 7300)

siriusB.print_info()

print("\n ################## \n")

# Testing siriusA
print(f"Checking {siriusA.name}:")
siriusA.is_FGKM()  # Prints True

print("\n ################## \n")

# Testing siriusB
print(f"Checking {siriusB.name}:")
siriusB.is_FGKM()  # Prints False
print("\n ################## \n")

# Print original sirius
print(sirius)
print("\n ################## \n")

