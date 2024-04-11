from pyravendb.store import document_store
from Entity import server_url, database_name, certificate, Sale, Product, Category
from datetime import datetime
import argparse

store = document_store.DocumentStore(urls=[server_url], database=database_name, certificate=certificate)
store.initialize()

period_dict = {"1":("1/1","1/4"), "2":("1/4","1/7"), "3":("1/7","1/10"), "4":("1/10","1/1")}

def query(from_date, to_date):
    with store.open_session() as session:
        sales = list(session.query(object_type=Sale).where_between("date", from_date.isoformat(), to_date.isoformat()).order_by("date"))
        if len(sales) == 0:
            with open('CustomerDemand.txt', "w", encoding='utf-8') as file:
                file.write(f"???\n")
            return
        
        products = list(session.query(collection_name="Products", object_type=Product))
        product_dict = {product.Id: product.category for product in products}
        
        categories = list(session.query(collection_name="Categories", object_type=Category))
        
        quantity_by_category = {category.name : 0 for category in categories}
        
        for sale in sales:
            quantity_by_category[product_dict[sale.product_id]] += sale.quantity
            
        total = sum(quantity for quantity in quantity_by_category.values())
        
        with open('CustomerDemand.txt', "w", encoding='utf-8') as file:
            for category, quantity in quantity_by_category.items():
                file.write(f"{category}#{quantity}#{round(quantity*100/total)}%\n")
                
            print("File write operation successful.")

if __name__ == "__main__":
    # Parse command-line arguments
    parser = argparse.ArgumentParser(description="Query customer demand")
    parser.add_argument("period", type=str, help="From Time (p/yyyy)")
    args = parser.parse_args()

    period, year = args.period.split('/')
    
    tup = period_dict[period]
    
    from_date_str = f'{tup[0]}/{year}'
    from_date = datetime.strptime(from_date_str, "%d/%m/%Y")
    
    to_date_str =''
    
    if period != "4":
        to_date_str = f'{tup[1]}/{year}'
    else:
        to_date_str = f'{tup[1]}/{int(year) + 1}'
    
    to_date = datetime.strptime(to_date_str, "%d/%m/%Y")
        
    
    query(from_date, to_date)