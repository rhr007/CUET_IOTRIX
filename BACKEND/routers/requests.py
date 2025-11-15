from fastapi import APIRouter, Depends
from sqlmodel import Session
from datetime import datetime
from db import get_db
from models import RideRequest

router = APIRouter(prefix="/request", tags=["Requests"])

@router.get("/create")
def create_request(destination: str, db: Session = Depends(get_db)):
    ride = RideRequest(
        destination=destination,
        request_time=datetime.now()
    )
    db.add(ride)
    db.commit()
    db.refresh(ride)

    return {
        "message": "Ride request created",
        "request_id": ride.id,
        "status": ride.status
    }
