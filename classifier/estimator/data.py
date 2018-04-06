TRAIN_URL = "http://<domain name>/<path to csv>/model_training.csv"
TEST_URL = "http://<domain name>/<path to csv>/model_test.csv"

CSV_COLUMN_NAMES = [
    'Attribute1',
    'Attribute2',
    'Attribute3',
    'Attribute4',
    'Labels'
]

# Dummy data
LABELS = [
    "/Arts & Entertainment",
    "/Autos & Vehicles",
    "/Beauty & Fitness",
    "/Books & Literature",
    "/Business & Industrial",
    "/Computers & Electronics",
    "/Finance",
    "/Food & Drink",
    "/Games",
    "/Health",
    "/Hobbies & Leisure",
    "/Home & Garden",
    "/Internet & Telecom",
    "/Jobs & Education",
    "/Law & Government",
    "/News",
    "/Online Communities",
    "/People & Society",
    "/Pets & Animals",
    "/Real Estate",
    "/Reference",
    "/Science",
    "/Shopping",
    "/Sports",
    "/Travel"
]

DICTIONARY = [
    "abstract",
    "abuse",
    "access",
    "accessories",
    "accommodations",
    "accounting",
    "acting",
    "activities",
    "add-ons",
    "admissions",
    "advertising",
    "advocacy",
    "aerospace",
    "affiliate",
    "agents",
    "aging",
    "agricultural",
    "agriculture",
    "aid",
    "aids",
    "air",
    "aircraft",
    "airport",
    "alcohol",
    "alcoholic",
    "allergies",
    "alternative",
    "american",
    "amphibians",
    "animal",
    "animals",
    "animated",
    "animation",
    "anime",
    "antiques",
    "anxiety",
    "apparel",
    "appliances",
    "apps",
    "aquaria",
    "arcade",
    "architecture",
    "art",
    "arthritis",
    "arts",
    "assisted",
    "astronomy",
    "athletic",
    "atmospheric",
    "auctions",
    "audio",
    "auditing",
    "australian",
    "automotive",
    "autos",
    "baked",
    "banking",
    "bank-owned",
    "bankruptcy",
    "bars",
    "baseball",
    "basketball",
    "bath",
    "bathroom",
    "bbq",
    "beaches",
    "beauty",
    "bed",
    "belief",
    "beverages",
    "bicycles",
    "bike",
    "billiards",
    "billing",
    "biographies",
    "biological",
    "biotech",
    "birds",
    "blogging",
    "blues",
    "bmx",
    "board",
    "boating",
    "boats",
    "body",
    "bonds",
    "books",
    "boxing",
    "brainteasers",
    "breakfast",
    "building",
    "bus",
    "business",
    "cable",
    "cad",
    "calculators",
    "calendars",
    "cam",
    "camera",
    "campers",
    "camping",
    "cancer",
    "candy",
    "capital",
    "car",
    "card",
    "cards",
    "care",
    "career",
    "cargo",
    "carpets",
    "cartoons",
    "casino",
    "casual",
    "cats",
    "cd",
    "celebrities",
    "centers",
    "certification",
    "cessation",
    "change",
    "charity",
    "charters",
    "chat",
    "cheerleading",
    "chemicals",
    "chemistry",
    "chess",
    "children",
    "circus",
    "classic",
    "classical",
    "classics",
    "classifieds",
    "classroom",
    "cleaning",
    "climate",
    "clip",
    "clothing",
    "clubs",
    "coaching",
    "coffee",
    "coin-op",
    "collectible",
    "collectibles",
    "collections",
    "college",
    "colleges",
    "coloring",
    "combat",
    "comics",
    "commercial",
    "commercials",
    "commodities",
    "communications",
    "communities",
    "company",
    "comparisons",
    "competitions",
    "components",
    "computer",
    "computers",
    "concerts",
    "conditions",
    "consoles",
    "construction",
    "consulting",
    "consumer",
    "contacts",
    "contests",
    "continuing",
    "control",
    "conventions",
    "cooking",
    "cookware",
    "corporate",
    "cosmetic",
    "cosmetology",
    "costumes",
    "country",
    "coupons",
    "courts",
    "cracking",
    "crafts",
    "credit",
    "cricket",
    "crime",
    "cruises",
    "currencies",
    "curtains",
    "cycling",
    "dance",
    "data",
    "dating",
    "decor",
    "defense",
    "delivery",
    "dental",
    "department",
    "depression",
    "design",
    "designers",
    "desktop",
    "desserts",
    "destinations",
    "development",
    "device",
    "devices",
    "diabetes",
    "dictionaries",
    "die-cast",
    "diets",
    "digital",
    "dining",
    "diningware",
    "directories",
    "discount",
    "discrimination",
    "diseases",
    "disorders",
    "distance",
    "doctors",
    "dogs",
    "dolls",
    "domestic",
    "doors",
    "downloads",
    "drag",
    "drawing",
    "dress-up",
    "drink",
    "drinks",
    "drivers",
    "drives",
    "driving",
    "drones",
    "drug",
    "drugs",
    "dryers",
    "ear",
    "earth",
    "eating",
    "e-books",
    "ecology",
    "e-commerce",
    "economics",
    "editing",
    "education",
    "electrical",
    "electricity",
    "electronic",
    "electronics",
    "email",
    "emergency",
    "emulation",
    "encyclopedias",
    "endocrine",
    "energy",
    "enforcement",
    "engineering",
    "enterprise",
    "entertainment",
    "environment",
    "environmental",
    "equipment",
    "estate",
    "event",
    "events",
    "exchange",
    "exotic",
    "experimental",
    "expos",
    "extreme",
    "eyeglasses",
    "eyewear",
    "face",
    "facial",
    "facilities",
    "family",
    "family-oriented",
    "fan",
    "fantasy",
    "fashion",
    "fast",
    "festivals",
    "fiber",
    "fiction",
    "field",
    "fighting",
    "file",
    "film",
    "finance",
    "financial",
    "finishing",
    "fire",
    "fireplaces",
    "fish",
    "fishing",
    "fitness",
    "flash-based",
    "flooring",
    "flowers",
    "folklore",
    "food",
    "foods",
    "football",
    "footwear",
    "foreclosed",
    "foreign",
    "forestry",
    "formal",
    "formats",
    "forms",
    "foundations",
    "fragrances",
    "freight",
    "fueling",
    "fun",
    "funny",
    "furnishings",
    "furniture",
    "futures",
    "galleries",
    "gambling",
    "game",
    "games",
    "garden",
    "gardening",
    "gardens",
    "gas",
    "general",
    "genetic",
    "geographic",
    "geology",
    "geriatrics",
    "gifs",
    "gifts",
    "global",
    "golf",
    "goodies",
    "goods",
    "gossip",
    "government",
    "gps",
    "grains",
    "grants",
    "grants",
    "green",
    "greetings",
    "grilling",
    "grocery",
    "guides",
    "gymnastics",
    "hacking",
    "hair",
    "hardware",
    "headwear",
    "health",
    "heart",
    "heavy",
    "hiking",
    "hip-hop",
    "history",
    "hiv",
    "hobbies",
    "hockey",
    "holidays",
    "home",
    "homeschooling",
    "horses",
    "hospitality",
    "hospitals",
    "hosting",
    "hotels",
    "house",
    "human",
    "humanities",
    "humor",
    "hunger",
    "hvac",
    "hybrid",
    "hygiene",
    "hypertension",
    "ice",
    "identity",
    "image",
    "immigration",
    "improvement",
    "individual",
    "industrial",
    "industry",
    "infectious",
    "instant",
    "institutions",
    "instruction",
    "insurance",
    "interests",
    "interior",
    "internet",
    "investigations",
    "investing",
    "invoicing",
    "islands",
    "issues",
    "items",
    "java",
    "jazz",
    "job",
    "jobs",
    "judiciary",
    "juice",
    "justice",
    "kids",
    "kitchen",
    "labor",
    "lamps",
    "land",
    "landscaping",
    "language",
    "laptops",
    "laundry",
    "law",
    "laws",
    "learning",
    "legal",
    "leisure",
    "lending",
    "liberties",
    "libraries",
    "licensing",
    "lighting",
    "listings",
    "literary",
    "literature",
    "livestock",
    "living",
    "loans",
    "logistics",
    "long",
    "loss",
    "lots",
    "lottery",
    "luxury",
    "machinery",
    "magic",
    "mail",
    "maintenance",
    "major",
    "make-up",
    "management",
    "manga",
    "manufacturing",
    "maps",
    "maritime",
    "marketing",
    "markets",
    "marriage",
    "martial",
    "mass",
    "massage",
    "massively",
    "materials",
    "mathematics",
    "matrimonial",
    "meat",
    "media",
    "medical",
    "medications",
    "memorabilia",
    "men",
    "mental",
    "merchants",
    "merit",
    "messaging",
    "metals",
    "military",
    "miniatures",
    "mining",
    "mlm",
    "mobile",
    "model",
    "modeling",
    "monitoring",
    "motor",
    "motorcycles",
    "mountain",
    "movie",
    "moving",
    "multimedia",
    "multiplayer",
    "museums",
    "music",
    "myth",
    "nail",
    "navigation",
    "network",
    "networking",
    "networks",
    "neurological",
    "neuroscience",
    "news",
    "nightlife",
    "nonwovens",
    "nose",
    "notebooks",
    "nursery",
    "nursing",
    "nutrition",
    "obesity",
    "occasions",
    "occult",
    "occupational",
    "offbeat",
    "offers",
    "office",
    "offices",
    "off-road",
    "oil",
    "olympics",
    "online",
    "opera",
    "operating",
    "operations",
    "opportunities",
    "oral",
    "organizations",
    "outdoors",
    "package",
    "packaging",
    "pageants",
    "pain",
    "paintball",
    "painting",
    "paranormal",
    "parking",
    "parks",
    "parts",
    "pasta",
    "patio",
    "pension",
    "people",
    "performance-enhancing",
    "performing",
    "perfumes",
    "peripherals",
    "personal",
    "personals",
    "pest",
    "pet",
    "pets",
    "pharmaceuticals",
    "pharmacy",
    "philanthropy",
    "philosophy",
    "phones",
    "photo",
    "photographic",
    "physical",
    "physics",
    "pictures",
    "pizzerias",
    "planning",
    "plans",
    "plastics",
    "playroom",
    "plumbing",
    "poetry",
    "poker",
    "political",
    "politics",
    "polymers",
    "pop",
    "portfolios",
    "poverty",
    "power",
    "precious",
    "preparation",
    "presentations",
    "price",
    "prices",
    "primary",
    "printing",
    "prizes",
    "procedures",
    "product",
    "productivity",
    "products",
    "professionals",
    "programming",
    "programs",
    "properties",
    "protection",
    "protocols",
    "providers",
    "psychology",
    "public",
    "publishing",
    "puzzles",
    "quotations",
    "rabbits",
    "racing",
    "racquet",
    "radio",
    "rail",
    "railroads",
    "rating",
    "rc",
    "real",
    "recipes",
    "recording",
    "records",
    "reference",
    "regional",
    "registration",
    "relations",
    "relationships",
    "religion",
    "religious",
    "relocation",
    "remote",
    "removal",
    "renewable",
    "rental",
    "rentals",
    "repair",
    "reporting",
    "reproductive",
    "reptiles",
    "research",
    "reservations",
    "residential",
    "resorts",
    "resources",
    "respiratory",
    "restaurant",
    "restaurants",
    "restricted",
    "resumes",
    "retail",
    "retailers",
    "retirement",
    "reviews",
    "ride-on",
    "rights",
    "robotics",
    "rock",
    "rodents",
    "roleplaying",
    "room",
    "rugby",
    "rugs",
    "rvs",
    "safety",
    "sales",
    "sandbox",
    "satellite",
    "saunas",
    "scandals",
    "scholarships",
    "schooling",
    "science",
    "sciences",
    "scientific",
    "seafood",
    "seasonal",
    "secondary",
    "security",
    "seniors",
    "service",
    "services",
    "sharing",
    "shelving",
    "shooter",
    "shopping",
    "short-term",
    "shows",
    "showtimes",
    "silly",
    "simulation",
    "sites",
    "skate",
    "skating",
    "ski",
    "skiing",
    "skin",
    "skins",
    "sleep",
    "small",
    "smoking",
    "snack",
    "snowboarding",
    "soccer",
    "social",
    "society",
    "soft",
    "software",
    "soundtracks",
    "soups",
    "space",
    "spas",
    "special",
    "specialty",
    "sporting",
    "sports",
    "standardized",
    "statistics",
    "stays",
    "steroids",
    "stews",
    "stocks",
    "storage",
    "stores",
    "stoves",
    "strategy",
    "streams",
    "street",
    "stress",
    "study",
    "stuffed",
    "style",
    "subcultures",
    "substance",
    "supplements",
    "supplies",
    "surf",
    "surfing",
    "surgery",
    "surveys",
    "suvs",
    "sweets",
    "swim",
    "swimming",
    "swimwear",
    "systems",
    "table",
    "tabloid",
    "tax",
    "taxi",
    "tea",
    "teaching",
    "team",
    "technology",
    "teen",
    "teens",
    "telecom",
    "templates",
    "term",
    "testing",
    "tests",
    "text",
    "textile",
    "textiles",
    "theater",
    "theme",
    "themes",
    "therapy",
    "throat",
    "time",
    "timeshares",
    "tobacco",
    "toiletries",
    "tools",
    "tourist",
    "toy",
    "toys",
    "track",
    "trade",
    "trading",
    "trailers",
    "training",
    "trains",
    "transport",
    "transportation",
    "travel",
    "treatment",
    "treatments",
    "trivia",
    "troubled",
    "trucking",
    "trucks",
    "tv",
    "undergarments",
    "universities",
    "unwanted",
    "urban",
    "used",
    "utilities",
    "vacation",
    "vehicle",
    "vehicles",
    "venture",
    "veterinarians",
    "video",
    "videos",
    "virtual",
    "visa",
    "vision",
    "visual",
    "vitamins",
    "vocational",
    "voice",
    "volleyball",
    "vpn",
    "wagons",
    "wallpapers",
    "wargaming",
    "warming",
    "washers",
    "water",
    "watercraft",
    "wear",
    "weather",
    "web",
    "weddings",
    "weight",
    "wildlife",
    "window",
    "windows",
    "winter",
    "wireless",
    "women",
    "word",
    "work",
    "world",
    "worlds",
    "wrestling",
    "writers",
    "writing",
    "yard",
    "youth"
]
