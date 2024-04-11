from pyravendb.store import document_store
from Entity import server_url, database_name, certificate, Seller
import argparse

store = document_store.DocumentStore(urls=[server_url], database=database_name, certificate=certificate)
store.initialize()

def query(seller_id):
    with store.open_session() as session:
        seller = session.load(seller_id, object_type=Seller)
        
        if seller:
            try:
                with open('SellerReviews.txt', "w", encoding='utf-8') as file:
                    file.write(f"{seller.seller_name}#{seller.seller_rating}#{seller.seller_response_rate}#{seller.seller_ship_ontime}\n")
                    
                print("File write operation successful.")
            except Exception as e:
                print(f"An error occurred: {e}")
        else:
            with open('SellerReviews.txt', "w", encoding='utf-8') as file:
                file.write(f"???\n")

if __name__ == "__main__":
    # Parse command-line arguments
    parser = argparse.ArgumentParser(description="Query Seller information")
    parser.add_argument("seller_id", type=str, help="Seller ID")
    args = parser.parse_args()
    
    query(args.seller_id)