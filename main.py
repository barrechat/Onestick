from fastapi import FastAPI
import pandas as pd

app = FastAPI()

@app.get("/total")
def crear_total():
    orders = pd.read_csv("orders.csv")
    products= pd.read_csv("products.csv")
    prices = pd.DataFrame([],columns=["id","total"])
            
    for order in orders.iterrows():
                total = 0.0
                
                id_order = order[0]
                id_products = order[1]["products"].split(" ")
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
                shopped = order[1]["products"].split(" ")
                customer = order[1]["customer"]
                print(order[1]["customer"])
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
        info[customer[1]["id"]] = {"name":customer[1]["firstname"],"lastname":customer[1]["lastname"]}
    for order, price in zip(orders.iterrows(),prices.iterrows()):
        ranking.loc[len(ranking)]={
            "id": order[1]["customer"],
            "name":info[order[1]["customer"]]["name"],
            "lastname":info[order[1]["customer"]]["lastname"],
            "total":price[1]["total"]}
    ranking =ranking.sort_values(by=["total"],ascending=False)
    ranking.to_csv("customer_ranking.csv",index=False)
    return ranking.to_json(orient="records")                