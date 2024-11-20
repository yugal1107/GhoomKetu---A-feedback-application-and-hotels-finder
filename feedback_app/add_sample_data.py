from places.models import Place, Hotel

# Sample data for hotels in Gwalior
sample_hotels = [
    {"name": "Hotel Landmark", "city": "Gwalior", "state": "Madhya Pradesh", "description": "A luxurious hotel with modern amenities.", "price": 4500.00},
    {"name": "Hotel Grace", "city": "Gwalior", "state": "Madhya Pradesh", "description": "A comfortable hotel with excellent service.", "price": 3500.00},
    {"name": "Hotel Central Park", "city": "Gwalior", "state": "Madhya Pradesh", "description": "A centrally located hotel with great facilities.", "price": 4000.00},
    {"name": "Hotel Shelter", "city": "Gwalior", "state": "Madhya Pradesh", "description": "A budget-friendly hotel with clean rooms.", "price": 2500.00},
    {"name": "Hotel Gwalior Regency", "city": "Gwalior", "state": "Madhya Pradesh", "description": "A premium hotel with top-notch amenities.", "price": 5000.00},
    {"name": "Hotel Suruchi", "city": "Gwalior", "state": "Madhya Pradesh", "description": "A cozy hotel with friendly staff.", "price": 3000.00},
    {"name": "Hotel Sunbeam", "city": "Gwalior", "state": "Madhya Pradesh", "description": "A modern hotel with excellent facilities.", "price": 4200.00},
    {"name": "Hotel Adityaz", "city": "Gwalior", "state": "Madhya Pradesh", "description": "A stylish hotel with great service.", "price": 3800.00},
    {"name": "Hotel Tansen Residency", "city": "Gwalior", "state": "Madhya Pradesh", "description": "A heritage hotel with beautiful architecture.", "price": 4700.00},
    {"name": "Hotel Royal Inn", "city": "Gwalior", "state": "Madhya Pradesh", "description": "A royal hotel with luxurious rooms.", "price": 5200.00},
]

# Sample data for places in Madhya Pradesh
sample_places = [
    {"name": "Khajuraho Temples", "city": "Khajuraho", "state": "Madhya Pradesh", "description": "Famous for their stunning architecture and erotic sculptures.", "price": 200.00},
    {"name": "Sanchi Stupa", "city": "Sanchi", "state": "Madhya Pradesh", "description": "A Buddhist complex famous for its Great Stupa.", "price": 100.00},
    {"name": "Bhimbetka Rock Shelters", "city": "Raisen", "state": "Madhya Pradesh", "description": "An archaeological site with prehistoric cave paintings.", "price": 150.00},
    {"name": "Kanha National Park", "city": "Mandla", "state": "Madhya Pradesh", "description": "A famous tiger reserve and wildlife sanctuary.", "price": 500.00},
    {"name": "Bandhavgarh National Park", "city": "Umaria", "state": "Madhya Pradesh", "description": "Known for its high density of Bengal tigers.", "price": 600.00},
    {"name": "Ujjain Mahakaleshwar Temple", "city": "Ujjain", "state": "Madhya Pradesh", "description": "One of the twelve Jyotirlinga shrines dedicated to Lord Shiva.", "price": 50.00},
    {"name": "Gwalior Fort", "city": "Gwalior", "state": "Madhya Pradesh", "description": "A historic fort with stunning architecture and history.", "price": 300.00},
    {"name": "Orchha Fort Complex", "city": "Orchha", "state": "Madhya Pradesh", "description": "A beautiful fort complex with palaces and temples.", "price": 250.00},
    {"name": "Pachmarhi", "city": "Pachmarhi", "state": "Madhya Pradesh", "description": "A hill station known for its natural beauty and waterfalls.", "price": 0.00},
    {"name": "Bhedaghat", "city": "Jabalpur", "state": "Madhya Pradesh", "description": "Famous for its marble rocks and Dhuandhar Falls.", "price": 100.00},
]

# Add hotels to the database
for hotel in sample_hotels:
    Hotel.objects.create(
        name=hotel["name"],
        city=hotel["city"],
        state=hotel["state"],
        description=hotel["description"],
        price=hotel["price"]
    )


print("Sample data added successfully.")