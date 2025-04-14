import pandas as pd
from fastapi import FastAPI, UploadFile, HTTPException
from fastapi.responses import FileResponse
from classify import classify

app = FastAPI()

@app.post("/classify")
async def classify_logs(file: UploadFile):
    if not file.filename.endswith(".csv"):
        raise HTTPException(status_code=400, detail="Invalid file type")

    try:
        df = pd.read_csv(file.file)
        if "source" not in df.columns or "log_message" not in df.columns:
            raise HTTPException(status_code=400, detail="file must contain 'source' and 'log_message' columns")

        # classify
        df['target_label'] = df["target_label"] = classify(list(zip(df["source"], df["log_message"])))


        # Save the file
        output_path = "resources/output.csv"
        df.to_csv(output_path, index=False)
        print("File saved in resources")
        return FileResponse(output_path, media_type="text/csv")

    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    finally:
        file.file.close()