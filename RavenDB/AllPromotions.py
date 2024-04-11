from pyravendb.store import document_store
from Entity import server_url, database_name, certificate, Promotion

store = document_store.DocumentStore(urls=[server_url], database=database_name, certificate=certificate)
store.initialize()

def query():
    with store.open_session() as session:
        promotions = list(session.query(collection_name="Promotions", object_type=Promotion))
        if len(promotions) == 0:
            with open('AllPromotions.txt', "w", encoding='utf-8') as file:
                file.write(f"???\n")
            return
        
        try:
            with open('AllPromotions.txt', "w", encoding='utf-8') as file:
                for promotion in promotions:
                    file.write(f"{promotion.Id}#{promotion.name}\n")
                
            print("File write operation successful.")
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    query()