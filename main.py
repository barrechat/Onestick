from fastapi import FastAPI,UploadFile,HTTPException
from fastapi.responses import FileResponse
import pandas as pd
from os import remove

app = FastAPI()

@app.get("/total")
def crear_total():
    #leemos los csv y creamos el dataframe resultante
    try:
        orders = pd.read_csv("orders.csv")
        products= pd.read_csv("products.csv")
        prices = pd.DataFrame([],columns=["id","total"])
    except:
         HTTPException(status_code=204,detail="No se encuentra algun archivo")      
    #recorremos orders.csv
    for order in orders.iterrows():
                total = 0.0
                try:
                    id_order = order[0]
                    id_products = order[1]["products"].split(" ")
                except:
                    print("index error, corregir bd")
                #sumamos el valor de los productos
                for id in id_products:
                    total += products.iloc[int(id)]["cost"]
                #guardamos el valor en el dataframe
                prices.loc[len(prices)] = {"id":id_order,"total":total}
    #almacenamos el dataframe y enviamos el resultado
    prices.to_csv("order_prices.csv",index=False)
    return prices.to_json(orient="records")                   
@app.get("/comprasxproducto")
def compras():    
    #leemos los csv y creamos el dataframe resultante y el dict auxiliar       
    try:
        orders = pd.read_csv("orders.csv")
        customers = pd.DataFrame([],columns=["id","customer_ids"])
        products = dict()
    except:
         HTTPException(status_code=204,detail="No se encuentra algun archivo")  
    
    for order in orders.iterrows():
                try:
                    shopped = order[1]["products"].split(" ")
                    customer = order[1]["customer"]
                except:
                    print("index error, corregir bd")
                #almacenamos los id de los clientes
                for product in shopped:
                    try:
                        products[int(product)]+= " "+ str(customer)
                        
                    except:
                        products[int(product)] = str(customer)
                    
    #almacenamos los resultado en el dataframe                
    for product in products:
                customers.loc[len(customers)]={"id":product,"customer_ids":products[product]}  
    #guardamos el csv y enviamos el resultado
    customers.to_csv("product_customers.csv",index=False)
    return customers.to_json(orient="records")
@app.get("/ranking")
def ranking():
    #actualizamos order_prices.csv
    crear_total()
    #leemos los csv y creamos el dataframe resultante y el dict auxiliar       
    try:
        prices = pd.read_csv("order_prices.csv")
        orders = pd.read_csv("orders.csv")
        customers =  pd.read_csv("customers.csv")
        ranking = pd.DataFrame([],columns=["id","name","lastname","total"])       
        info = dict() 
    except:
         HTTPException(status_code=204,detail="No se encuentra algun archivo")  
    #iteramos los clientes
    for customer in customers.iterrows():
        try:
            #almacenamos los datos del cliente en info
            info[customer[1]["id"]] = {"name":customer[1]["firstname"],"lastname":customer[1]["lastname"]}
        except:
             print("index error, corregir bd")
    #iteramos orders.csv y order_prices.csv conjuntamente
    for order, price in zip(orders.iterrows(),prices.iterrows()):
        try:
            #almacenamos los datos necesarios
            ranking.loc[len(ranking)]={
                "id": order[1]["customer"],
                "name":info[order[1]["customer"]]["name"],
                "lastname":info[order[1]["customer"]]["lastname"],
                "total":price[1]["total"]}
        except:
             print("index error, corregir bd")
    #ordenamos descendentemente
    ranking =ranking.sort_values(by=["total"],ascending=False)
    #almacenamos el csv y enviamos los resultados
    ranking.to_csv("customer_ranking.csv",index=False)
    return ranking.to_json(orient="records")    
@app.post("/upload")  
async def upload_total(file : UploadFile):
    try:
        #abrimos el archivo enviado
        with open(file.filename,"wb") as new:
         data = await file.read()
         new.write(data)
         new.close()
        return "success"
    except:
        raise HTTPException(status_code=204,detail="El archivo es incorrecto")

@app.get("/download/{filename}")
async def download_file(filename:str):
     try:
        #retornamos el archivo solicitado
        return FileResponse("./"+filename, status_code=200)
     except:
          HTTPException(status_code=400, detail="No se pudo almacenar archivo")

@app.delete("/delete/{filename}")
async def delete_file(filename:str):
     try:
          #eliminamos el archivo solicitado
          remove(filename)
     except:
          HTTPException(status_code=204,detail="No se encuentra el archivo")
