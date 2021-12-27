from fastapi import APIRouter, Query, Response, Request, Body, Path
from typing import Optional, List
from .schema import *
from .examples import *
import json

api = APIRouter()


@api.put("/_ingest/pipeline/{ingestPipelineName}",
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
def save_ingest_pipeline(
        ingestPipelineName: str = Path(default='test-pipeline',
                                       example='test-pipeline'),
        request: dict = Body(
            ...,
            examples={
                "simple_pipeline": {
                    "summary": "A simple pipeline configuration",
                    "description": "Just adds a field to all documents.",
                    "value": {
                        "description":
                        "Add field example",
                        "processors": [{
                            "set": {
                                "description": "Add field processor",
                                "field": "important-field",
                                "value": "added-field"
                            }
                        }]
                    }
                },
                "add_timestamp_pipeline": {
                    "summary": "A timestamp pipeline configuration",
                    "description": "Adds timestamp to documents. We also add a date processor to remove the nanos and milliseconds",
                    "value": {
                        "description":
                        "Add timestamp to documents",
                        "processors": [{
                            "set": {
                                "field": "@timestamp",
                                "value": "{{_ingest.timestamp}}"
                            }
                        }, {
                            "date": {
                                "field": "@timestamp",
                                "target_field": "@timestamp",
                                "formats": ["strict_date_optional_time_nanos"],
                                "output_format": "basic_date_time_no_millis"
                            }
                        }]
                    }
                },
                "allocate_document_to_datetime_index_pipeline": {
                    "summary": "Allocate the document to a datetime index",
                    "description": "Adds timestamp to documents.",
                    "value": {
                        "description":
                        "Add timestamp to documents",
                        "processors": [{
                            "set": {
                                "field": "@timestamp",
                                "value": "{{_ingest.timestamp}}"
                            }
                        }, {
                            "date_index_name": {
                                "field": "@timestamp",
                                "index_name_prefix": "country-",
                                "date_formats":
                                ["strict_date_optional_time_nanos"],
                                "date_rounding": "M",
                                "timezone": "Australia/Sydney"
                            }
                        }]
                    }
                }
            })):
    """
        This endpoint is used to save an ingest pipelines into the cluster state. 
    """
    return _id


@api.get("/_ingest/pipeline/{ingestPipelineName}",
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
def retrieve_ingest_pipeline(ingestPipelineName: str = Path(
    default='test-pipeline', example='test-pipeline')):
    """
       Retrieve a previously saved ingest pipeline - based on the 
       specified ingest pipeline name
    """
    return _id


@api.delete("/_ingest/pipeline/{ingestPipelineName}",
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
def delete_ingest_pipeline(ingestPipelineName: str = Path(
    default='test-pipeline', example='test-pipeline')):
    """
       Delete a previously saved ingest pipeline - based on the ingest pipeline name.       
    """
    return _id


@api.post("/_ingest/pipeline/{ingestPipelineName}/_simulate",
          responses={
              200: {
                  "description": "Success",
                  "content": {
                      "application/json": {
                          "examples": {
                              "template_output": {
                                  "query": {
                                      "match": {
                                          "name": "France"
                                      }
                                  },
                                  "from": "20",
                                  "size": "10"
                              }
                          }
                      }
                  }
              },
          })
def simulate_ingest_pipeline(
        ingestPipelineName: str = Path(default='test-pipeline',
                                       example='test-pipeline'),
        request:
    dict = Body(
        ...,
        examples={
            "simple_index_creation": {
                "summary": "A simple index setting configuration",
                "description":
                "A **simple** index configuration. In this example we are just setting the number of shards and replicas",
                "value": {
                    "docs": [{
                        "_index": "index",
                        "_id": "id",
                        "_source": {
                            "country": "Australia"
                        }
                    }, {
                        "_index": "index",
                        "_id": "id",
                        "_source": {
                            "country": "New Zealand"
                        }
                    }]
                }
            }
        })):
    """
        Process a series of documents against a specified ingest pipeline. 
      """
    return _id

    # responses={
    #     200: {
    #         "description": "Success",
    #         "content": {
    #             "application/json": {
    #                 "examples": {
    #                     "JSON Response": {
    #                         "summary": "JSON Response",
    #                         "value": {
    #                             "acknowledged": True
    #                         }
    #                     }
    #                 }
    #             }
    #         }
    #     },
    # }