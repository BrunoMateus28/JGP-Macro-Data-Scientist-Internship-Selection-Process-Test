from fastapi import FastAPI
import pandas as pd
from typing import List, Optional

app = FastAPI()

# Load data from CSV
df = pd.read_csv('cpi_data.csv')
df['date'] = pd.to_datetime(df['date'], format='%m/%d/%Y')

@app.get("/data/")
def get_data(start_date: Optional[str] = None, end_date: Optional[str] = None) -> List[dict]:
    """
    Get data from the CSV file.
    You can specify the start_date and end_date to filter the data.
    Dates should be in the format YYYY-MM-DD.
    """
    # Convert optional query parameters to datetime
    if start_date:
        start_date = pd.to_datetime(start_date)
    if end_date:
        end_date = pd.to_datetime(end_date)

    # Filter data
    filtered_df = df
    if start_date:
        filtered_df = filtered_df[filtered_df['date'] >= start_date]
    if end_date:
        filtered_df = filtered_df[filtered_df['date'] <= end_date]

    # Convert to list of dicts for response
    result = filtered_df.to_dict(orient='records')
    return result

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
