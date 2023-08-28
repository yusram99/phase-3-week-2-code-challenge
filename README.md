# phase-3-week-2-code-challenge
# Restaurant Reviews

This project simulates a Yelp-style domain with three models: `Restaurant`, `Customer`, and `Review`. These models establish relationships between restaurants, customers, and reviews. This README provides an overview of the project's structure, functionality, and usage instructions.

# Introduction
This project showcases how to model a restaurant review system using object-oriented programming principles. It demonstrates how to create and interact with instances of `Restaurant`, `Customer`, and `Review` classes.

# Files
The project consists of the following files:
- `customer.py`: Contains the `Customer` class definition.
- `restaurant.py`: Contains the `Restaurant` class definition.
- `review.py`: Contains the `Review` class definition.
- `main.py`: Main script to create instances and test methods.

# Usage
1. Ensure you have Python installed on your system.
2. Clone this repository or download the files.
3. Navigate to the project directory in your terminal.
4. Run the main script using: `python main.py`.
5. Observe the printed output to see the functionality in action.

# Methods
The classes and their methods are structured as follows:

# Customer Class
- `__init__(given_name, family_name)`: Initialize a customer instance.
- `given_name()`: Get the customer's given name.
- `family_name()`: Get the customer's family name.
- `full_name()`: Get the customer's full name.
- `add_review(restaurant, rating)`: Add a review for a restaurant.
- `restaurants()`: Get unique restaurants reviewed by the customer.
- `num_reviews()`: Get the total number of reviews authored.
- `find_by_name(name)`: Find a customer by full name.
- `find_all_by_given_name(name)`: Find all customers with a given name.

# Restaurant Class
- `__init__(name)`: Initialize a restaurant instance.
- `name()`: Get the restaurant's name.
- `reviews()`: Get all reviews for the restaurant.
- `customers()`: Get unique customers who reviewed the restaurant.
- `average_star_rating()`: Get the average star rating for the restaurant.

# Review Class
- `__init__(customer, restaurant, rating)`: Initialize a review instance.
- `customer()`: Get the customer object for the review.
- `restaurant()`: Get
