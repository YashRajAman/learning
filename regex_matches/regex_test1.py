import re


vehicle_registration_examples = [
    {
        "state": "Alabama",
        "example": "1-ABC-1234",
        "regex": r"^(1)[ -]?[A-Z]{3}[ -]?[0-9]{4}$"
    },
    {
        "state": "Alaska",
        "example": "ABC-1234",
        "regex": r"^[A-Z]{3}[ -]?[0-9]{4}$"
    },
    {
        "state": "Arizona",
        "example": "123-ABC-1234",
        "regex": r"^[0-9]{3}[ -]?[A-Z]{3}[ -]?[0-9]{4}$"
    },
    {
        "state": "Arkansas",
        "example": "ABC-1234",
        "regex": r"^[A-Z]{3}[ -]?[0-9]{4}$"
    },
    {
        "state": "California",
        "example": "1ABC-1234",
        "regex": r"^(1)[ -]?[A-Z]{3}[ -]?[0-9]{4}$"
    },
    {
        "state": "Colorado",
        "example": "123-ABC-1234",
        "regex": r"^[0-9]{3}[ -]?[A-Z]{3}[ -]?[0-9]{4}$"
    },
    {
        "state": "Connecticut",
        "example": "ABC-1234",
        "regex": r"^[A-Z]{3}[ -]?[0-9]{4}$"
    },
    {
        "state": "Delaware",
        "example": "123456",
        "regex": r"^[0-9]{6}$"
    },
    {
        "state": "Florida",
        "example": "1ABC-1234",
        "regex": r"^(1)[ -]?[A-Z]{3}[ -]?[0-9]{4}$"
    },
    {
        "state": "Georgia",
        "example": "ABC-1234",
        "regex": r"^[A-Z]{3}[ -]?[0-9]{4}$"
    },
    {
        "state": "Hawaii",
        "example": "ABC-1234",
        "regex": r"^[A-Z]{3}[ -]?[0-9]{4}$"
    },
    {
        "state": "Idaho",
        "example": "1ABC-1234",
        "regex": r"^(1)[ -]?[A-Z]{3}[ -]?[0-9]{4}$"
    },
    {
        "state": "Illinois",
        "example": "123-ABC-1234",
        "regex": r"^[0-9]{3}[ -]?[A-Z]{3}[ -]?[0-9]{4}$"
    },
    {
        "state": "Indiana",
        "example": "123-ABC-1234",
        "regex": r"^[0-9]{3}[ -]?[A-Z]{3}[ -]?[0-9]{4}$"
    },
    {
        "state": "Iowa",
        "example": "ABC-1234",
        "regex": r"^[A-Z]{3}[ -]?[0-9]{4}$"
    },
    {
        "state": "Kansas",
        "example": "123-ABC-1234",
        "regex": r"^[0-9]{3}[ -]?[A-Z]{3}[ -]?[0-9]{4}$"
    },
    {
        "state": "Kentucky",
        "example": "ABC-1234",
        "regex": r"^[A-Z]{3}[ -]?[0-9]{4}$"
    },
    {
        "state": "Louisiana",
        "example": "ABC-1234",
        "regex": r"^[A-Z]{3}[ -]?[0-9]{4}$"
    },
    {
        "state": "Maine",
        "example": "123-ABC-1234",
        "regex": r"^[0-9]{3}[ -]?[A-Z]{3}[ -]?[0-9]{4}$"
    },
    {
        "state": "Maryland",
        "example": "123-ABC-1234",
        "regex": r"^[0-9]{3}[ -]?[A-Z]{3}[ -]?[0-9]{4}$"
    },
    {
        "state": "Massachusetts",
        "example": "123-ABC-1234",
        "regex": r"^[0-9]{3}[ -]?[A-Z]{3}[ -]?[0-9]{4}$"
    },
    {
        "state": "Michigan",
        "example": "ABC-1234",
        "regex": r"^[A-Z]{3}[ -]?[0-9]{4}$"
    },
    {
        "state": "Minnesota",
        "example": "ABC-1234",
        "regex": r"^[A-Z]{3}[ -]?[0-9]{4}$"
    },
    {
        "state": "Mississippi",
        "example": "ABC-1234",
        "regex": r"^[A-Z]{3}[ -]?[0-9]{4}$"
    },
    {
        "state": "Missouri",
        "example": "ABC-1234",
        "regex": r"^[A-Z]{3}[ -]?[0-9]{4}$"
    },
    {
        "state": "Montana",
        "example": "123-ABC-1234",
        "regex": r"^[0-9]{3}[ -]?[A-Z]{3}[ -]?[0-9]{4}$"
    },
    {
        "state": "Nebraska",
        "example": "ABC-1234",
        "regex": r"^[A-Z]{3}[ -]?[0-9]{4}$"
    },
    {
        "state": "Nevada",
        "example": "123-ABC-1234",
        "regex": r"^[0-9]{3}[ -]?[A-Z]{3}[ -]?[0-9]{4}$"
    },
    {
        "state": "New Hampshire",
        "example": "123-ABC-1234",
        "regex": r"^[0-9]{3}[ -]?[A-Z]{3}[ -]?[0-9]{4}$"
    },
    {
        "state": "New Jersey",
        "example": "ABC-1234",
        "regex": r"^[A-Z]{3}[ -]?[0-9]{4}$"
    },
    {
        "state": "New Mexico",
        "example": "ABC-1234",
        "regex": r"^[A-Z]{3}[ -]?[0-9]{4}$"
    },
    {
        "state": "New York",
        "example": "ABC-1234",
        "regex": r"^[A-Z]{3}[ -]?[0-9]{4}$"
    },
    {
        "state": "North Carolina",
        "example": "ABC-1234",
        "regex": r"^[A-Z]{3}[ -]?[0-9]{4}$"
    },
    {
        "state": "North Dakota",
        "example": "123-ABC-1234",
        "regex": r"^[0-9]{3}[ -]?[A-Z]{3}[ -]?[0-9]{4}$"
    },
    {
        "state": "Ohio",
        "example": "ABC-1234",
        "regex": r"^[A-Z]{3}[ -]?[0-9]{4}$"
    },
    {
        "state": "Oklahoma",
        "example": "123-ABC-1234",
        "regex": r"^[0-9]{3}[ -]?[A-Z]{3}[ -]?[0-9]{4}$"
    },
    {
        "state": "Oregon",
        "example": "ABC-1234",
        "regex": r"^[A-Z]{3}[ -]?[0-9]{4}$"
    },
    {
        "state": "Pennsylvania",
        "example": "ABC-1234",
        "regex": r"^[A-Z]{3}[ -]?[0-9]{4}$"
    },
    {
        "state": "Rhode Island",
        "example": "123-ABC-1234",
        "regex": r"^[0-9]{3}[ -]?[A-Z]{3}[ -]?[0-9]{4}$"
    },
    {
        "state": "South Carolina",
        "example": "ABC-1234",
        "regex": r"^[A-Z]{3}[ -]?[0-9]{4}$"
    },
    {
        "state": "South Dakota",
        "example": "123-ABC-1234",
        "regex": r"^[0-9]{3}[ -]?[A-Z]{3}[ -]?[0-9]{4}$"
    },
    {
        "state": "Tennessee",
        "example": "ABC-1234",
        "regex": r"^[A-Z]{3}[ -]?[0-9]{4}$"
    },
    {
        "state": "Texas",
        "example": "ABC-1234",
        "regex": r"^[A-Z]{3}[ -]?[0-9]{4}$"
    },
    {
        "state": "Utah",
        "example": "123-ABC-1234",
        "regex": r"^[0-9]{3}[ -]?[A-Z]{3}[ -]?[0-9]{4}$"
    },
    {
        "state": "Vermont",
        "example": "123-ABC-1234",
        "regex": r"^[0-9]{3}[ -]?[A-Z]{3}[ -]?[0-9]{4}$"
    },
    {
        "state": "Virginia",
        "example": "ABC-1234",
        "regex": r"^[A-Z]{3}[ -]?[0-9]{4}$"
    },
    {
        "state": "Washington",
        "example": "ABC-1234",
        "regex": r"^[A-Z]{3}[ -]?[0-9]{4}$"
    },
    {
        "state": "West Virginia",
        "example": "ABC-1234",
        "regex": r"^[A-Z]{3}[ -]?[0-9]{4}$"
    },
    {
        "state": "Wisconsin",
        "example": "ABC-1234",
        "regex": r"^[A-Z]{3}[ -]?[0-9]{4}$"
    },
    {
        "state": "Wyoming",
        "example": "123-ABC-1234",
        "regex": r"^[0-9]{3}[ -]?[A-Z]{3}[ -]?[0-9]{4}$"
    }
]

# print(vehicle_registration_examples)

full_regex = []
for x in vehicle_registration_examples:
    full_regex.append(x["regex"])
full_regex = '|'.join(full_regex)

# print(full_regex)
print(len(full_regex))
with open("regex_matches/regex_file.txt", "w+") as file:
    file.write(full_regex)

pattern = re.compile(fr"{full_regex}", re.IGNORECASE)

# print(fr"{full_regex}")

print(vehicle_registration_examples[0].get("example"))

match = re.match(pattern, vehicle_registration_examples[0].get("example"))

print(match)
