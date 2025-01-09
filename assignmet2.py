# 1. Area of a Rectangle
length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))
area_rectangle = length * width
print(f"Area of the rectangle: {area_rectangle}")

# 2. Circumference of a Circle
import math
radius = float(input("Enter the radius of the circle: "))
circumference = 2 * math.pi * radius
print(f"Circumference of the circle: {circumference}")

# 3. Simple Interest
principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the rate of interest: "))
time = float(input("Enter the time in years: "))
simple_interest = principal * rate * time
print(f"Simple Interest: {simple_interest}")

# 4. Speed of an Object
distance = float(input("Enter the distance: "))
time = float(input("Enter the time: "))
speed = distance / time
print(f"Speed: {speed}")

# 5. BMI Calculator
weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in meters: "))
bmi = weight / (height ** 2)
print(f"Body Mass Index (BMI): {bmi}")

# 6. Force Using Newton's Second Law
mass = float(input("Enter the mass in kg: "))
acceleration = float(input("Enter the acceleration in m/s^2: "))
force = mass * acceleration
print(f"Force: {force}")

# 7. Compound Interest
principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the annual interest rate (in decimal): "))
n = int(input("Enter the number of times interest is compounded per year: "))
time = float(input("Enter the time in years: "))
amount = principal * (1 + rate / n) ** (n * time)
compound_interest = amount - principal
print(f"Compound Interest: {compound_interest}")

# 8. Perimeter of a Triangle
a = float(input("Enter the first side of the triangle: "))
b = float(input("Enter the second side of the triangle: "))
c = float(input("Enter the third side of the triangle: "))
perimeter_triangle = a + b + c
print(f"Perimeter of the triangle: {perimeter_triangle}")

# 9. Volume of a Sphere
radius = float(input("Enter the radius of the sphere: "))
volume_sphere = (4/3) * math.pi * radius ** 3
print(f"Volume of the sphere: {volume_sphere}")

# 10. Kinetic Energy
mass = float(input("Enter the mass in kg: "))
velocity = float(input("Enter the velocity in m/s: "))
kinetic_energy = 0.5 * mass * velocity ** 2
print(f"Kinetic Energy: {kinetic_energy}")

# 11. Quadratic Equation Roots
a = float(input("Enter the coefficient a: "))
b = float(input("Enter the coefficient b: "))
c = float(input("Enter the coefficient c: "))
discriminant = b**2 - 4*a*c
if discriminant >= 0:
    root1 = (-b + math.sqrt(discriminant)) / (2*a)
    root2 = (-b - math.sqrt(discriminant)) / (2*a)
    print(f"Roots of the quadratic equation: {root1}, {root2}")
else:
    print("The quadratic equation has no real roots.")

# 12. Temperature Conversion
celsius = float(input("Enter the temperature in Celsius: "))
fahrenheit = (celsius * 9/5) + 32
print(f"Temperature in Fahrenheit: {fahrenheit}")

# 13. Gravitational Force
G = 6.67430e-11
m1 = float(input("Enter the mass of the first object (kg): "))
m2 = float(input("Enter the mass of the second object (kg): "))
r = float(input("Enter the distance between the objects (m): "))
gravitational_force = G * (m1 * m2) / (r ** 2)
print(f"Gravitational Force: {gravitational_force}")

# 14. Volume of a Cylinder
radius = float(input("Enter the radius of the cylinder: "))
height = float(input("Enter the height of the cylinder: "))
volume_cylinder = math.pi * radius ** 2 * height
print(f"Volume of the cylinder: {volume_cylinder}")

# 15. Pressure
force = float(input("Enter the force applied: "))
area = float(input("Enter the area: "))
pressure = force / area
print(f"Pressure: {pressure}")

# 16. Electric Power
voltage = float(input("Enter the voltage: "))
current = float(input("Enter the current: "))
power = voltage * current
print(f"Electric Power: {power}")

# 17. Perimeter of a Circle
radius = float(input("Enter the radius of the circle: "))
perimeter_circle = 2 * math.pi * radius
print(f"Perimeter of the circle: {perimeter_circle}")

# 18. Future Value in Savings
present_value = float(input("Enter the present value: "))
rate = float(input("Enter the annual interest rate (in decimal): "))
time = float(input("Enter the time in years: "))
future_value = present_value * (1 + rate) ** time
print(f"Future Value: {future_value}")

# 19. Work Done by a Force
force = float(input("Enter the force: "))
distance = float(input("Enter the distance: "))
theta = math.radians(float(input("Enter the angle between force and direction of movement (in degrees): ")))
work_done = force * distance * math.cos(theta)
print(f"Work Done: {work_done}")

# 20. Heat Transfer
mass = float(input("Enter the mass: "))
specific_heat_capacity = float(input("Enter the specific heat capacity: "))
delta_temperature = float(input("Enter the change in temperature: "))
heat_transfer = mass * specific_heat_capacity * delta_temperature
print(f"Heat Transfer: {heat_transfer}")