# from pyravendb.store import document_store
import csv

# Configuration
server_url = "https://a.bigdataapp.ravendb.community"
database_name = "ECommerce"
a = {"pfx":"E:\RavenDB-6.0.101-windows-x64\Server\cluster.server.certificate.bigdataapp.pfx","password":""}

# Create a document store and initialize it with certificate
# store = document_store.DocumentStore(urls=[server_url], database=database_name, certificate=a)
# store.initialize()

csv_file_path = "LazData.csv"

# Define the Customer class
class Product:
    def __init__(self, name, brand, category, image, mall_certification, total_product_reviews, price, product_rate1star, product_rate2star, product_rate3star, product_rate4star, product_rate5star, product_average_rating, seller_name, seller_rating, seller_response_rate, seller_ship_ontime):
        self.name = name
        self.brand = brand
        self.category = category
        self.image = image
        self.mall_certification = mall_certification
        self.total_product_reviews = total_product_reviews
        self.price = price
        self.product_rate1star = product_rate1star
        self.product_rate2star = product_rate2star
        self.product_rate3star = product_rate3star
        self.product_rate4star = product_rate4star
        self.product_rate5star = product_rate5star
        self.product_average_rating = product_average_rating
        self.seller_name = seller_name
        self.seller_rating = seller_rating
        self.seller_response_rate = seller_response_rate
        self.seller_ship_ontime = seller_ship_ontime
    
def store_data():
    with open(csv_file_path, 'r', encoding='utf-8') as file:
        # Create a CSV DictReader object
        csv_reader = csv.DictReader(file)
        
        # with store.open_session() as session:
        for row in csv_reader:
            name = row['p_name']
            brand = row['p_brand']
            category = row['p_cate']
            image = row['p_image']
            mall_certification = row['p_mall']
            total_product_reviews = row['p_number_reviews']
            price = row['p_price']
            product_rate1star = row['p_rate1star']
            product_rate2star = row['p_rate2star']
            product_rate3star = row['p_rate3star']
            product_rate4star = row['p_rate4star']
            product_rate5star = row['p_rate5star']
            product_average_rating = row['p_rating']
            seller_name = row['s_name']
            seller_rating = row['s_rating']
            seller_response_rate = row['s_response_rate']
            seller_ship_ontime = row['s_ship_ontime']
            product = Product(name, brand, category, image, mall_certification, total_product_reviews, price, product_rate1star, product_rate2star, product_rate3star, product_rate4star, product_rate5star, product_average_rating, seller_name, seller_rating, seller_response_rate, seller_ship_ontime)
            print(category)
            # session.store(product)
                
            # session.save_changes()
            
        print(f"Successfully store product records.")
    

if __name__ == "__main__":
    store_data()
