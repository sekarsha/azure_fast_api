from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app=FastAPI()

@app.get("/", response_class=HTMLResponse)
async def welcome():
    """
    Welcome page that serves as the entry point for the application.
    """
    return """
    <html>
        <head>
            <title>Welcome Page</title>
        </head>
        <body>
            <h1>Welcome to the API!</h1>
            <p>This is the welcome page.</p>
        </body>
    </html>
    """