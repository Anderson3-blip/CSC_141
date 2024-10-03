favorite_places = {
    'eric' : ['bear mountain', 'death valley', 'san fransico'],
    'brandon' : ['iceland', 'poland'],
    'johns' : ['new york','philadelphia']
    }


for name, places in favorite_places.items():
    print(f"\n{name.title()} likes the following places:")
    for place in places:
        print(f"-{place.title()}")