from fastapi import FastAPI, status
from fastapi.responses import JSONResponse

import time
import requests
app = FastAPI(title=f"NewAI 🧠 - APIs")


@app.get("/check", tags=["General"])
async def check():
    try:
        for i in range(5):
            time.sleep(0.5)
            requests.get("https://google.com/")
            print(f"Sleeping {i}")
        return JSONResponse(status_code=status.HTTP_200_OK,
                            content={"message": "NewAI APIs is running well!"})
    except Exception as e:
        return JSONResponse(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            content={"message": str(e)})


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8001)
