# Configuration
server_url = "https://a.bigdataapp.ravendb.community"
database_name = "ECommerce"
certificate = {"pfx":"E:\RavenDB-6.0.101-windows-x64\Server\cluster.server.certificate.bigdataapp.pfx","password":""}

class Product:
    def __init__(self, id, name, brand, category_id, category, image, mall_certification, total_product_reviews, price, product_rate1star, product_rate2star, product_rate3star, product_rate4star, product_rate5star, product_average_rating, seller_name, seller_id):
        self.Id = id
        self.name = name
        self.brand = brand
        self.category_id = category_id
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
        self.seller_id = seller_id
           
class Seller:
    def __init__(self, id, seller_name, seller_rating, seller_response_rate, seller_ship_ontime, num_of_rating, num_of_response_rate, num_of_ship_ontime):
        self.Id = id
        self.seller_name = seller_name
        self.seller_rating = seller_rating
        self.seller_response_rate = seller_response_rate
        self.seller_ship_ontime = seller_ship_ontime
        self.num_of_rating = num_of_rating
        self.num_of_response_rate = num_of_response_rate
        self.num_of_ship_ontime = num_of_ship_ontime
        
class Category:
    def __init__(self, id, name):
        self.Id = id
        self.name = name
        
class Customer:
    def __init__(self, id, full_name, birthYear, gender, province, recent_interested):
        self.Id = id
        self.full_name = full_name
        self.birthYear = birthYear
        self.gender = gender
        self.province = province
        self.recent_interested = recent_interested

class Inventory:
    def __init__(self, id, date, product_id, product_name, quantity):
        self.Id = id
        self.date = date
        self.product_id = product_id
        self.product_name = product_name
        self.quantity = quantity
        
class Sale:
    def __init__(self, id, date, product_id, product_name, quantity):
        self.Id = id
        self.date = date
        self.product_id = product_id
        self.product_name = product_name
        self.quantity = quantity
    
class Promotion:
    def __init__(self, id, name, from_date, to_date):
        self.Id = None
        self.name = name
        self.from_date = from_date
        self.to_date = to_date