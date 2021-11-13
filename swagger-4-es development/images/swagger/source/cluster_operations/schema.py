from pydantic import BaseModel, Field, AnyUrl 
from datetime import datetime
from typing import List, Optional, Set
from enum import Enum


class actions(BaseModel):
    auto_create_index : Optional[str]

class metadata(BaseModel):
    display_name : Optional[str]
    cluster_purpose : Optional[str]

class nestedActions(BaseModel):
    action : Optional[actions]
    cluster: Optional[metadata]

class country_model(BaseModel):
    persistent: Optional[nestedActions] 
    transient : Optional[nestedActions]

