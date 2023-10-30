import fastapi
import connection
app = fastapi.FastAPI()
@app.get("/")
def hello_world_root():
    return {"Olá": "Funciona"}

@app.get("/getContinents")
def getContinents():
    Continents_list = []
    mycursor = connection.mydb.cursor(dictionary=True)
    sql = "select * from continents"
    mycursor.execute(sql)
    for data_continents in mycursor:
        Continents_list.append( data_continents )
    mycursor.close()
    return {"Continents": Continents_list}

@app.get("/getRegions")
def getRegions():
    Regions_list = []
    mycursor = connection.mydb.cursor(dictionary=True)
    sql = "select * from regions"
    mycursor.execute(sql)
    for data_regions in mycursor:
        Regions_list.append( data_regions )
    mycursor.close()
    return {"Regions": Regions_list}
