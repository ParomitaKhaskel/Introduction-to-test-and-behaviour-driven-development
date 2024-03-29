from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from your_project.models import Product  # Import your SQLAlchemy Product model

def load_products(data):
    # Connect to the database
    engine = create_engine('sqlite:///your_database.db')  # Change this to your database URL
    Session = sessionmaker(bind=engine)
    session = Session()

    # Load products into the database
    for product_data in data:
        product = Product(**product_data)
        session.add(product)

    session.commit()
    session.close()

if __name__ == "__main__":
    # Sample data (you can replace this with your actual data)
    products_data = [
        {'name': 'Product 1', 'price': 10.99, 'description': 'This is product 1'},
        {'name': 'Product 2', 'price': 20.49, 'description': 'This is product 2'},
        # Add more products as needed
    ]

    # Load products into the database
    load_products(products_data)
