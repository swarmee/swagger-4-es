from fastapi import APIRouter, Query, Response, Request, Body, Depends, File, Form, UploadFile, Path
from typing import Optional, List
from .schema import *
from .examples import alias_management_request_examples
from fastapi.security import HTTPBasic, HTTPBasicCredentials

api = APIRouter()


@api.post("/_aliases",
          status_code=200,
          responses={
              200: {
                  "description": "Success",
                  "content": {
                      "application/json": {
                          "examples": {
                              "JSON Response(Success)": {
                                  "summary": "JSON Response(Success)",
                                  "value": {
                                      "acknowledged": True
                                  }
                              },
                              "JSON Response(Failure)": {
                                  "summary": "JSON Response(Failure)",
                                  "value": {
                                      "error": {
                                          "root_cause": [{
                                              "type":
                                              "index_not_found_exception",
                                              "reason":
                                              "no such index [party]",
                                              "index": "party",
                                              "resource.id": "party",
                                              "resource.type":
                                              "index_or_alias",
                                              "index_uuid": "_na_"
                                          }],
                                          "type":
                                          "index_not_found_exception",
                                          "reason":
                                          "no such index [party]",
                                          "index":
                                          "party",
                                          "resource.id":
                                          "party",
                                          "resource.type":
                                          "index_or_alias",
                                          "index_uuid":
                                          "_na_"
                                      },
                                      "status": 404
                                  }
                              }
                          }
                      }
                  }
              },
          })
def management_of_index_aliases(request: dict = Body(
    ..., examples=alias_management_request_examples)):
    """
        Create, update and delete index aliases
    """
    return _id


@api.get("/_alias",
         status_code=200,
         responses={
             200: {
                 "description": "Success",
                 "content": {
                     "application/json": {
                         "examples": {
                             "JSON Response(Created)": {
                                 "summary": "JSON Response(Created)",
                                 "value": {
                                     "_index": "country",
                                     "_type": "_doc",
                                     "_id": "1",
                                     "_version": 1,
                                     "result": "created",
                                     "_shards": {
                                         "total": 1,
                                         "successful": 1,
                                         "failed": 0
                                     },
                                     "_seq_no": 0,
                                     "_primary_term": 1
                                 }
                             },
                             "JSON Response(Updated)": {
                                 "summary": "JSON Response(Updated)",
                                 "value": {
                                     "_index": "country",
                                     "_type": "_doc",
                                     "_id": "1",
                                     "_version": 2,
                                     "result": "updated",
                                     "_shards": {
                                         "total": 1,
                                         "successful": 1,
                                         "failed": 0
                                     },
                                     "_seq_no": 5,
                                     "_primary_term": 1
                                 }
                             }
                         }
                     }
                 }
             },
         })
def retrieve_all_index_aliases():
    """
    Retrieve all index aliases
    """
    return _id


@api.get("/_alias/{aliasName}",
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
                                     "country-2021": {
                                         "aliases": {
                                             "country": {
                                                 "filter": {
                                                     "bool": {
                                                         "filter": [{
                                                             "range": {
                                                                 "@timestamp":
                                                                 {
                                                                     "gte":
                                                                     "now-1d/d"
                                                                 }
                                                             }
                                                         }]
                                                     }
                                                 }
                                             }
                                         }
                                     }
                                 }
                             }
                         }
                     }
                 }
             }
         })
def retrieve_a_specific_alias(aliasName: str = Path(
    ..., description="Index alias name")):
    """
    Retrieve a specific index alias by name
    """
    return _id
