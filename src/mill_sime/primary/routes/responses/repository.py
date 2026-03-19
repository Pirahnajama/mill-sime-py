from datetime import date
from pydantic import BaseModel 

class RepositoryResponse (BaseModel):
    appointement_date : date