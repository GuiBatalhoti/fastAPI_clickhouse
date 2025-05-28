from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from clickhouse_driver import Client
from datetime import datetime


app = FastAPI()
# Connect to ClickHouse
ch_client = Client(host='localhost', port=19000, user='default', password='changeme')
print("CLICKHOUSE:",ch_client.execute('SHOW DATABASES'))
ch_client.execute('USE db')
print("CLICKHOUSE:",ch_client.execute('SHOW TABLES'))


@app.get("/")
def root():
    return {"Hello": "World!!"}


@app.get("/query/{no_fantasia}/{date}")
def query(no_fantasia: str, data: str):
    try:
        result = ch_client.execute(
            f'SELECT * FROM vit WHERE no_fantasia=\'{no_fantasia}\' AND data = \'{data}\'',
        )
        if not result:
            raise HTTPException(status_code=404, detail="No data found")
        
        # Return the result as JSON
        return JSONResponse(content=result)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    

@app.get("/get_all")
def get_all():
    try:
        # Execute the query to get all data
        result = ch_client.execute('SELECT * FROM vit')
        if not result:
            raise HTTPException(status_code=404, detail="No data found")
        
        # Return the result as JSON
        return JSONResponse(content=result)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    

@app.post("/populate")
def populate():
    try:
        # Execute the insert query
        ch_client.execute(
            'INSERT INTO vit (no_fantasia, data, placa) VALUES',
            [('example_fantasia1', '2023-10-01', 'ABC1234'),
             ('example_fantasia1', '2023-10-02', 'XYZ5678'),
             ('example_fantasia1', '2023-10-03', 'LMN9101'),
             ('example_fantasia1', '2023-10-04', 'OPQ2345'),
             ('example_fantasia2', '2023-10-05', 'RST6789'),
             ('example_fantasia2', '2023-10-06', 'UVW3456'),
             ('example_fantasia2', '2023-10-07', 'XYZ8901'),
             ('example_fantasia2', '2023-10-08', 'ABC1234')]
        )
        return {"message": "Data inserted successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
    
@app.delete("/drop_all")
def drop_all():
    try:
        # Execute the delete query
        ch_client.execute('TRUNCATE TABLE vit')
        return {"message": "All data dropped successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))