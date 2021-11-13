from fastapi import APIRouter, Query, Response, Request, Body, Path
from typing import Optional, List
from .schema import *
from .examples import create_index_examples, update_index_settings_examples
import json

api = APIRouter()


### List indexes
@api.get("/_cat/indices",
         responses={
             200: {
                 "description": "Success",
                 "content": {
                     "application/json": {
                         "examples": {
                             "JSON Response": {
                                 "summary":
                                 "JSON Response",
                                 "value": [{
                                     "health": "green",
                                     "status": "open",
                                     "index": "country",
                                     "uuid": "jNi87tzhRgyDCnyqSeaWDQ",
                                     "pri": "1",
                                     "rep": "0",
                                     "docs.count": "0",
                                     "docs.deleted": "0",
                                     "store.size": "208b",
                                     "pri.store.size": "208b"
                                 }, {
                                     "health": "green",
                                     "status": "open",
                                     "index": "test",
                                     "uuid": "Xk6o3Nv6QnqG2POSufHJaA",
                                     "pri": "1",
                                     "rep": "0",
                                     "docs.count": "0",
                                     "docs.deleted": "0",
                                     "store.size": "208b",
                                     "pri.store.size": "208b"
                                 }]
                             }
                         }
                     }
                 }
             },
         })
def list_indices(v: bool = Query(None),
                 format: format_types = Query(default="column")):
    """
        `cat` stands for Compact and Aligned Text - there are many elasticserch endpoints under `_cat` \n 
        These endpoints are meant for humans to read as the text is neatly aligned in columns. \n
        However they have evolved to have a format parameter so you can get `json` back from them also.\n
        This `cat` endpoint list indices and provides their state \n
        The **v** parameter toggles the column headings on and off in the column view.  
    """
    return {}


### Create index
@api.put("/{index}/",
         status_code=200,
         responses={
             200: {
                 "description": "Success",
                 "content": {
                     "application/json": {
                         "examples": {
                             "JSON Response": {
                                 "summary": "JSON Response",
                                 "value": {
                                     "acknowledged": True,
                                     "shards_acknowledged": True,
                                     "index": "country"
                                 }
                             }
                         }
                     }
                 }
             },
         })
def create_index(request: dict = Body(..., examples=create_index_examples),
                 index: str = Path(default='country', example="country")):
    """
        Create an empty index in elasticsearch with a predefined configuration. \n
        Over time you will probably want to look at index templates - however you need to understand the fundamentals of index settings. \n 
        Below are a number of index configurations. 
    """
    return {}


@api.get("/{index}/",
         responses={
             200: {
                 "description": "Success",
                 "content": {
                     "application/json": {
                         "examples": {
                             "JSON Response": {
                                 "summary": "JSON Response",
                                 "value": {
                                     "country": {
                                         "aliases": {},
                                         "mappings": {},
                                         "settings": {
                                             "index": {
                                                 "creation_date":
                                                 "1631913972854",
                                                 "number_of_shards": "1",
                                                 "number_of_replicas": "0",
                                                 "uuid":
                                                 "yQ8dF5otQ5SKHyWQYlr9Jw",
                                                 "version": {
                                                     "created": "135217827"
                                                 },
                                                 "provided_name": "country"
                                             }
                                         }
                                     }
                                 }
                             }
                         }
                     }
                 }
             },
         })
def view_index_details(index: str = Path(default="country", example="country")):
    """
        View the aliases, mappings and settings for an index.

        _**Aliases**_ are similar to table views from sql land - i.e. they don't hold data - they just point to one or more indexes. \n
        _**Mappings**_ defines the type of each field and how it is indexes \n
        _**Settings**_ defines the index level configuration.   
    """
    return {}


### Update Index
@api.put("/{index}/_settings",
         responses={
             200: {
                 "description": "Success",
                 "content": {
                     "application/json": {
                         "examples": {
                             "JSON Response": {
                                 "summary": "JSON Response",
                                 "value": {
                                     "acknowledged": True
                                 }
                             }
                         }
                     }
                 }
             },
         })
def update_index_settings(index: str = Path(default="country", example="country"),
                          request: dict = Body(
                              ..., examples=update_index_settings_examples)):
    """
        Update an existing indexes settings. \n
        For example you might want to build an index with settings optimised for speed, however once its built you might want to optimise for redundancy (e.g. increasing the number of replicates), \n
        **Not** all index settings can be changed once an index is created.  
    """
    return _id


### Delete Index
@api.delete("/{index}/",
            responses={
                200: {
                    "description": "Success",
                    "content": {
                        "application/json": {
                            "examples": {
                                "JSON Response": {
                                    "summary": "JSON Response",
                                    "value": {
                                        "acknowledged": True
                                    }
                                }
                            }
                        }
                    }
                },
            })
def delete_index(index: str = Path(default="country",
                                    description="Index to be deleted",
                                    title="The index name",
                                    example="country")):
    """
        Delete an index (and all documents contained within the index)\n
        These types of endpoints support asterisk (`*`) as a wild. \n
        This is really helpful when you need to delete indices which have the date in the index name. E.g.; \n
        ``` bash
        curl -X 'DELETE' 'https://localhost/2020-01-*-applogs/' 
        ```
        But be careful.
    """
    return _id


