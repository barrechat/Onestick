from fastapi import FastAPI,UploadFile,HTTPException
from fastapi.responses import FileResponse
import pandas as pd
from os import remove

app = FastAPI()

@app.get("/total")
def crear_total():
    orders = pd.read_csv("orders.csv")
    products= pd.read_csv("products.csv")
    prices = pd.DataFrame([],columns=["id","total"])
            
    for order in orders.iterrows():
                total = 0.0
                try:
                    id_order = order[0]
                    id_products = order[1]["products"].split(" ")
                except:
                    print("index error, corregir bd")
                for id in id_products:
                    total += products.iloc[int(id)]["cost"]
                prices.loc[len(prices)] = {"id":id_order,"total":total}
    prices.to_csv("order_prices.csv",index=False)
    return prices.to_json(orient="records")                   
@app.get("/comprasxproducto")
def compras():           
    
    orders = pd.read_csv("orders.csv")
    customers = pd.DataFrame([],columns=["id","customer_ids"])
    products = dict()

    for order in orders.iterrows():
                try:
                    shopped = order[1]["products"].split(" ")
                    customer = order[1]["customer"]
                except:
                    print("index error, corregir bd")
                for product in shopped:
                    try:
                        products[int(product)]+= " "+ str(customer)
                        
                    except:
                        products[int(product)] = str(customer)
                    
                    
    for product in products:
                customers.loc[len(customers)]={"id":product,"customer_ids":products[product]}  
    customers.to_csv("product_customers.csv",index=False)
    return customers.to_json(orient="records")
@app.get("/ranking")
def ranking():
    crear_total()
    prices = pd.read_csv("order_prices.csv")
    orders = pd.read_csv("orders.csv")
    customers =  pd.read_csv("customers.csv")
    ranking = pd.DataFrame([],columns=["id","name","lastname","total"])       
    info = dict() 
    
    for customer in customers.iterrows():
        try:
            info[customer[1]["id"]] = {"name":customer[1]["firstname"],"lastname":customer[1]["lastname"]}
        except:
             print("index error, corregir bd")
    for order, price in zip(orders.iterrows(),prices.iterrows()):
        try:
            ranking.loc[len(ranking)]={
                "id": order[1]["customer"],
                "name":info[order[1]["customer"]]["name"],
                "lastname":info[order[1]["customer"]]["lastname"],
                "total":price[1]["total"]}
        except:
             print("index error, corregir bd")
    ranking =ranking.sort_values(by=["total"],ascending=False)
    ranking.to_csv("customer_ranking.csv",index=False)
    return ranking.to_json(orient="records")    
@app.post("/upload/orders")  
async def upload_total(file : UploadFile):
    try:
        with open("orders.csv","wb") as orders:
         data = await file.read()
         orders.write(data)
         orders.close()
        return "succes"
    except:
        raise HTTPException(status_code=204,detail="El archivo es incorrecto")

@app.post("/upload/products")  
async def upload_total(file : UploadFile):
    try:
        with open("products.csv","wb") as products:
            data = await file.read()
            products.write(data)
            products.close()
        return "succes"
    except:
        raise HTTPException(status_code=204,detail="El archivo es incorrecto")

@app.post("/upload/customers")  
async def upload_total(file : UploadFile):
    with open("customers.csv","wb") as customers:
         data = await file.read()
         customers.write(data)
         customers.close()
    return "succes"

@app.get("/download/{filename}")
async def download_file(filename:str):
     try:
        return FileResponse("./"+filename, status_code=200)
     except:
          HTTPException(status_code=400, detail="No se pudo almacenar archivo")

@app.delete("/delete/{filename}")
async def delete_file(filename:str):
     try:
          remove(filename)
     except:
          HTTPException(status_code=204,detail="No se encuentra el archivo")
