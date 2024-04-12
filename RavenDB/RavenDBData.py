from pyravendb.store import document_store
from Entity import Product, Seller, Category, Customer, Inventory, Sale, Promotion
from datetime import datetime
import random
import csv

# Configuration
server_url = "https://a.bigdataapp.ravendb.community"
database_name = "ECommerce"
a = {"pfx":"E:\RavenDB-6.0.101-windows-x64\Server\cluster.server.certificate.bigdataapp.pfx","password":""}

# Create a document store and initialize it with certificate
store = document_store.DocumentStore(urls=[server_url], database=database_name, certificate=a)
store.initialize()

category_ids = []

def store_data(records):
    with store.open_session() as session:
        for record in records:
            session.store(record)
            
        session.save_changes()
        
def read_products_data():
    with open("LazData.csv", 'r', encoding='utf-8') as file:
        # Create a CSV DictReader object
        csv_reader = csv.DictReader(file)
        
        products = []
        categories = []
        sellers_dict = {}
        seller_names = {}
        category_dict = {}
        
        for row in csv_reader:
            name = row['p_name']
            brand = row['p_brand']
            category = row['p_cate']
            image = row['p_image']
            mall_certification = row['p_mall']
            total_product_reviews = row['p_number_reviews']
            price = row['p_price']
            product_rate1star = int(row['p_rate1star'])
            product_rate2star = int(row['p_rate2star'])
            product_rate3star = int(row['p_rate3star'])
            product_rate4star = int(row['p_rate4star'])
            product_rate5star = int(row['p_rate5star'])
            product_average_rating = round(float(product_rate1star + product_rate2star * 2 + product_rate3star * 3 + product_rate4star * 4 + product_rate5star * 5) / (product_rate1star + product_rate2star + product_rate3star + product_rate4star + product_rate5star),1) if (product_rate1star + product_rate2star + product_rate3star + product_rate4star + product_rate5star) != 0 else 0
            seller_name = row['s_name']
            seller_rating = 0
            if row['s_rating'] != '---':
                seller_rating = int(row['s_rating'])
            seller_response_rate = 0
            if row['s_response_rate'] != '---':
                seller_response_rate = int(row['s_response_rate'])
            seller_ship_ontime = 0
            if row['s_ship_ontime'] != '---':
                seller_ship_ontime = int(row['s_ship_ontime'])
            
            if seller_name not in seller_names.keys():
                i = len(seller_names) + 1
                seller_id = f"sellers/{i}-A"
                seller_names[seller_name] = seller_id
                num_of_rating = 0 if seller_rating == 0 else 1
                num_of_response_rate = 0 if seller_response_rate == 0 else 1
                num_of_ship_ontime = 0 if seller_ship_ontime == 0 else 1
                
                sellers_dict[seller_name] = Seller(seller_id, seller_name, seller_rating, seller_response_rate, seller_ship_ontime, num_of_rating, num_of_response_rate, num_of_ship_ontime)
            else:
                if seller_rating != 0:
                    sellers_dict[seller_name].seller_rating += seller_rating
                    sellers_dict[seller_name].num_of_rating += 1
                    
                if seller_response_rate != 0:
                    sellers_dict[seller_name].seller_response_rate += seller_response_rate
                    sellers_dict[seller_name].num_of_response_rate += 1
                    
                if seller_ship_ontime != 0:
                    sellers_dict[seller_name].seller_ship_ontime += seller_ship_ontime
                    sellers_dict[seller_name].num_of_ship_ontime += 1
 
            if category not in category_dict.keys():
                i = len(category_dict) + 1
                category_id = f"categories/{i}-A"
                category_ids.append(category_id)
                category_dict[category] = category_id
                categories.append(Category(category_id, category))
            
            product = Product(None, name, brand, category_dict[category], category, image, mall_certification, int(total_product_reviews), float(price), product_rate1star, product_rate2star, product_rate3star, product_rate4star, product_rate5star, product_average_rating, seller_name, seller_names[seller_name])
            products.append(product)
        
        for seller in sellers_dict.values():
            if seller.num_of_rating != 0:
                seller.seller_rating = round(seller.seller_rating/seller.num_of_rating)
            if seller.num_of_response_rate != 0:
                seller.seller_response_rate = round(seller.seller_response_rate/seller.num_of_response_rate)
            if seller.num_of_ship_ontime != 0:
                seller.seller_ship_ontime = round(seller.seller_ship_ontime/seller.num_of_ship_ontime)
        
        return products, sellers_dict.values(), categories
    
def create_products_and_categories():
    products, sellers, categories = read_products_data()
    
    store_data(sellers)
    print(f"Successfully stored seller records.")
    store_data(categories)
    print(f"Successfully stored category records.")
    store_data(products)
    print(f"Successfully stored product records.")

def create_customers():
    with open("customers.csv", 'r', encoding='utf-8') as file:
        # Create a CSV DictReader object
        csv_reader = csv.DictReader(file)
        
        with store.open_session() as session:
            for row in csv_reader:
                fullname = row['fullname']
                birthYear = row['birthYear']
                gender = row['gender']
                province = row['province']
                recent_interested = random.choice(category_ids)
                customer = Customer(None, fullname,int(birthYear), gender, province, recent_interested)
                session.store(customer)
                
            session.save_changes()
            
        print(f"Successfully stored customer records.")
        
def create_inventories():
    with open("inventory_in.csv", 'r', encoding='utf-8') as file:
        # Create a CSV DictReader object
        csv_reader = csv.DictReader(file)
        
        with store.open_session() as session:
            for row in csv_reader:
                date = row['date']
                product_id = row['product_id']
                product_name = row['product_name']
                quantity = row['quantity']
                inventory = Inventory(None, datetime.strptime(date, "%Y-%m-%d"), product_id, product_name, int(quantity))
                session.store(inventory)
                
            session.save_changes()
            
        print(f"Successfully stored inventory records.")
        
def create_sales():
    with open("sales.csv", 'r', encoding='utf-8') as file:
        # Create a CSV DictReader object
        csv_reader = csv.DictReader(file)
        
        with store.open_session() as session:
            for row in csv_reader:
                date = row['date']
                product_id = row['product_id']
                product_name = row['product_name']
                quantity = row['quantity']
                sale = Sale(None, datetime.strptime(date, "%Y-%m-%d"), product_id, product_name, int(quantity))
                session.store(sale)
                
            session.save_changes()
            
        print(f"Successfully stored sale records.")

def create_promotions():
    with open("promotions.csv", 'r', encoding='utf-8') as file:
        # Create a CSV DictReader object
        csv_reader = csv.DictReader(file)
        
        with store.open_session() as session:
            for row in csv_reader:
                name = row['name']
                from_date = row['from_date']
                to_date = row['to_date']
                promotion = Promotion(None, name, datetime.strptime(from_date, "%Y-%m-%d"), datetime.strptime(to_date, "%Y-%m-%d"))
                session.store(promotion)
                
            session.save_changes()
            
        print(f"Successfully stored promotion records.")

if __name__ == "__main__":
    create_products_and_categories()
    create_customers()
    create_inventories()
    create_sales()
    create_promotions()
