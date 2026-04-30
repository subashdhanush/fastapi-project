from fastapi import FastAPI
from models import Product


app=FastAPI()

@app.get("/")
def greet():
    return "Welcome to FastAPI"


products=[

   Product(id=1,name="Laptop",description="A high performance laptop",price=999.99,quantity=10),
   Product(id=2,name="Smartphone",description="A latest model smartphone",price=499.99,quantity=20),
]

# @app.get("/products")
# def get_all_products():
#     return products


@app.get("/products")
def get_all_products():
    db=session()
    db.query()
    return products


@app.get("/product/{id}")
def get_product_by_id(id:int):
    for product in products:
        if product.id==id:
            return product
    return "product not found"

@app.post("/product")
def add_product(product:Product):
    products.append(product)
    return "product added successfully"

@app.put("/product")
def update_product(id:int,product:Product):
    for i in range(len(products)):
        if products[i].id ==id:
            products[i]=product
            return "product updated successfully"
    return "product not found"    


@app.delete("/product")
def delete_product(id:int):
    for i in range(len(products)):
        if products[i].id == id:
            del products[i]
            return "product deleted successfully"
    return "product not found"    