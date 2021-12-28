from fastapi import APIRouter, Query, Response, Request, Body, Path
from typing import Optional, List
from .schema import *
from .examples import country_index_template_examples

api = APIRouter()


@api.put("/_index_template/{indexTemplateName}",
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
def save_index_template(
        indexTemplateName: str = Path(default='country-index-template',
                                      example='country-index-template'),
        request: dict = Body(..., examples=country_index_template_examples)):
    """
        This endpoint is used to save an index template into the cluster.
        Once a template has been saved into the cluster all indexes created after that match the index pattern will have this template applied. 
    """
    return _id


@api.get("/_index_template/{indexTemplateName}",
         responses={
             200: {
                 "description": "Success",
                 "content": {
                     "application/json": {
                         "examples": {
                             "JSON Response": {
                                 "summary": "JSON Response",
                                 "value": {
                                     "index_templates": [{
                                         "name": "country-index-template",
                                         "index_template": {
                                             "index_patterns":
                                             ["country", "country*"],
                                             "template": {
                                                 "settings": {
                                                     "index": {
                                                         "number_of_shards":
                                                         "1",
                                                         "codec":
                                                         "best_compression",
                                                         "number_of_replicas":
                                                         "0"
                                                     }
                                                 },
                                                 "mappings": {
                                                     "properties": {
                                                         "countryCode": {
                                                             "type": "keyword"
                                                         }
                                                     }
                                                 }
                                             },
                                             "composed_of": [],
                                             "priority":
                                             1
                                         }
                                     }]
                                 }
                             }
                         }
                     }
                 }
             },
         })
def retrieve_index_template(indexTemplateName: str = Path(
    default="country-index-template", example="country-index-template")):
    """
       Retrieve a previously saved index template - based on the 
       specified index template name
    """
    return _id


@api.get(
    "/_index_template/",
    responses={
        200: {
            "description": "Success",
            "content": {
                "application/json": {
                    "examples": {
                        "JSON Response": {
                            "summary": "JSON Response",
                            "value": {
                                "index_templates": [{
                                    "name": "country-index-template",
                                    "index_template": {
                                        "index_patterns": ["country"],
                                        "template": {
                                            "settings": {
                                                "index": {
                                                    "number_of_shards": "1"
                                                }
                                            },
                                            "mappings": {
                                                "properties": {
                                                    "host_name": {
                                                        "type": "keyword"
                                                    }
                                                }
                                            }
                                        },
                                        "version": 3,
                                        "_meta": {
                                            "description":
                                            "my first index template"
                                        }
                                    }
                                }, {
                                    "name": "transaction-report",
                                    "index_template": {
                                        "index_patterns":
                                        ["transaction-report"],
                                        "template": {
                                            "settings": {
                                                "index": {
                                                    "max_result_window":
                                                    "20000",
                                                    "codec":
                                                    "best_compression",
                                                    "refresh_interval": "30s",
                                                    "analysis": {
                                                        "analyzer": {
                                                            "account_number_analyzer":
                                                            {
                                                                "char_filter":
                                                                [
                                                                    "account_number_filter"
                                                                ],
                                                                "tokenizer":
                                                                "standard"
                                                            }
                                                        },
                                                        "char_filter": {
                                                            "account_number_filter":
                                                            {
                                                                "pattern":
                                                                "[^0-9]",
                                                                "type":
                                                                "pattern_replace",
                                                                "replacement":
                                                                ""
                                                            }
                                                        }
                                                    },
                                                    "number_of_shards": "3",
                                                    "number_of_replicas": "0"
                                                }
                                            },
                                            "mappings": {
                                                "properties": {
                                                    "all": {
                                                        "type": "text"
                                                    },
                                                    "role": {
                                                        "type": "nested",
                                                        "properties": {
                                                            "roleType": {
                                                                "copy_to":
                                                                "all",
                                                                "type": "text",
                                                                "fields": {
                                                                    "keyword":
                                                                    {
                                                                        "ignore_above":
                                                                        256,
                                                                        "type":
                                                                        "keyword"
                                                                    }
                                                                }
                                                            },
                                                            "party": {
                                                                "type":
                                                                "nested",
                                                                "properties": {
                                                                    "address":
                                                                    {
                                                                        "type":
                                                                        "nested",
                                                                        "properties":
                                                                        {
                                                                            "country":
                                                                            {
                                                                                "copy_to":
                                                                                "all",
                                                                                "type":
                                                                                "text",
                                                                                "fields":
                                                                                {
                                                                                    "keyword":
                                                                                    {
                                                                                        "ignore_above":
                                                                                        256,
                                                                                        "type":
                                                                                        "keyword"
                                                                                    }
                                                                                }
                                                                            },
                                                                            "streetAddress":
                                                                            {
                                                                                "copy_to":
                                                                                "all",
                                                                                "type":
                                                                                "text",
                                                                                "fields":
                                                                                {
                                                                                    "keyword":
                                                                                    {
                                                                                        "ignore_above":
                                                                                        256,
                                                                                        "type":
                                                                                        "keyword"
                                                                                    }
                                                                                }
                                                                            },
                                                                            "postcode":
                                                                            {
                                                                                "copy_to":
                                                                                "all",
                                                                                "type":
                                                                                "text",
                                                                                "fields":
                                                                                {
                                                                                    "keyword":
                                                                                    {
                                                                                        "ignore_above":
                                                                                        256,
                                                                                        "type":
                                                                                        "keyword"
                                                                                    }
                                                                                }
                                                                            },
                                                                            "suburb":
                                                                            {
                                                                                "copy_to":
                                                                                "all",
                                                                                "type":
                                                                                "text",
                                                                                "fields":
                                                                                {
                                                                                    "keyword":
                                                                                    {
                                                                                        "ignore_above":
                                                                                        256,
                                                                                        "type":
                                                                                        "keyword"
                                                                                    }
                                                                                }
                                                                            },
                                                                            "state":
                                                                            {
                                                                                "copy_to":
                                                                                "all",
                                                                                "type":
                                                                                "text",
                                                                                "fields":
                                                                                {
                                                                                    "keyword":
                                                                                    {
                                                                                        "ignore_above":
                                                                                        256,
                                                                                        "type":
                                                                                        "keyword"
                                                                                    }
                                                                                }
                                                                            },
                                                                            "geolocation":
                                                                            {
                                                                                "type":
                                                                                "geo_point"
                                                                            }
                                                                        }
                                                                    },
                                                                    "identification":
                                                                    {
                                                                        "type":
                                                                        "nested",
                                                                        "properties":
                                                                        {
                                                                            "identifier":
                                                                            {
                                                                                "copy_to":
                                                                                "all",
                                                                                "type":
                                                                                "text",
                                                                                "fields":
                                                                                {
                                                                                    "keyword":
                                                                                    {
                                                                                        "ignore_above":
                                                                                        256,
                                                                                        "type":
                                                                                        "keyword"
                                                                                    }
                                                                                }
                                                                            },
                                                                            "identificationSubType":
                                                                            {
                                                                                "type":
                                                                                "text",
                                                                                "fields":
                                                                                {
                                                                                    "keyword":
                                                                                    {
                                                                                        "ignore_above":
                                                                                        256,
                                                                                        "type":
                                                                                        "keyword"
                                                                                    }
                                                                                }
                                                                            },
                                                                            "identificationType":
                                                                            {
                                                                                "copy_to":
                                                                                "all",
                                                                                "type":
                                                                                "text",
                                                                                "fields":
                                                                                {
                                                                                    "keyword":
                                                                                    {
                                                                                        "ignore_above":
                                                                                        256,
                                                                                        "type":
                                                                                        "keyword"
                                                                                    }
                                                                                }
                                                                            }
                                                                        }
                                                                    },
                                                                    "gender": {
                                                                        "copy_to":
                                                                        "all",
                                                                        "type":
                                                                        "text",
                                                                        "fields":
                                                                        {
                                                                            "keyword":
                                                                            {
                                                                                "ignore_above":
                                                                                256,
                                                                                "type":
                                                                                "keyword"
                                                                            }
                                                                        }
                                                                    },
                                                                    "jobTitle":
                                                                    {
                                                                        "copy_to":
                                                                        "all",
                                                                        "type":
                                                                        "text",
                                                                        "fields":
                                                                        {
                                                                            "keyword":
                                                                            {
                                                                                "ignore_above":
                                                                                256,
                                                                                "type":
                                                                                "keyword"
                                                                            }
                                                                        }
                                                                    },
                                                                    "name": {
                                                                        "type":
                                                                        "nested",
                                                                        "properties":
                                                                        {
                                                                            "fullName":
                                                                            {
                                                                                "copy_to":
                                                                                "all",
                                                                                "type":
                                                                                "text",
                                                                                "fields":
                                                                                {
                                                                                    "keyword":
                                                                                    {
                                                                                        "ignore_above":
                                                                                        256,
                                                                                        "type":
                                                                                        "keyword"
                                                                                    }
                                                                                }
                                                                            }
                                                                        }
                                                                    },
                                                                    "partyId":
                                                                    {
                                                                        "copy_to":
                                                                        "all",
                                                                        "type":
                                                                        "text",
                                                                        "fields":
                                                                        {
                                                                            "keyword":
                                                                            {
                                                                                "ignore_above":
                                                                                256,
                                                                                "type":
                                                                                "keyword"
                                                                            }
                                                                        }
                                                                    },
                                                                    "partyType":
                                                                    {
                                                                        "copy_to":
                                                                        "all",
                                                                        "type":
                                                                        "text",
                                                                        "fields":
                                                                        {
                                                                            "keyword":
                                                                            {
                                                                                "ignore_above":
                                                                                256,
                                                                                "type":
                                                                                "keyword"
                                                                            }
                                                                        }
                                                                    },
                                                                    "account":
                                                                    {
                                                                        "type":
                                                                        "nested",
                                                                        "properties":
                                                                        {
                                                                            "branchId":
                                                                            {
                                                                                "type":
                                                                                "text",
                                                                                "fields":
                                                                                {
                                                                                    "keyword":
                                                                                    {
                                                                                        "ignore_above":
                                                                                        256,
                                                                                        "type":
                                                                                        "keyword"
                                                                                    }
                                                                                }
                                                                            },
                                                                            "country":
                                                                            {
                                                                                "type":
                                                                                "text",
                                                                                "fields":
                                                                                {
                                                                                    "keyword":
                                                                                    {
                                                                                        "ignore_above":
                                                                                        256,
                                                                                        "type":
                                                                                        "keyword"
                                                                                    }
                                                                                }
                                                                            },
                                                                            "number":
                                                                            {
                                                                                "copy_to":
                                                                                "all",
                                                                                "analyzer":
                                                                                "account_number_analyzer",
                                                                                "type":
                                                                                "text",
                                                                                "fields":
                                                                                {
                                                                                    "keyword":
                                                                                    {
                                                                                        "ignore_above":
                                                                                        256,
                                                                                        "type":
                                                                                        "keyword"
                                                                                    }
                                                                                }
                                                                            },
                                                                            "streetAddress":
                                                                            {
                                                                                "copy_to":
                                                                                "all",
                                                                                "type":
                                                                                "text",
                                                                                "fields":
                                                                                {
                                                                                    "keyword":
                                                                                    {
                                                                                        "ignore_above":
                                                                                        256,
                                                                                        "type":
                                                                                        "keyword"
                                                                                    }
                                                                                }
                                                                            },
                                                                            "postcode":
                                                                            {
                                                                                "copy_to":
                                                                                "all",
                                                                                "type":
                                                                                "text",
                                                                                "fields":
                                                                                {
                                                                                    "keyword":
                                                                                    {
                                                                                        "ignore_above":
                                                                                        256,
                                                                                        "type":
                                                                                        "keyword"
                                                                                    }
                                                                                }
                                                                            },
                                                                            "branchName":
                                                                            {
                                                                                "type":
                                                                                "text",
                                                                                "fields":
                                                                                {
                                                                                    "keyword":
                                                                                    {
                                                                                        "ignore_above":
                                                                                        256,
                                                                                        "type":
                                                                                        "keyword"
                                                                                    }
                                                                                }
                                                                            },
                                                                            "suburb":
                                                                            {
                                                                                "copy_to":
                                                                                "all",
                                                                                "type":
                                                                                "text",
                                                                                "fields":
                                                                                {
                                                                                    "keyword":
                                                                                    {
                                                                                        "ignore_above":
                                                                                        256,
                                                                                        "type":
                                                                                        "keyword"
                                                                                    }
                                                                                }
                                                                            },
                                                                            "state":
                                                                            {
                                                                                "copy_to":
                                                                                "all",
                                                                                "type":
                                                                                "text",
                                                                                "fields":
                                                                                {
                                                                                    "keyword":
                                                                                    {
                                                                                        "ignore_above":
                                                                                        256,
                                                                                        "type":
                                                                                        "keyword"
                                                                                    }
                                                                                }
                                                                            },
                                                                            "network":
                                                                            {
                                                                                "copy_to":
                                                                                "all",
                                                                                "type":
                                                                                "text",
                                                                                "fields":
                                                                                {
                                                                                    "keyword":
                                                                                    {
                                                                                        "ignore_above":
                                                                                        256,
                                                                                        "type":
                                                                                        "keyword"
                                                                                    }
                                                                                }
                                                                            }
                                                                        }
                                                                    }
                                                                }
                                                            }
                                                        }
                                                    },
                                                    "report": {
                                                        "properties": {
                                                            "reportType": {
                                                                "type": "text",
                                                                "fields": {
                                                                    "keyword":
                                                                    {
                                                                        "ignore_above":
                                                                        256,
                                                                        "type":
                                                                        "keyword"
                                                                    }
                                                                }
                                                            },
                                                            "submissionId": {
                                                                "type":
                                                                "keyword"
                                                            },
                                                            "reportNumber": {
                                                                "type": "long"
                                                            },
                                                            "reporter": {
                                                                "type": "text",
                                                                "fields": {
                                                                    "keyword":
                                                                    {
                                                                        "ignore_above":
                                                                        256,
                                                                        "type":
                                                                        "keyword"
                                                                    }
                                                                }
                                                            },
                                                            "reporterId": {
                                                                "type":
                                                                "integer"
                                                            },
                                                            "processedDatetime":
                                                            {
                                                                "format":
                                                                "yyyy-MM-dd'T'HH:mm:ssZ||yyyy-MM-dd||strict_date_optional_time",
                                                                "type": "date"
                                                            }
                                                        }
                                                    },
                                                    "transaction": {
                                                        "properties": {
                                                            "amount": {
                                                                "type":
                                                                "double"
                                                            },
                                                            "transactionDatetime":
                                                            {
                                                                "format":
                                                                "yyyy-MM-dd'T'HH:mm:ssZ||yyyy-MM-dd||strict_date_optional_time",
                                                                "type": "date"
                                                            },
                                                            "direction": {
                                                                "type": "text",
                                                                "fields": {
                                                                    "keyword":
                                                                    {
                                                                        "ignore_above":
                                                                        256,
                                                                        "type":
                                                                        "keyword"
                                                                    }
                                                                }
                                                            }
                                                        }
                                                    }
                                                }
                                            }
                                        }
                                    }
                                }]
                            }
                        }
                    }
                }
            }
        },
    })
def retrieve_all_index_templates():
    """
       Retrieve a list of all index templates.
    """
    return _id


@api.delete("/_index_template/{indexTemplateName}",
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
def delete_index_template(indexTemplateName: str = Path(
    default="country-index-template", example="country-index-template")):
    """
       Delete a previously saved index template - based on the index template name.       
    """
    return _id
