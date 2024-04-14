from datetime import datetime
from pyravendb.store import document_store
from dateutil.parser import parse
from Entity import server_url, database_name, certificate, Product, Seller, Customer, Sale, Inventory

# store = document_store.DocumentStore(urls=[server_url], database=database_name, certificate=certificate)
# store.initialize()

characters_to_remove = ['"', '[', ']']

def handle_raw_message(raw_message):
    for char in characters_to_remove:
        raw_message = raw_message.replace(char, '')
    return raw_message

def update_product_sale(raw_message):
    print(f"Ready to update Sale.")
    with document_store.DocumentStore(urls=[server_url], database=database_name, certificate=certificate) as store:
        store.initialize()
        message = handle_raw_message(raw_message)
        product_id, transaction_id, quantity, date_str = message.split(', ')
        with store.open_session() as session:
            inventories = list(session.query(object_type=Inventory).where_equals(field_name="product_id", value=product_id))
            if len(inventories) == 0:
                return
            
            total_inventories = sum(int(inventory.quantity) for inventory in inventories)        
            sales = list(session.query(object_type=Sale).where_equals(field_name="product_id", value=product_id))        
            total_sales = sum(int(sale.quantity) for sale in sales)
            remain = total_inventories - total_sales
            date = datetime.strptime(date_str, "%Y-%m-%d").date()
            for sale in sales:
                sale_date = parse(sale.date).date()
                if sale_date == date:
                    updated_sale = session.load(sale.Id, object_type=Sale)
                    if updated_sale:
                        updated_sale.quantity = int(quantity) if remain >= int(quantity) else remain
                        session.save_changes()
                        print(f"Sales are updated successfully.")
                        return
                    
            product = session.load(product_id, object_type=Product)
            if product:
                sale = Sale(None, datetime.strptime(date_str, "%Y-%m-%d"), product_id, product.name, int(quantity) if remain >= int(quantity) else remain)
                session.store(sale)
                
            session.save_changes()
            print(f"Sales are updated successfully.")
        

def update_customer_recent_interested(raw_message):
    with document_store.DocumentStore(urls=[server_url], database=database_name, certificate=certificate) as store:
        store.initialize()
        message = handle_raw_message(raw_message)
        customer_id, category_id = message.split(', ')
        with store.open_session() as session:
            customer = session.load(customer_id, object_type=Customer)
            
            if customer:
                recent_interesteds = customer.recent_interested.split(',')
                
                if category_id in recent_interesteds:
                    index = recent_interesteds.index(category_id)
                    recent_interesteds.pop(index)
                    recent_interesteds = [category_id] + recent_interesteds
                else:
                    recent_interesteds = [category_id] + recent_interesteds
                    if len(recent_interesteds) > 3:
                        recent_interesteds.pop()
                    
                customer.recent_interested = ','.join(recent_interesteds)
                session.save_changes()
                
                print(f"Customer {customer_id} updated successfully.")
            else:
                print("Customer not found for update.")

def update_product_review(raw_message):
    with document_store.DocumentStore(urls=[server_url], database=database_name, certificate=certificate) as store:
        store.initialize()
        message = handle_raw_message(raw_message)
        product_id, point = message.split(', ')
        with store.open_session() as session:
            product = session.load(product_id, object_type=Product)
            if product:
                if point == '1':
                    product.product_rate1star = int(product.product_rate1star) + 1
                elif point == '2':
                    product.product_rate2star = int(product.product_rate2star) + 1
                elif point == '3':
                    product.product_rate3star = int(product.product_rate3star) + 1
                elif point == '4':
                    product.product_rate4star = int(product.product_rate4star) + 1
                elif point == '5':
                    product.product_rate5star = int(product.product_rate5star) + 1
                    
                product.product_average_rating = round(float(product.product_rate1star + product.product_rate2star * 2 + product.product_rate3star * 3 + product.product_rate4star * 4 + product.product_rate5star * 5) / (product.product_rate1star + product.product_rate2star + product.product_rate3star + product.product_rate4star + product.product_rate5star),1) if (product.product_rate1star + product.product_rate2star + product.product_rate3star + product.product_rate4star + product.product_rate5star) != 0 else 0
                
                session.save_changes()
                print(f"Product {product_id} updated successfully.")
            else:
                print("Product not found for update.")
            
def update_seller_review(raw_message):
    with document_store.DocumentStore(urls=[server_url], database=database_name, certificate=certificate) as store:
        store.initialize()
        message = handle_raw_message(raw_message)
        seller_id, seller_rating, seller_response_rate, seller_ship_ontime = message.split(', ')
        with store.open_session() as session:
            seller = session.load(seller_id, object_type=Seller)
            if seller:
                seller.seller_rating = round(((int(seller.seller_rating) * int(seller.num_of_rating)) + int(seller_rating)) / (int(seller.num_of_rating) + 1))
                seller.num_of_rating = int(seller.num_of_rating) + 1
                
                seller.seller_response_rate = round(((int(seller.seller_response_rate) * int(seller.num_of_response_rate)) + int(seller_response_rate)) / (int(seller.num_of_response_rate) + 1))
                seller.num_of_response_rate = int(seller.num_of_response_rate) + 1
                
                seller.seller_ship_ontime = round(((int(seller.seller_ship_ontime) * int(seller.num_of_ship_ontime)) + int(seller_ship_ontime)) / (int(seller.num_of_ship_ontime) + 1))
                seller.num_of_ship_ontime = int(seller.num_of_ship_ontime) + 1
                
                session.save_changes()
                print(f"Seller {seller_id} updated successfully.")
            else:
                print("Seller not found for update.")