from typing import Any, Dict
from rich.pretty import pprint
from fastapi import FastAPI

app = FastAPI()


@app.post("/")
def recv_webhook(payload: Dict[Any, Any]):
    pprint(payload)
