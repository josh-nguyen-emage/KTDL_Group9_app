from pyravendb.store import document_store
from Entity import server_url, database_name, certificate, Product, Category, Customer
from datetime import datetime
import argparse

store = document_store.DocumentStore(urls=[server_url], database=database_name, certificate=certificate)
store.initialize()

def query(customer_id):
    with store.open_session() as session:
        customer = session.load(customer_id, object_type=Customer)        
        if customer:
            recent_interesteds = customer.recent_interested.split(',')
            products = []
            for recent_interested in recent_interesteds:
                products.extend(list(session.query(collection_name="Products", object_type=Product).where_equals("category_id", recent_interested).order_by_descending("product_average_rating").take(20)))
            
            if len(products) == 0:
                with open('ProductSuggestions.txt', "w", encoding='utf-8') as file:
                    file.write(f"???\n")
                    return
                
            try:
                with open('ProductSuggestions.txt', "w", encoding='utf-8') as file:
                    file.write(f"{customer.full_name}\n")
                    
                    stt = 1
                    for product in products:
                        file.write(f"{stt}#{product.name}#{product.brand}#{product.category}#{product.product_average_rating}\n")
                        stt += 1
                    
                print("File write operation successful.")
            except Exception as e:
                print(f"An error occurred: {e}")
        else:
            with open('ProductSuggestions.txt', "w", encoding='utf-8') as file:
                file.write(f"???\n") 

if __name__ == "__main__":
    # Parse command-line arguments
    parser = argparse.ArgumentParser(description="Product suggestion")
    parser.add_argument("customer_id", type=str, help="Customer Id")
    args = parser.parse_args()
    
    query(args.customer_id)