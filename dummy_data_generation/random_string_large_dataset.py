import csv
import random

# List of names and places
names = ["john", "mary", "jane", "bob", "alice", "emma", "oliver", "lily"]
places = ["madrid", "london", "paris", "rome", "berlin", "amsterdam", "vienna", "zurich"]

# Function to generate a random list of names and places
def generate_random_values():
    return ' '.join(random.sample(names, random.randint(1, 5))), ' '.join(random.sample(places, random.randint(1, 5)))

# Open the CSV file for writing
with open('output.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    
    # Write the header
    writer.writerow(["name","place"])
    
    # Generate and write 5 million records
    for _ in range(5000000):
        name, place = generate_random_values()
        writer.writerow([name, place])