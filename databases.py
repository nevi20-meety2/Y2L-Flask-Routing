from model import Base, Product


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker,scoped_session


engine = create_engine('sqlite:///database.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = scoped_session(sessionmaker(bind=engine,autoflush=False))

def add_product(name, Price, Picturelink, Descroption):
    product_object = Product(
        name=name,
        Price=Price,
        Picturelink=Picturelink,
    	Description=Descroption)
    session.add(product_object)
    session.commit()


#add_product("GREY TPWK HOODIE", 60.0, "static/tpwkgrey.png", "")
#add_product("ADORE YOU BLACK TEE", 35.0, "static/adoreyoushirt.jpg", "")

def update_product(name, Price, Picturelink, Descroption):
   product_object = session.query(
       Product).filter_by(
       name=name).first()
   product_object.Price = Price
   session.commit()


#update_product("Emily", True)

def delete_product(their_price):
   session.query(Product).filter_by(
       Price=their_price).delete()
   session.commit()


#delete_student("Mayuri")

def query_all():
   """
   Print all the students
   in the database.
   """
   product = session.query(
      Product).all()
   return product


print(query_all())

def query_by_price(their_price):
   """
   Find the first student
   in the database, by their name
   """
   Product = session.query(
       Product).filter_by(
       name=their_name).first()
   return Product


#print(query_by_name("Mayuri"))

def Add_To_Cart (productID):
    cart_object = Cart(
        productID=productID)
    session.add(Cart_object)
    session.commit()

#Add_To_Cart()