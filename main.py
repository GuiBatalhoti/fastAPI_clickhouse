from fastapi import FastAPI
from fastapi.responses import JSONResponse
from clickhouse_driver import Client

app = FastAPI()

# Connect to ClickHouse
ch_client = Client(host='some-clickhouse-server', port=9000)

@app.get("/users/{user_id}")
async def read_user(user_id: int):
    # Query ClickHouse for user data
    query = f"SELECT * FROM users WHERE id = {user_id}"
    result = ch_client.execute(query)
    
    if result:
        # Convert ClickHouse result to JSON and return it
        user_data = result[0]  # Assuming the result is a dictionary
        return JSONResponse(content=user_data)
    else:
        return JSONResponse(content={"message": "User not found"}, status_code=404)