# Dictionary for favorite places
favorite_places = {
    "John": ["Central Park", "Times Square", "Empire State Building"],
    "Samantha": ["Golden Gate Bridge", "Fisherman's Wharf"],
    "Tom": ["Grand Canyon", "Yellowstone National Park"],
}

# Looping through the dictionary
for name, place in favorite_places.items():
    print(name + ', here are your favorite places:')
    for place in place:
        print(place)
        
