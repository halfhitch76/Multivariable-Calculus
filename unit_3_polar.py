import math
from scipy import integrate

#Cartesian to Polar
def cartesian_to_polar(x, y):
    r = math.sqrt(x**2 + y**2)
    theta = math.atan2(y, x)
    
    # Convert theta to degrees
    theta_degrees = math.degrees(theta)
    
    return r, theta_degrees

#Polar to Cartesian
def polar_to_cartesian(r, theta_degrees):
    # Convert theta to radians
    theta_radians = math.radians(theta_degrees)
    
    x = r * math.cos(theta_radians)
    y = r * math.sin(theta_radians)
    
    return x, y

#Double Integral
def double_integral(func, x1, x2, y1, y2):
    result, error = integrate.dblquad(func, x1, x2, lambda x: y1, lambda x: y2)
    return result

# Example function to integrate: f(x, y) = x + y
def example_function(x, y):
    return x + y

def main():
    # Cartesian to Polar
    # Input Cartesian coordinates
    x = float(input("Enter the x-coordinate: "))
    y = float(input("Enter the y-coordinate: "))
    
    # Convert to polar coordinates
    r, theta_degrees = cartesian_to_polar(x, y)
    
    # Display the result
    print(f"Polar Coordinates: (r = {r}, θ = {theta_degrees} degrees)")


    #Polar to Cartesian
    # Input polar coordinates
    r = float(input("Enter the r-coordinate: "))
    theta_degrees = float(input("Enter the theta-coordinate in degrees: "))
    
    # Convert to Cartesian coordinates
    x, y = polar_to_cartesian(r, theta_degrees)
    
    # Display the result
    print(f"Cartesian Coordinates: (x = {x}, y = {y})")


    # Double Integral
    # Example of limits integration
    x1 = 0
    x2 = 1
    y1 = 0
    y2 = 1
    
    # Calculate the double integral of the example function
    result = double_integral(example_function, x1, x2, y1, y2)
    
    # Display the example result
    print(f"The double integral result is: {result}")

if __name__ == "__main__":
    main()
