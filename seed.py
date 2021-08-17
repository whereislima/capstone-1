from app import app
from models import db, Product

db.drop_all()
db.create_all()

p1 = Product(name="brand face wash", description="cleanser")
p2 = Product(name="brand toner", description="toner")
p3 = Product(name="brand essence", description="essence")
p4 = Product(name="brand eyecream", description="eye cream")
p5 = Product(name="brand vitaminC", description="active")
p6 = Product(name="brand retinol", description="active")
p7 = Product(name="brand sunblock", description="sunscreen")
p8 = Product(name="brand moisturizer", description="moisturizer")

db.session.add_all([p1, p2, p3, p4, p5, p6, p7, p8])
db.session.commit()