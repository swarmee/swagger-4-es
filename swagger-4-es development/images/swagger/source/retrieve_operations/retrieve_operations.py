from fastapi import APIRouter, Query, Response, Request, Body, Path
from typing import Optional, List

from fastapi.datastructures import Default
from .schema import *
from .examples import single_country, simple_single_country, search_examples
import json

api = APIRouter()


@api.get("/{index}/_doc/{_id}",
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
                                     "_version": 4,
                                     "_seq_no": 3,
                                     "_primary_term": 1,
                                     "found": True,
                                     "_source": {
                                         "name": "Afghanistan",
                                         "alpha2Code": "AF",
                                         "capital": "Kabul",
                                         "region": "Asia",
                                         "subregion": "Southern Asia",
                                         "area": 652230
                                     }
                                 }
                             }
                         }
                     }
                 }
             },
         })
def retrieve_document_by_id(index: str = Path(default="country",
                                              example="country"),
                            _id: str = Path(default="1", example="1")):
    """
        This end point simply retrieves a document based on the provided `_id`. \n
        Note the structure of the document returned:
        - At the top level we have various meta data about the document (e.g. `index` and `version`). \n
        - The original document is nested in a field called `_source`. 
    """
    return _id


@api.post("/{index}/_search",
          responses={
              200: {
                  "description": "Success",
                  "content": {
                      "application/json": {
                          "examples": {
                              "JSON Response": {
                                  "summary": "JSON Response",
                                  "value": {
                                      "took": 26,
                                      "timed_out": False,
                                      "_shards": {
                                          "total": 1,
                                          "successful": 1,
                                          "skipped": 0,
                                          "failed": 0
                                      },
                                      "hits": {
                                          "total": {
                                              "value": 3,
                                              "relation": "eq"
                                          },
                                          "max_score":
                                          0.036367644,
                                          "hits": [{
                                              "_index": "country",
                                              "_type": "_doc",
                                              "_id": "1",
                                              "_score": 0.036367644,
                                              "_source": {
                                                  "name": "Afghanistan",
                                                  "alpha2Code": "AF",
                                                  "capital": "Kabul",
                                                  "region": "Asia",
                                                  "subregion": "Southern Asia",
                                                  "area": 652230
                                              }
                                          }, {
                                              "_index": "country",
                                              "_type": "_doc",
                                              "_id": "5",
                                              "_score": 0.036367644,
                                              "_source": {
                                                  "name": "Afghanistan",
                                                  "alpha2Code": "AF",
                                                  "capital": "Kabul",
                                                  "region": "Asia",
                                                  "subregion": "Southern Asia",
                                                  "area": 652230
                                              }
                                          }, {
                                              "_index": "country",
                                              "_type": "_doc",
                                              "_id": "UIK69XsBc-WDXl5oS7Q1",
                                              "_score": 0.036367644,
                                              "_source": {
                                                  "name": "Afghanistan",
                                                  "alpha2Code": "AF",
                                                  "capital": "Kabul",
                                                  "region": "Asia",
                                                  "subregion": "Southern Asia",
                                                  "area": 652230
                                              }
                                          }]
                                      }
                                  }
                              }
                          }
                      }
                  }
              },
          })
def retrieve_documents_by_search(index: str = Path(default="country",
                                                   example="country"),
                                 size: Optional[int] = 10,
                                 request: search_model = Body(
                                     None, examples=search_examples)):
    """
        This is the most feature rich endpoint in elasticsearch - coming from sql the searches that you can
        perform will **blown your mind**. \n
        We will just cover the basics here now - but lots more to come on this. 
        A number of example query types have been provided. \n 
        This end point can also been used to sample some documents when submitted without a request body 
        (i.e. with no search parameters). By default only ten documents will be returned. \n
        The sample response shows illustrates the structure that will be returned. 
        At the top level we have details about the search execution (e.g. `took`, `timed_out` and shard details)
        Then we have a `hits` key which has summary details on the search (e.g. `max_score` and `total` hits)
        as well as sub `hits` key which lists the search results in score order.  
    """
    return _id
