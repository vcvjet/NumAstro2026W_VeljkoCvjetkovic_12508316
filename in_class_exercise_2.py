def create_star(name, mass, radius, temperature):
    """
    Creates and returns a dictionary containing the star's properties.
    """
    return {
        "name": name,
        "mass": mass,
        "radius": radius,
        "temperature": temperature
    }

def print_star(star):
    """
    Takes a star dictionary and prints its contents in a readable format.
    """
    print(f"--- Star Details: {star['name']} ---")
    print(f"Mass:        {star['mass']} Solar Masses")
    print(f"Radius:      {star['radius']} Solar Radii")
    print(f"Temperature: {star['temperature']} K")

def is_FGKM(star, t_limit=7300):
    """
    Returns True if the star's temperature is strictly less than t_limit, 
    otherwise returns False.
    """
    return star["temperature"] < t_limit

# --- Example Usage ---
if __name__ == "__main__":
    # 1. Create the star dictionary
    star = create_star("Sirius", 2.06, 1.71, 9940)
    
    # 2. Print the star's details
    print_star(star)
    print()  # Add a blank line for spacing
    
    # 3. Check if it falls under the temperature limit
    limit = 7300
    if is_FGKM(star, t_limit=limit):
        print(f"True: {star['name']} is cool enough (under {limit}K).")
    else:
        print(f"False: {star['name']} is hotter than {limit}K. ")
