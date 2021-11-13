from fastapi import APIRouter, Query, Response, Request, Body, Path
from typing import Optional, List
from .schema import *
from .examples import analysis_examples, index_analyze_examples
import json

api = APIRouter()


### Basic analyze index
@api.post("/_analyze",
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
                                      "tokens": [{
                                          "token": "johnny",
                                          "start_offset": 0,
                                          "end_offset": 6,
                                          "type": "<ALPHANUM>",
                                          "position": 0
                                      }, {
                                          "token": "5",
                                          "start_offset": 8,
                                          "end_offset": 9,
                                          "type": "<NUM>",
                                          "position": 1
                                      }, {
                                          "token": "is",
                                          "start_offset": 10,
                                          "end_offset": 12,
                                          "type": "<ALPHANUM>",
                                          "position": 2
                                      }, {
                                          "token": "alive",
                                          "start_offset": 13,
                                          "end_offset": 18,
                                          "type": "<ALPHANUM>",
                                          "position": 3
                                      }]
                                  }
                              },
                              "JSON Response(with explain equals True)": {
                                  "summary":
                                  "JSON Response(with explain equals True)",
                                  "value": {
                                      "detail": {
                                          "custom_analyzer": False,
                                          "analyzer": {
                                              "name":
                                              "standard",
                                              "tokens": [{
                                                  "token": "johnny",
                                                  "start_offset": 0,
                                                  "end_offset": 6,
                                                  "type": "<ALPHANUM>",
                                                  "position": 0,
                                                  "bytes":
                                                  "[6a 6f 68 6e 6e 79]",
                                                  "positionLength": 1,
                                                  "termFrequency": 1
                                              }, {
                                                  "token": "5",
                                                  "start_offset": 8,
                                                  "end_offset": 9,
                                                  "type": "<NUM>",
                                                  "position": 1,
                                                  "bytes": "[35]",
                                                  "positionLength": 1,
                                                  "termFrequency": 1
                                              }, {
                                                  "token": "is",
                                                  "start_offset": 10,
                                                  "end_offset": 12,
                                                  "type": "<ALPHANUM>",
                                                  "position": 2,
                                                  "bytes": "[69 73]",
                                                  "positionLength": 1,
                                                  "termFrequency": 1
                                              }, {
                                                  "token": "alive",
                                                  "start_offset": 13,
                                                  "end_offset": 18,
                                                  "type": "<ALPHANUM>",
                                                  "position": 3,
                                                  "bytes": "[61 6c 69 76 65]",
                                                  "positionLength": 1,
                                                  "termFrequency": 1
                                              }]
                                          }
                                      }
                                  }
                              }
                          }
                      }
                  }
              },
          })
def text_analysis(request: dict = Body(..., examples=analysis_examples),
                  #index: str = Path(default='country')
                  ):
    """
        The *analyze* endpoint allows you test out how your data will be analyzed and indexed.
        The default behaviour is for your search terms to be analyzed using the same analysis chain.
        E.g. if you split terms on dashes and lowercase the characters
        the same processing will be applied at index time to the documents as well as at search time to
        the searched terms. \n\n  
        Out of the box elastic comes with 8 "built-in" analyzers, which are a pre configured combination of:
        - Character Filters, 
        - Tokenizers, and
        - Token Filters  \n 
        Popular analyzers include:
        - Standard - which tokenizes based on unicode text logic, removes punctuation and lowercases terms. 
        - Keyword - which basically preforms no analysis, including no tokenization (e.g. a phase comes in and comes out a phase).
        - Simple - which tokenizes whenever it hits a character that is not a letter.
        - Stop - which removes stop words (based off the simple analyzer). \n
        If the out of the box analyzers don't meet your requirements, you can create your own analysis chain (i.e. analyzer).
        Which basically just involves stringing together the avaliable `Character Filters`, `Tokenizers` and `Token Filters`. 
        Examples of each are provided below:
        <details><summary>Character Filters - preprocess characters before passed to tokenizer</summary>
        Character filters include: \n
        - **Mapping** - maps text (e.g. `:)` = good/happy). \n 
        - **HTML Strip** - basically tries to remove HTML garbage from text before indexing. \n 
        - **Pattern Replace** - firstly I've never had a need to use this character filter. It allows you to use regex to fiddle with the text. \n 
        </p>
        </details>
        <details><summary>Tokenization - how the text is broken down into tokens</summary>
        Avaliable tokenizers include: \n
        - **Letter** (breaks on non leters) \n 
        - **Standard** (grammer based tokenisation) - note however the apostrophe `s` is kept with the preceding word   \n 
        - **Classic** (pretty good for english however `standard` is preferred now with most general language support) \n 
        - **Ngram** (ngrams for all tokens) - default is min_gram 1 and max_gram 2 \n
        - **Edge_ngram** (ngrams from the edges) - default is min_gram 1 and max_gram 2  \n
        - **Keyword** (no tokenization) \n\n 
        </p>
        </details>
        <details><summary>Token Filters - processing of tokens (add, modify, delete) from tokenizer</summary>
        Avaliable Token Filters include: \n
        - **Apostrophe** - removes apostrophe and text following the apostrophe (e.g. john's becomes john) \n 
        - **Stopwords** - removes configured stopwords so they are not indexed. \n 
        - **stemmer** - which supports a number of stemming algorithms. \n 
        - **Snowball** - snowball stemming of terms. \n         
        </p>
        </details>
        \n\n
        Note: including `"explain" : true` in the request payload will allow you to review the full analysis chain. 
        
    """
    return {}


