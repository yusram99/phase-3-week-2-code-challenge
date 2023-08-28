from restaurants import Restaurant
from customer import Customer, Review

# Create instances and perform tests
restaurant1 = Restaurant("Restaurant A")
restaurant2 = Restaurant("Restaurant B")

customer1 = Customer("John", "Doe")
customer2 = Customer("Jane", "Smith")

customer1.add_review(restaurant1, 4)
customer1.add_review(restaurant2, 5)
customer2.add_review(restaurant1, 3)

# Test methods
print("Customer 1 reviews:", customer1.reviews)
print("Customer 2 restaurants:", customer2.restaurants())  
print("Average rating for Restaurant A:", restaurant1.average_star_rating())  
print("Customers who reviewed Restaurant A:", [customer.full_name() for customer in restaurant1.customers()])  
print("Finding customer by name 'John Doe':", Customer.find_by_name("John Doe").full_name())  
print("Finding all customers with given name 'John':", [customer.full_name() for customer in Customer.find_all_by_given_name("John")])  


