from pydantic import BaseModel


class SaveBase(BaseModel):
    '''Base save model'''
    plr_one_active: bool
    plr_one_name:   str
    plr_two_name:   str
    plr_one_score:  int
    plr_two_score:  int
# end SaveBase()


class SaveCreate(SaveBase):
    '''Inherits from SaveBase'''
    pass
# end SaveCreate()


class Save(SaveBase):
    '''Inherits from SaveBase, used for route handling'''
    id: int

    class Config:
        orm_mode = True
    # end Config

# end Save()
