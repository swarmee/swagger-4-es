from fastapi import APIRouter, Query, Response, Request, Body
from typing import Optional, List
from retrieve_operations.schema import *
from .schema import *
from .examples import delete_examples

api = APIRouter()


@api.delete("/{index}/_doc/{_id}",
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
                                        "_id": "1",
                                        "_version": 5,
                                        "result": "deleted",
                                        "_shards": {
                                            "total": 1,
                                            "successful": 1,
                                            "failed": 0
                                        },
                                        "_seq_no": 13,
                                        "_primary_term": 1
                                    }
                                }
                            }
                        }
                    }
                },
            })
def delete_document(
        index: str = Query(default="country",
                           description="Index Name",
                           title="Number of results to be returned",
                           example="asdfasdfasdfas"),
        _id: str = Field(default="1"),
):
    """
        Delete an individual document based on the document `_id`.
    """
    return _id


@api.post("/{index}/_delete_by_query",
          responses={
              200: {
                  "description": "Success",
                  "content": {
                      "application/json": {
                          "examples": {
                              "JSON Response(sync)": {
                                  "summary": "JSON Response(sync)",
                                  "value": {
                                      "took": 67,
                                      "timed_out": False,
                                      "total": 8,
                                      "deleted": 8,
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
def delete_by_query(index: str = Query(
    default="country",
    description="Index Name",
),
                    wait_for_completion: bool = Query(
                        desription="submit asynchronously flag",
                        default=False),
                    request: search_model = Body(...,
                                                 examples=delete_examples)):
    """
        Delete all documents that match a query. All of the powerful search language can be used here
        to identify what needs to be deleted. Depdending on the number of documents to be deleted you 
        may choose to submit this request synchronously or asynchronously based on the `wait_for_completion`
        flag. \n
        If you choose asynchronously you are provided a `task_id` that you can use to manage the request
        at a later point.  
    """
    return _id