from pyravendb.store import document_store
from Entity import server_url, database_name, certificate, Promotion, Sale
from datetime import datetime
from dateutil.parser import parse
from dateutil.relativedelta import relativedelta
import argparse

store = document_store.DocumentStore(urls=[server_url], database=database_name, certificate=certificate)
store.initialize()

def query(promotion_id, product_id):
    with store.open_session() as session:
        promotion = session.load(promotion_id, object_type=Promotion)
        if promotion:
            promotion_from_date = parse(promotion.from_date)
            promotion_to_date = parse(promotion.to_date)
            
            start_date = datetime(promotion_from_date.year, promotion_from_date.month, 1)
            end_date = start_date + relativedelta(months=1)
            
            sales = list(session.query(object_type=Sale).where_between("date", start_date.isoformat(), end_date.isoformat()).order_by("date"))
            sales_by_product = [sale for sale in sales if sale.product_id == product_id]
            
            if len(sales_by_product) == 0:
                with open('InventoryManagment.txt', "w", encoding='utf-8') as file:
                    file.write(f"???\n")
                    return
            
            total_in_month = sum(int(sale.quantity) for sale in sales)
            promotion_sales = list(filter(lambda sale: promotion_from_date <= parse(sale.date) <= promotion_to_date, sales))
            total_in_promotion = sum(int(sale.quantity) for sale in promotion_sales)
            
            total_by_product_in_month = sum(int(sale.quantity) for sale in sales_by_product)
            promotion_sales_by_product = list(filter(lambda sale: promotion_from_date <= parse(sale.date) <= promotion_to_date, sales_by_product))
            total_by_product_in_promotion = sum(int(sale.quantity) for sale in promotion_sales_by_product)
            
            with open('PromotionProgram.txt', "w", encoding='utf-8') as file:
                file.write(f"{sales_by_product[0].product_name}\n")
                file.write(f"{total_by_product_in_month}#{total_by_product_in_promotion}#{total_in_month}#{total_in_promotion}\n")
            
            print("File write operation successful.")
        else:
            with open('InventoryManagment.txt', "w", encoding='utf-8') as file:
                file.write(f"???\n")
    

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Query promotion infomation")
    parser.add_argument("promotion_id", type=str, help="Promotion ID")
    parser.add_argument("product_id", type=str, help="Product ID")
    args = parser.parse_args()
    
    query(args.promotion_id, args.product_id)