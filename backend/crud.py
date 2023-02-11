from sqlalchemy.orm import Session

# Local imports
from . import models, schemas

# ********************************************************************
# NOTES
# ********************************************************************
# All database interaction is handled through the /saves/ route

# Player names are not allowed to be updated within the save files
# This is because different players means its a different game


def create_save(db: Session, save: schemas.SaveCreate):
    '''
    Action: Insert new record into db
    Params: save: pydantic schema, db: db session instance
    Return: save pydantic schema
    '''
    db_save = models.Save(**save.dict())
    db.add(db_save)
    db.commit()
    db.refresh(db_save)

    return db_save
# end create_save()


def read_saves(db: Session, offset: int = 0, limit: int = 15):
    '''
    Action: Retrieve n number of records starting from an offset
    Params: offset: number of records to skip, limit: first n records after offset
    Return: result of "SELECT" query
    '''
    return db.query(models.Save).offset(offset).limit(limit).all()
# end read_saves()


def read_save(db: Session, id: int):
    '''
    Action: Get save record by its id
    Params: db: session instance, id: primary key
    Return: Result of "SELECT" query
    '''
    return db.query(models.Save).filter(models.Save.id == id).first()
# end read_save()


def update_save(db: Session, id: int, save: schemas.SaveCreate):
    '''
    Action: Update existing save
    Params: id: id of save record, save: pydantic schema, db: db session instance
    Return: updated save pydantic schema
    '''
    db_save = db.query(models.Save).filter(models.Save.id == id).first()

    # Update fields
    db_save.plr_one_active = save.plr_one_active
    db_save.plr_one_score = save.plr_one_score
    db_save.plr_two_score = save.plr_two_score

    db.commit()

    return db_save
# end update_save()


def delete_save(db: Session, id: int):
    '''
    Action: Delete record with matching id
    Params: db: db session instance, id: id of save record
    Return: N/A
    '''
    db.query(models.Save).filter(models.Save.id == id).delete()
    db.commit()

    return
# end delete_save
