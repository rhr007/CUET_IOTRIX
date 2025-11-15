from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select
from db import get_db
from models import User, RideRequest

router = APIRouter(prefix="/puller", tags=["Puller"])

@router.get("/requests")
def get_pending_requests(db: Session = Depends(get_db)):
    requests = db.exec(
        select(RideRequest).where(RideRequest.status == "pending")
    ).all()
    
    return requests


@router.post("/accept")
def accept_request(puller_id: int, request_id: int, db: Session = Depends(get_db)):
    ride = db.get(RideRequest, request_id)

    if not ride:
        raise HTTPException(404, "Request not found")

    if ride.status != "pending":
        return {"message": "Too late, someone already took it!"}

    ride.status = "accepted"
    ride.assigned_puller_id = puller_id

    db.add(ride)
    db.commit()
    db.refresh(ride)

    return {"message": "Request accepted", "request_id": ride.id}


# @router.post("/complete")
# def complete_request(request_id: int, db: Session = Depends(get_db)):
#     ride = db.get(RideRequest, request_id)
#     ride.status = "completed"

#     db.add(ride)
#     db.commit()

#     return {"message": "Request completed"}

@router.post("/complete")
def complete_request(
    request_id: int,
    puller_id: int,
    db: Session = Depends(get_db)
):
    ride = db.get(RideRequest, request_id)

    if not ride:
        raise HTTPException(404, "Ride not found")

    if ride.status != "accepted":
        raise HTTPException(400, "This ride is not active")

    # Update ride status
    ride.status = "completed"
    db.add(ride)

    # Fetch puller
    puller = db.get(User, puller_id)
    if not puller:
        raise HTTPException(404, "Puller not found")

    # Add reward points
    puller.points += 100
    db.add(puller)

    db.commit()
    db.refresh(puller)

    return {
        "message": "Ride completed",
        "earned_points": 100,
        "total_points": puller.points
    }



@router.post("/reject")
def reject_request(request_id: int, db: Session = Depends(get_db)):
    ride = db.get(RideRequest, request_id)

    ride.status = "rejected"
    db.add(ride)
    db.commit()

    return {"message": "Request rejected"}



@router.get("/accepted")
def get_accepted_requests(puller_id: int, db: Session = Depends(get_db)):
    rides = db.exec(
        select(RideRequest).where(
            RideRequest.assigned_puller_id == puller_id,
            RideRequest.status == "accepted"
        )
    ).all()
    return rides

@router.get("/completed")
def get_completed_requests(puller_id: int, db: Session = Depends(get_db)):
    rides = db.exec(
        select(RideRequest).where(
            RideRequest.assigned_puller_id == puller_id,
            RideRequest.status == "completed"
        )
    ).all()
    return rides


