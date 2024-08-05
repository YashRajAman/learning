from faker import Faker
import random

fake = Faker()

class fake_data:

    #user_id, name, contact, email, address, occupation, hobby,
    #  highest_qualification

    name:str
    contact: str
    email: str
    address: str
    occupation: str
    hobby: str
    qualification: str
    user_id: str

    def __init__(self, userid):
        self.user_id = userid



    def generate_fake_data(self,userid):
        fake = Faker()
        data = { "user_id" : userid,
        "name" : fake.name(),
        "contact" : fake.phone_number(),
        "email" : fake.email(),
        "address" : fake.address(),
        "occupation" : self.get_random_occupation(),
        "hobby" : self.get_random_hobby(),
        "qualification" : self.get_random_qualification()}

    def get_random_qualification(self):
        academic_qualifications = {
        "PhD": "Doctor of Philosophy",
        "MD": "Doctor of Medicine",
        "DO": "Doctor of Osteopathic Medicine",
        "DVM": "Doctor of Veterinary Medicine",
        "DDS": "Doctor of Dental Surgery",
        "DMD": "Doctor of Dental Medicine",
        "JD": "Juris Doctor",
        "LLB": "Bachelor of Laws",
        "LLM": "Master of Laws",
        "MBA": "Master of Business Administration",
        "MPA": "Master of Public Administration",
        "MFA": "Master of Fine Arts",
        "MS": "Master of Science",
        "MA": "Master of Arts",
        "MSc": "Master of Science",
        "MEng": "Master of Engineering",
        "MEd": "Master of Education",
        "MPhil": "Master of Philosophy",
        "MRes": "Master of Research",
        "MPH": "Master of Public Health",
        "MHA": "Master of Health Administration",
        "MAcc": "Master of Accountancy",
        "MSW": "Master of Social Work",
        "MST": "Master of Studies",
        "MLIS": "Master of Library and Information Science",
        "BSc": "Bachelor of Science",
        "BA": "Bachelor of Arts",
        "BEng": "Bachelor of Engineering",
        "BBA": "Bachelor of Business Administration",
        "BFA": "Bachelor of Fine Arts",
        "BEd": "Bachelor of Education",
        "BCom": "Bachelor of Commerce",
        "BSN": "Bachelor of Science in Nursing",
        "BN": "Bachelor of Nursing",
        "BPH": "Bachelor of Public Health",
        "BMus": "Bachelor of Music",
        "BDes": "Bachelor of Design",
        "BArch": "Bachelor of Architecture",
        "BTech": "Bachelor of Technology",
        "BPharm": "Bachelor of Pharmacy",
        "BNSc": "Bachelor of Nursing Science",
        "BM": "Bachelor of Medicine",
        "BDS": "Bachelor of Dental Surgery",
        "LLD": "Doctor of Laws",
        "DBA": "Doctor of Business Administration",
        "EdD": "Doctor of Education",
        "DSc": "Doctor of Science",
        "DM": "Doctor of Management",
        "DPT": "Doctor of Physical Therapy",
        "DNP": "Doctor of Nursing Practice",
        "DSW": "Doctor of Social Work",
        "DEng": "Doctor of Engineering",
        "ScD": "Doctor of Science",
        "PsyD": "Doctor of Psychology",
        "PharmD": "Doctor of Pharmacy"
    }

        return academic_qualifications[random.choice(list(academic_qualifications.keys()))]

    def get_random_hobby(self):
        hobbies = {
        "Gardening": "Growing and maintaining plants",
        "Cooking": "Preparing food",
        "Baking": "Cooking food using prolonged dry heat",
        "Knitting": "Creating fabric by interlocking loops of yarn",
        "Crocheting": "Creating fabric from yarn using a crochet hook",
        "Sewing": "Using a needle and thread to stitch fabric",
        "Drawing": "Creating pictures using pencils or pens",
        "Painting": "Creating artwork using paint",
        "Photography": "Taking pictures with a camera",
        "Writing": "Composing text",
        "Reading": "Reading books, articles, etc.",
        "Journaling": "Writing in a journal",
        "Scrapbooking": "Creating a scrapbook",
        "Collecting": "Gathering and keeping items of interest",
        "Hiking": "Walking in nature",
        "Running": "Jogging or sprinting",
        "Cycling": "Riding a bicycle",
        "Swimming": "Moving through water",
        "Fishing": "Catching fish",
        "Camping": "Staying overnight in nature",
        "Traveling": "Visiting new places",
        "Birdwatching": "Observing birds",
        "Stargazing": "Observing the stars",
        "Yoga": "Practicing yoga poses",
        "Meditation": "Practicing mindfulness and relaxation",
        "Pilates": "A form of low-impact exercise",
        "Fitness": "Engaging in physical exercise",
        "Weightlifting": "Lifting weights",
        "Martial Arts": "Practicing martial arts",
        "Dancing": "Moving to music",
        "Singing": "Vocalizing musical sounds",
        "Playing Musical Instruments": "Playing instruments",
        "Listening to Music": "Enjoying music",
        "Attending Concerts": "Going to live music performances",
        "Watching Movies": "Viewing films",
        "Watching TV Shows": "Viewing television programs",
        "Acting": "Performing in plays or films",
        "Theater": "Participating in live theater",
        "Comedy": "Performing or enjoying comedy",
        "Magic": "Performing magic tricks",
        "Puzzles": "Solving puzzles",
        "Board Games": "Playing board games",
        "Card Games": "Playing card games",
        "Video Games": "Playing video games",
        "Role-Playing Games": "Participating in role-playing games",
        "Chess": "Playing chess",
        "Volunteering": "Helping others",
        "Mentoring": "Guiding others",
        "Community Service": "Participating in community activities",
        "DIY Projects": "Do-it-yourself home projects",
        "Woodworking": "Creating objects from wood",
        "Metalworking": "Creating objects from metal",
        "3D Printing": "Creating objects using a 3D printer",
        "Model Building": "Constructing models",
        "Lego Building": "Creating with Lego bricks",
        "Origami": "Folding paper into shapes",
        "Calligraphy": "Art of beautiful handwriting",
        "Pottery": "Creating objects from clay",
        "Sculpting": "Creating figures from materials",
        "Jewelry Making": "Creating jewelry",
        "Beading": "Creating objects with beads",
        "Embroidery": "Decorating fabric with needle and thread",
        "Quilting": "Creating quilts",
        "Weaving": "Creating fabric by interlacing threads",
        "Macrame": "Creating decorative knots",
        "Leatherworking": "Creating objects from leather",
        "Painting Miniatures": "Painting small models",
        "Carving": "Shaping objects by cutting",
        "Whittling": "Carving small objects from wood",
        "Glassblowing": "Shaping glass using a blowpipe",
        "Mosaic Art": "Creating images with small pieces",
        "Digital Art": "Creating art using digital tools",
        "Graphic Design": "Creating visual content",
        "Animation": "Creating animated images",
        "Filmmaking": "Creating films",
        "Podcasting": "Creating audio content",
        "Blogging": "Writing and publishing blog posts",
        "Vlogging": "Creating video blogs",
        "Streaming": "Broadcasting live video",
        "Social Media": "Engaging with social media",
        "DIY Electronics": "Creating electronic projects",
        "Robotics": "Building robots",
        "Coding": "Writing computer programs",
        "Web Development": "Creating websites",
        "App Development": "Creating mobile applications",
        "Homebrewing": "Brewing beer at home",
        "Winemaking": "Making wine",
        "Mixology": "Creating cocktails",
        "Baking Bread": "Making bread",
        "Cooking International Cuisine": "Cooking food from different cultures",
        "Making Sauces": "Creating sauces",
        "Fermenting": "Preserving food through fermentation",
        "Gardening Vegetables": "Growing vegetables",
        "Gardening Flowers": "Growing flowers",
        "Indoor Gardening": "Growing plants indoors",
        "Urban Gardening": "Gardening in an urban environment",
        "Beekeeping": "Raising bees",
        "Aquascaping": "Designing underwater landscapes",
        "Keeping Fish": "Raising fish",
        "Keeping Reptiles": "Raising reptiles",
        "Pet Training": "Training pets",
        "Pet Grooming": "Caring for pets' appearance",
        "Horseback Riding": "Riding horses"
    }

        return random.choice(list(hobbies.keys()))

    def get_random_occupation(self):
        occupations = {
        "Accountant": "A person who prepares and examines financial records",
        "Actor": "A person who performs in plays, movies, or television shows",
        "Architect": "A person who designs buildings and in many cases also supervises their construction",
        "Artist": "A person who creates art",
        "Baker": "A person who bakes and sells bread and other baked goods",
        "Barber": "A person who cuts hair, especially men's, and shaves or trims beards",
        "Bartender": "A person who prepares and serves drinks at a bar",
        "Biologist": "A scientist who studies living organisms",
        "Carpenter": "A person who builds and repairs wooden structures",
        "Chef": "A professional cook",
        "Chemist": "A scientist who studies chemicals",
        "Chiropractor": "A healthcare professional who treats disorders of the musculoskeletal system",
        "Civil Engineer": "An engineer who designs and oversees the construction of public works",
        "Computer Scientist": "A person who studies and develops computer systems and software",
        "Dentist": "A medical professional who treats diseases and conditions of the teeth and gums",
        "Designer": "A person who plans the form, look, or workings of something",
        "Doctor": "A medical professional who diagnoses and treats illnesses",
        "Economist": "A person who studies the economy",
        "Electrician": "A person who installs and maintains electrical systems",
        "Engineer": "A professional who applies scientific knowledge to design, build, and maintain structures, machines, and systems",
        "Farmer": "A person who owns or manages a farm",
        "Firefighter": "A person who fights fires",
        "Fisherman": "A person who catches fish",
        "Graphic Designer": "A person who creates visual content to communicate messages",
        "Hairdresser": "A person who cuts and styles hair",
        "Journalist": "A person who writes for newspapers, magazines, or news websites",
        "Judge": "A public official appointed to decide cases in a court of law",
        "Lawyer": "A professional who practices law",
        "Librarian": "A person who works in a library",
        "Machinist": "A person who operates machine tools",
        "Mechanic": "A person who repairs and maintains machinery",
        "Musician": "A person who plays a musical instrument",
        "Nurse": "A healthcare professional who cares for patients",
        "Optician": "A person who designs, fits, and dispenses lenses for the correction of vision",
        "Painter": "A person who paints buildings or creates art with paint",
        "Pharmacist": "A healthcare professional who prepares and dispenses medications",
        "Photographer": "A person who takes photographs",
        "Physician": "A medical doctor",
        "Physicist": "A scientist who studies matter and energy",
        "Pilot": "A person who operates the controls of an aircraft",
        "Plumber": "A person who installs and repairs water systems",
        "Police Officer": "A person who enforces the law",
        "Programmer": "A person who writes computer software",
        "Psychologist": "A professional who studies the mind and behavior",
        "Real Estate Agent": "A person who buys and sells property",
        "Researcher": "A person who conducts scientific studies",
        "Scientist": "A person who conducts scientific research",
        "Social Worker": "A professional who helps individuals, families, and groups improve their well-being",
        "Software Developer": "A person who creates computer programs",
        "Surgeon": "A medical doctor who performs surgeries",
        "Teacher": "A person who educates students",
        "Therapist": "A professional who provides mental health counseling",
        "Translator": "A person who converts written text from one language to another",
        "Truck Driver": "A person who drives a truck",
        "Veterinarian": "A medical professional who treats animals",
        "Waiter": "A person who serves food and drinks at a restaurant",
        "Web Developer": "A person who creates websites",
        "Writer": "A person who writes books, articles, etc.",
        "Zoologist": "A scientist who studies animals",
        "Air Traffic Controller": "A person who coordinates the movement of aircraft",
        "Anthropologist": "A scientist who studies human behavior and societies",
        "Archaeologist": "A scientist who studies ancient cultures",
        "Astronomer": "A scientist who studies celestial objects",
        "Auditor": "A person who examines financial records",
        "Biochemist": "A scientist who studies the chemistry of living organisms",
        "Broker": "A person who buys and sells goods or assets for others",
        "Butcher": "A person who cuts and sells meat",
        "Cameraman": "A person who operates a camera",
        "Cartographer": "A person who creates maps",
        "Chaplain": "A religious leader who provides spiritual care",
        "Clerk": "A person who performs office tasks",
        "Coach": "A person who trains athletes or teams",
        "Counselor": "A professional who provides advice and guidance",
        "Curator": "A person who manages a museum or collection",
        "Dancer": "A person who performs dances",
        "Dietitian": "A healthcare professional who advises on diet and nutrition",
        "Editor": "A person who prepares content for publication",
        "Event Planner": "A person who organizes events",
        "Florist": "A person who sells and arranges flowers",
        "Geologist": "A scientist who studies the Earth",
        "Historian": "A person who studies and writes about history",
        "Illustrator": "An artist who creates images for books, magazines, etc.",
        "Interpreter": "A person who translates spoken language",
        "Janitor": "A person who cleans and maintains buildings",
        "Lab Technician": "A professional who works in a laboratory",
        "Loan Officer": "A person who evaluates and approves loan applications",
        "Mathematician": "A scientist who studies and applies mathematics",
        "Meteorologist": "A scientist who studies weather and climate",
        "Nanny": "A person who cares for children",
        "Paramedic": "A healthcare professional who provides emergency medical care",
        "Pilot": "A person who operates the controls of an aircraft",
        "Politician": "A person involved in politics",
        "Postal Worker": "A person who delivers mail",
        "Publicist": "A person who manages publicity for a company or individual",
        "Receptionist": "A person who greets visitors and manages calls",
        "Statistician": "A scientist who collects and analyzes data",
        "Surveyor": "A professional who measures land and plots boundaries",
        "Tailor": "A person who makes or alters clothing",
        "Tattoo Artist": "A person who applies tattoos",
        "Technician": "A person skilled in the technical aspects of a field",
        "Tour Guide": "A person who leads tourists",
        "Tutor": "A person who provides individual instruction",
        "Umpire": "A person who enforces the rules in sports",
        "Welder": "A person who fuses materials together",
        "Youth Worker": "A person who works with young people to support their development"
    }

        return random.choice(list(occupations.keys()))

    
    def get_name(self):
        self.name = fake.name()
        return self.name
    
    def get_contact(self):
        self.contact = fake.phone_number()
        return self.contact
    
    def get_email(self):
        self.email = fake.email()
        return self.email
    
    def get_address(self):
        self.address = fake.address()
        return self.address
    
    def get_occupation(self):
        self.occupation = self.get_random_occupation()
        return self.occupation
    
    def get_hobby(self):
        self.hobby = self.get_random_hobby()
        return self.hobby
    
    def get_qualification(self):
        self.qualification = self.get_random_qualification()
        return self.qualification
    
    def get_user_id(self):
        return self.user_id
        
    def get_full_data(self):
        return {    "user_id" : self.get_user_id(),
                    "name" : self.get_name(),
                    "contact" : self.get_contact(),
                    "email" : self.get_email(),
                    "address" : self.get_address(),
                    "occupation" : self.get_occupation(),
                    "hobby" : self.get_hobby(),
                    "qualification" : self.get_qualification()}