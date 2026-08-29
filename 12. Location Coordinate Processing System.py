# Location Coordinate Processing System

# Storing fixed GPS coordinates as tuples
location1 = (18.5204, 73.8567)   # Pune
location2 = (19.0760, 72.8777)   # Mumbai
location3 = (28.6139, 77.2090)   # Delhi

# Display coordinates
print("Location 1:", location1)
print("Location 2:", location2)
print("Location 3:", location3)

# Tuple indexing
print("\nLatitude of Location 1:", location1[0])
print("Longitude of Location 1:", location1[1])

# Tuple length
print("\nNumber of coordinates:", len(location1))

# Tuple concatenation
all_locations = location1 + location2 + location3
print("\nCombined coordinates:", all_locations)

# Tuple repetition
repeated_location = location1 * 2
print("\nRepeated Location 1:", repeated_location)

# Membership operation
if 18.5204 in location1:
    print("\nLatitude 18.5204 is present in Location 1")

# Tuple unpacking
latitude, longitude = location2
print("\nUnpacked Location 2:")
print("Latitude:", latitude)
print("Longitude:", longitude)

# Slicing
print("\nFirst four values from all locations:", all_locations[0:4])

# Comparing tuples
print("\nAre Location 1 and Location 2 the same?", location1 == location2)