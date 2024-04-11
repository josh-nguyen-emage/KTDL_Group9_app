from pyravendb.store import document_store
from Entity import server_url, database_name, certificate, Inventory,Sale
from datetime import datetime
from dateutil.parser import parse
from dateutil.relativedelta import relativedelta
import argparse

store = document_store.DocumentStore(urls=[server_url], database=database_name, certificate=certificate)
store.initialize()

def query(product_id, from_date, to_date):
    with store.open_session() as session:
        # .where_greater_than_or_equal(field_name="date", value=from_date.isoformat()).where_less_than_or_equal(field_name="date", value=to_date.isoformat())
        inventories = list(session.query(object_type=Inventory).where_equals(field_name="product_id",value=product_id).order_by(field_name="date"))
        if len(inventories) == 0:
            with open('InventoryManagment.txt', "w", encoding='utf-8') as file:
                file.write(f"???\n")
            return
        # .where_greater_than_or_equal(field_name="date", value=from_date.isoformat()).where_less_than_or_equal(field_name="date", value=to_date.isoformat())
        sales = list(session.query(object_type=Sale).where_equals(field_name="product_id", value=product_id).order_by(field_name="date"))
        
        filtered_inventories = list(filter(lambda inventory: from_date <= parse(inventory.date) < to_date, inventories))
        filtered_sales = list(filter(lambda sale: from_date <= parse(sale.date) < to_date, sales))

        
        inventory_monthly_totals = {}
        for inventory in filtered_inventories:
            datetime_object = parse(inventory.date)
            month_key = (datetime_object.year, datetime_object.month)
            if month_key not in inventory_monthly_totals.keys():
                inventory_monthly_totals[month_key] = int(inventory.quantity)
            else:
                inventory_monthly_totals[month_key] += int(inventory.quantity)
                
        sale_monthly_totals = {}
        for sale in filtered_sales:
            datetime_object = parse(sale.date)
            month_key = (datetime_object.year, datetime_object.month)
            if month_key not in sale_monthly_totals.keys():
                sale_monthly_totals[month_key] = int(sale.quantity)
            else:
                sale_monthly_totals[month_key] += int(sale.quantity)

        try:
            with open('InventoryManagment.txt', "w", encoding='utf-8') as file:
                file.write(f"{inventories[0].product_name}\n")
                
                for month_key in inventory_monthly_totals.keys():
                    inventory_quantity = inventory_monthly_totals[month_key]
                    sale_quantity = 0 if month_key not in sale_monthly_totals.keys() else sale_monthly_totals[month_key]
                    file.write(f"{month_key[1]}/{month_key[0]}#{sale_quantity}#{inventory_quantity}\n")
                
            print("File write operation successful.")
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Parse command-line arguments
    parser = argparse.ArgumentParser(description="Query products by category")
    parser.add_argument("product_id", type=str, help="Product ID")
    parser.add_argument("from_time", type=str, help="From Time (mm/yyyy)")
    parser.add_argument("to_time", type=str, help="To Time (mm/yyyy)")
    args = parser.parse_args()

    from_month_str, from_year_str = args.from_time.split('/')
    from_month = int(from_month_str)
    from_year = int(from_year_str)
    from_date = datetime(year=from_year, month=from_month, day=1)
    
    print(f'{from_date.day}/{from_date.month}/{from_date.year}')
    
    to_month_str, to_year_str = args.to_time.split('/')
    to_month = int(to_month_str)
    to_year = int(to_year_str)
    to_date = datetime(year=to_year, month=to_month, day=1) + relativedelta(months=1) 
    
    print(f'{to_date.day}/{to_date.month}/{to_date.year}')
    
    query(args.product_id, from_date, to_date)