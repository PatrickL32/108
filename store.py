

def one_product():
    product={
        "title":"keyboard",
        "price":27.99 
    }

    print(product)
    print(product["title"])
    print(product["price"])


def multiple_products():
    catalog = [
        {"title": "Wireless Mouse", "price": 25.99, "category": "Electronics"},
        {"title": "Yoga Mat", "price": 19.99, "category": "Fitness"},
        {"title": "Coffee Maker", "price": 49.99, "category": "Appliances"},
        {"title": "Desk Lamp", "price": 29.99, "category": "Home Decor"},
        {"title": "Bluetooth Headphones", "price": 89.99, "category": "Electronics"},
        {"title": "Water Bottle", "price": 14.99, "category": "Outdoors"},
        {"title": "Running Shoes", "price": 69.99, "category": "Footwear"},
    ]

    for product in catalog : 
        title= product["title"]
        price= product["price"]

        print(f"{title} ${price}")


    
def start_program():
        print("Hello")
        one_product()
        multiple_products()








start_program()