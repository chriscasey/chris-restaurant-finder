import requests
import json

API_KEY = 'Bearer qlWvJAEpa42CLh0Lz7vBnF-JkIsngtx0mlQSqqf4t1fG5SOXOPOJGOHyGpkV8EbRLovqiyBsd-nGO_UPfQx_B5gErZP89n4pREobk8kCGkR7K1htwoX0L5LZtzcMXHYx'
CUSTOM_API_HEADER = {'Authorization': API_KEY}
BUSINESS_SEARCH_BASE_URL = 'https://api.yelp.com/v3/businesses/search'
SEARCH_LOC = 'Berkeley, CA'
PRICE = "1, 2, 3"
CATEGORIES_ADVENTUROUS = 'categories-adventurous.txt'
CATEGORIES_ALL = 'categories-all.txt'


def find_restaurants(categories):
    payload = {'location': SEARCH_LOC, 'limit': 3, 'sort_by': 'rating', 'open_now': True, 'categories': categories, 'price': PRICE}
    r = requests.get(BUSINESS_SEARCH_BASE_URL, params=payload, headers=CUSTOM_API_HEADER)
    if r.status_code is not 200:
        print r.error
        return
    response_str = r.content
    businesses = generate_yelp_restaurants(json.loads(response_str))
    print businesses


def generate_yelp_restaurants(response_json):
    businesses = []
    for business in response_json['businesses']:
        name = business.get('name', None)
        rating = business.get('rating', None)
        price = business.get('price', None)
        address = business.get('address', None)
        categories = ', '.join([str(c['title']) for c in business['categories']])
        businesses.append(YelpRestaurant(name, rating, price, categories, address))
    return businesses


def enrich_categories():
    categories = []
    with open(CATEGORIES_ADVENTUROUS) as fp:
        line = fp.readline()
        while line:
            categories.append(line.rstrip())
            line = fp.readline()
    return ",".join(categories)


class YelpRestaurant:
    def __init__(self, name, rating, price, categories, address):
        self.name = name
        self.rating = rating
        self.price = price
        self.categories = categories
        self.address = address

    def ___str___(self):
        return self.name

    def __repr__(self):
        return 'YelpRestaurant(name=%s, rating=%s, categories=%s)' % (self.name, self.rating, self.categories)


if __name__ == "__main__":
    categories = enrich_categories()
    restaurants = find_restaurants(categories)
    print restaurants
