from pyravendb.store import document_store
from Entity import server_url, database_name, certificate, Product
import argparse

store = document_store.DocumentStore(urls=[server_url], database=database_name, certificate=certificate)
store.initialize()

def query(category_id):
    with store.open_session() as session:
        products = list(session.query(object_type=Product).where_equals(field_name="category_id",value=category_id).order_by_descending(field_name="product_average_rating"))
        
        if len(products) == 0:
            with open('ProductReview.txt', "w", encoding='utf-8') as file:
                file.write(f"???\n")
                return
            
        with open('ProductReview.txt', "w", encoding='utf-8') as file:
            file.write(f"{products[0].category}\n")
            for product in products:
                file.write(f"{product.name}#{product.total_product_reviews}#{product.product_average_rating}\n")
            print("File write operation successful.")
            
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Query product reviews")
    parser.add_argument("category_id", type=str, help="Category ID")
    args = parser.parse_args()
    
    query(args.category_id)