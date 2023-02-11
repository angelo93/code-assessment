from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
from fastapi.middleware.cors import CORSMiddleware

# Local imports
from . import crud, models, schemas, game
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Required to allow frontend communication
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


def get_db():
    '''
    Action: Attempts to provide a db session, closes session when done
    Params: N/A
    Return: Yields db session instance
    Note:   Used as a dependancy
    '''
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
    # end try
# end get_db()


# ********************************************************************
# SAVE ROUTING
# ********************************************************************


@app.post("/saves/", response_model=schemas.Save)
def create_save(save: schemas.SaveCreate, db: Session = Depends(get_db)):
    '''
    Action: Creates a new save in the database
    Params: save: pydantic schema, db: db session instance
    Return: save pydantic schema
    '''
    save_result = crud.create_save(db, save)
    return save_result
# end create_save()


@app.get("/saves/", response_model=list[schemas.Save])
def read_saves(offset: int = 0, limit: int = 15, db: Session = Depends(get_db)):
    '''
    Action: Retrieve n number of records starting from an offset
    Params: offset: number of records to skip, limit: first n records after offset
            db: session instance
    Return: list of save records in pydantic schema form
    '''
    saves = crud.read_saves(db, offset, limit)
    return saves
# end read_saves()


@app.get("/saves/{id}", response_model=schemas.Save)
def read_save(id: int, db: Session = Depends(get_db)):
    '''
    Action: Retrieve save record with matching id
    Params: db: session instance
    Return: Save record or Return Code
    '''
    save = crud.read_save(db, id)

    if save is None:
        raise HTTPException(status_code=404, detail="Save file not found")
    # end if

    return save
# end read_save()


@app.put("/saves/{id}", response_model=schemas.Save)
def update_save(id: int, save: schemas.SaveCreate, db: Session = Depends(get_db)):
    '''
    Action: Update existing save
    Params: id: id of save record, save: pydantic schema, db: db session instance
    Return: updated save pydantic schema
    '''
    old_save = crud.read_save(db, id)

    if old_save is None:
        raise HTTPException(status_code=404, detail="Save file not found")
    # end if

    updated_save = crud.update_save(db, id, save)

    return updated_save
# end update_save()


@app.delete("/saves/{id}", response_model=schemas.Save)
def delete_save(id: int, db: Session = Depends(get_db)):
    '''
    Action: Delete record with matching id
    Params: db: db session instance, id: id of save record
    Return: save pydantic schema
    '''
    save = crud.read_save(db, id)

    if save is None:
        raise HTTPException(status_code=404, detail="Save file not found")
    else:
        crud.delete_save(db, id)
    # end if

    return save
# end delete_save()

# ********************************************************************
# GAME ROUTING
# ********************************************************************


@app.get("/match/")
async def match_result(plr_one_choice: int, plr_two_choice: int, mode: int):
    '''
    Action: Determine result of match
    Params: plr_one_choice, plr_two_choice, mode: PvP, PvC
    Return: Dictionary with information related to match
    '''
    result = {}

    if mode == 0 or mode == 1:
        result = game.match_result(plr_one_choice, plr_two_choice, mode)
    else:
        raise HTTPException(status_code=400, detail="Invalid game mode")
    # end if

    return result
# end match_result()
