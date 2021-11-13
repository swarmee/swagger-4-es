from fastapi import APIRouter, Query, Response, Request, Body, Path
from typing import Optional, List
from .schema import *
from .examples import update_document_examples, update_document_by_query_examples
import json

api = APIRouter()


@api.post("/{index}/_update/{_id}",
          responses={
              200: {
                  "description": "Success",
                  "content": {
                      "application/json": {
                          "examples": {
                              "JSON Response": {
                                  "summary": "JSON Response",
                                  "value": {
                                      "_index": "country",
                                      "_type": "_doc",
                                      "_id": "UYIP9nsBc-WDXl5o2rS7",
                                      "_version": 4,
                                      "result": "updated",
                                      "_shards": {
                                          "total": 1,
                                          "successful": 1,
                                          "failed": 0
                                      },
                                      "_seq_no": 32,
                                      "_primary_term": 1
                                  },
                              }
                          }
                      }
                  },
              }
          })
def update_document(index: str,
                    _id: str = Path(title="Documemt _id", default="None"),
                    request: dict = Body(...,
                                         examples=update_document_examples)):
    """
        Inserting a document with an existing document _id will replace the existing document - So
        if you need to replace a whole document with a existing document just use the create document 
        with `_id` end point.
        There are two types of updates `doc` and `script`:

        - doc is used to add or update specific fields
        - script is used to perform more complex updates (e.g. adding an item to an existing list)
    """
    return _id


@api.post("/{index}/_update_by_query",
          responses={
              200: {
                  "description": "Success",
                  "content": {
                      "application/json": {
                          "examples": {
                              "JSON Response(sync)": {
                                  "summary": "JSON Response(sync)",
                                  "value": {
                                      "took": 139,
                                      "timed_out": False,
                                      "total": 3,
                                      "updated": 3,
                                      "deleted": 0,
                                      "batches": 1,
                                      "version_conflicts": 0,
                                      "noops": 0,
                                      "retries": {
                                          "bulk": 0,
                                          "search": 0
                                      },
                                      "throttled_millis": 0,
                                      "requests_per_second": -1,
                                      "throttled_until_millis": 0,
                                      "failures": []
                                  }
                              },
                              "JSON Response(async)": {
                                  "summary": "JSON Response(async)",
                                  "value": {
                                      "task": "houRpFPvSzSZe_TwFBhyFg:4125"
                                  }
                              }
                          }
                      }
                  }
              },
          })
def update_by_query(index: str = Query(
    default="country",
    description="Index Name",
),
                    wait_for_completion: bool = Query(
                        desription="submit asynchronously flag",
                        default=False),
                    request: search_model = Body(
                        ..., examples=update_document_by_query_examples)):
    """
        Delete all documents that match a query. All of the powerful search language can be used here
        to identify what needs to be deleted. Depdending on the number of documents to be deleted you 
        may choose to submit this request synchronously or asynchronously based on the `wait_for_completion`
        flag. \n
        If you choose asynchronously you are provided a `task_id` that you can use to manage the request
        at a later point.  
    """
    return _id