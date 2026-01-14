from fastapi import FastAPI
from pydantic import BaseModel
import psycopg2
from datetime import datetime

app = FastAPI()

# Database connection
def get_db_connection():
    return psycopg2.connect(
        host="postgres",  # Docker Compose service name!
        database="mldata",
        user="mluser",
        password="mlpassword"
    )

class PredictionInput(BaseModel):
    value: float

@app.get("/")
def read_root():
    return {"message": "ML API with Database", "status": "running"}

@app.post("/predict")
def predict(input: PredictionInput):
    # Simple prediction
    prediction = input.value * 2
    
    # Store in database
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO predictions (input_value, prediction, timestamp) VALUES (%s, %s, %s)",
            (input.value, prediction, datetime.now())
        )
        conn.commit()
        cur.close()
        conn.close()
    except Exception as e:
        print(f"Database error: {e}")
    
    return {"input": input.value, "prediction": prediction}

@app.get("/history")
def get_history():
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("SELECT * FROM predictions ORDER BY timestamp DESC LIMIT 10")
        results = cur.fetchall()
        cur.close()
        conn.close()
        
        return {"predictions": [
            {
                "id": r[0],
                "input": r[1],
                "prediction": r[2],
                "timestamp": str(r[3])
            } for r in results
        ]}
    except Exception as e:

        return {"error": str(e)}
