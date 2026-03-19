from signal import pause
from fastapi import APIRouter
from fastapi.exceptions import HTTPException
from sqlalchemy.log import Identified

from mill_sime.dependencies import FarmerRepositoryDep
from mill_sime.domain.models.farmer import FarmerReference
from mill_sime.domain.use_cases import get
from mill_sime.primary.routes.responses.repository import RepositoryResponse
from mill_sime.secondary import farmer_repository

router = APIRouter(prefix="/api/repositories", tags=["repositories"])


@router.post(path=f"/{id}", response_model=RepositoryResponse)
def post_repository(id: int, farmer_repository:FarmerRepositoryDep) :

    farmer = get(farmer_id=FarmerReference(Identified), farmer_repository=farmer_repository)
    if farmer is None:
        raise HTTPException(status_code=404)
    
    

    pass
