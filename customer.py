from review import Review
from restaurants import Restaurant

class Customer:
    all_customers = []

    def __init__(self, given_name, family_name):
        self._given_name = given_name
        self._family_name = family_name
        self.reviews = []
        self.__class__.all_customers.append(self)

    def given_name(self):
        return self._given_name

    def family_name(self):
        return self._family_name

    def full_name(self):
        return f"{self._given_name} {self._family_name}"

    def add_review(self, restaurant, rating):
        review = Review(self, restaurant, rating)
        self.reviews.append(review)
        restaurant.reviews.append(review)


    def restaurants(self):
        reviewed_restaurants = set()
        for review in self.reviews:
            reviewed_restaurants.add(review.restaurant())
        return list(reviewed_restaurants)

    def add_review(self, restaurant, rating):
        review = Review(self, restaurant, rating)
        self.reviews.append(review)
        restaurant.reviews.append(review)

    def num_reviews(self):
        return len(self.reviews)

    @classmethod
    def find_by_name(cls, name):
        for customer in cls.all_customers:
            if customer.full_name() == name:
                return customer
        return None

    @classmethod
    def find_all_by_given_name(cls, name):
        matching_customers = []
        for customer in cls.all_customers:
            if customer.given_name() == name:
                matching_customers.append(customer)
        return matching_customers