### Basic analyze index
@api.post("/{index}/_analyze",
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
                                      "tokens": [{
                                          "token": "jumping",
                                          "start_offset": 0,
                                          "end_offset": 7,
                                          "type": "<ALPHANUM>",
                                          "position": 0
                                      }, {
                                          "token": "jack's",
                                          "start_offset": 8,
                                          "end_offset": 14,
                                          "type": "<ALPHANUM>",
                                          "position": 1
                                      }, {
                                          "token": "jumpers",
                                          "start_offset": 15,
                                          "end_offset": 22,
                                          "type": "<ALPHANUM>",
                                          "position": 2
                                      }]
                                  }
                              }
                          }
                      }
                  }
              }
          })
def text_analysis_for_specific_index(request: dict = Body(
    ..., examples=index_analyze_examples),
                                     index: str = Path(default='country')):
    """
       Analyze how text would be analyzed for a specific index. \n
       Including `"explain" : true` in the request will allow you to review the full analysis chain. 
        
    """
    return {}


# ### List indexes
# @api.get("/_cat/indices",
#          responses={
#              200: {
#                  "description": "Success",
#                  "content": {
#                      "application/json": {
#                          "examples": {
#                              "JSON Response": {
#                                  "summary":
#                                  "JSON Response",
#                                  "value": [{
#                                      "health": "green",
#                                      "status": "open",
#                                      "index": "country",
#                                      "uuid": "jNi87tzhRgyDCnyqSeaWDQ",
#                                      "pri": "1",
#                                      "rep": "0",
#                                      "docs.count": "0",
#                                      "docs.deleted": "0",
#                                      "store.size": "208b",
#                                      "pri.store.size": "208b"
#                                  }, {
#                                      "health": "green",
#                                      "status": "open",
#                                      "index": "test",
#                                      "uuid": "Xk6o3Nv6QnqG2POSufHJaA",
#                                      "pri": "1",
#                                      "rep": "0",
#                                      "docs.count": "0",
#                                      "docs.deleted": "0",
#                                      "store.size": "208b",
#                                      "pri.store.size": "208b"
#                                  }]
#                              }
#                          }
#                      }
#                  }
#              },
#          })
# def list_indices(v: bool = Query(None),
#                  format: format_types = Query(default="column")):
#     """
#         `cat` stands for Compact and Aligned Text - there are many elasticserch endpoints under `_cat` \n
#         These endpoints are meant for humans to read as the text is neatly aligned in columns. \n
#         However they have evolved to have a format parameter so you can get `json` back from them also.\n
#         This `cat` endpoint list indices and provides their state \n
#         The **v** parameter toggles the column headings on and off in the column view.
#     """
#     return _id

# @api.get("/{index}/",
#          responses={
#              200: {
#                  "description": "Success",
#                  "content": {
#                      "application/json": {
#                          "examples": {
#                              "JSON Response": {
#                                  "summary": "JSON Response",
#                                  "value": {
#                                      "country": {
#                                          "aliases": {},
#                                          "mappings": {},
#                                          "settings": {
#                                              "index": {
#                                                  "creation_date":
#                                                  "1631913972854",
#                                                  "number_of_shards": "1",
#                                                  "number_of_replicas": "0",
#                                                  "uuid":
#                                                  "yQ8dF5otQ5SKHyWQYlr9Jw",
#                                                  "version": {
#                                                      "created": "135217827"
#                                                  },
#                                                  "provided_name": "country"
#                                              }
#                                          }
#                                      }
#                                  }
#                              }
#                          }
#                      }
#                  }
#              },
#          })
# def view_index_details(index: str = Query("country")):
#     """
#         View the aliases, mappings and settings for an index.

#         _**Aliases**_ are similar to table views from sql land - i.e. they don't hold data - they just point to one or more indexes. \n
#         _**Mappings**_ defines the type of each field and how it is indexes \n
#         _**Settings**_ defines the index level configuration.
#     """
#     return _id

# ### Update Index
# @api.put("/{index}/_settings",
#          responses={
#              200: {
#                  "description": "Success",
#                  "content": {
#                      "application/json": {
#                          "examples": {
#                              "JSON Response": {
#                                  "summary": "JSON Response",
#                                  "value": {
#                                      "acknowledged": True
#                                  }
#                              }
#                          }
#                      }
#                  }
#              },
#          })
# def update_index_settings(index: str,
#                           request: dict = Body(
#                               ..., examples=update_index_settings_examples)):
#     """
#         Update an existing indexes settings. \n
#         For example you might want to build an index with settings optimised for speed, however once its built you might want to optimise for redundancy (e.g. increasing the number of replicates), \n
#         **Not** all index settings can be changed once an index is created.
#     """
#     return _id

# ### Delete Index
# @api.delete("/{index}/",
#             responses={
#                 200: {
#                     "description": "Success",
#                     "content": {
#                         "application/json": {
#                             "examples": {
#                                 "JSON Response": {
#                                     "summary": "JSON Response",
#                                     "value": {
#                                         "acknowledged": True
#                                     }
#                                 }
#                             }
#                         }
#                     }
#                 },
#             })
# def delete_index(index: str = Query(default="country",
#                                     description="Index to be deleted",
#                                     title="The index name",
#                                     example="country")):
#     """
#         Delete an index (and all documents contained within the index)\n
#         These types of endpoints support asterisk (`*`) as a wild. \n
#         This is really helpful when you need to delete indices which have the date in the index name. E.g.; \n
#         ``` bash
#         curl -X 'DELETE' 'https://localhost/2020-01-*-applogs/'
#         ```
#         But be careful.
#     """
#     return _id
