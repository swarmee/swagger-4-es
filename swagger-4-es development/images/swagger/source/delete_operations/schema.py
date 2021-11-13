from pydantic import BaseModel, Field, AnyUrl
from datetime import datetime
from typing import List, Optional, Set
from enum import Enum



class currencies(BaseModel):
    code: Optional[str]
    name: Optional[str]
    symbol:  Optional[str]

class languages(BaseModel):
    iso639_1: Optional[str]
    iso639_2: Optional[str]
    name:  Optional[str]
    nativeName:  Optional[str]

class regionalBlocs(BaseModel):
    acronym: Optional[str]
    name: Optional[str]
    otherAcronyms: Optional[List[str]]
    otherNames: Optional[List[str]]

class country_model(BaseModel):
    cioc: Optional[str] 
    regionalBlocs: Optional[List[regionalBlocs]] 
    flag: Optional[AnyUrl] 
    translations: Optional[dict]  ## could list all countries here
    languages: Optional[List[languages]] 
    currencies:  Optional[List[currencies]] 
    numericCode: Optional[str] 
    nativeName: Optional[str] 
    borders: Optional[List[str]] 
    timezones: Optional[List[str]] 
    gini : Optional[float]
    area : Optional[int]
    demonym : Optional[str] 
    latlng :  Optional[List[float]]
    population : Optional[int]
    subregion : Optional[str] 
    region :     Optional[str] 
    altSpellings : Optional[List[str]] 
    capital : Optional[str] 
    name : Optional[str]
    topLevelDomain : Optional[List[str]] 
    alpha2Code:  Optional[str] 
    alpha3Code:  Optional[str] 
    callingCodes: Optional[List[int]] 
