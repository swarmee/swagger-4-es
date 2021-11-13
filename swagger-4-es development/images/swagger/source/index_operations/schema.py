from pydantic import BaseModel, Field, AnyUrl 
from datetime import datetime
from typing import List, Optional, Set
from enum import Enum


class format_types(str, Enum):
    json = "json"
    column = "column"