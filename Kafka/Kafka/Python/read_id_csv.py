# from pyravendb.store import document_store
import csv

csv_file_path = 'LazData.csv'

# Define the Customer class
class Product:
    def __init__(self, product_id, name):
        self.product_id = product_id
        self.name = name

    
def store_data():
    product_ids = []  # List to store product IDs
    names = []
    with open(csv_file_path, 'r', encoding='utf-8') as file:
        # Create a CSV DictReader object
        csv_reader = csv.DictReader(file)
        
        # with store.open_session() as session:
        for row in csv_reader:
            product_id = row['p_cate']
            name = row['p_brand']
            # brand = row['p_brand']

            product = Product(product_id, name)
            
            product_ids.append(product_id)    
            names.append(name)
        print(f"Successfully store product records.")
    for pid in product_ids:
        print(pid)
    print(len(product_ids))
    print(len(names))
    return product_ids

if __name__ == "__main__":
    store_data()
