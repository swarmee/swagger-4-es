from fastapi import APIRouter, Query, Response, Request, Body, Path
from typing import Optional, List

from fastapi.datastructures import Default
from .schema import *
from .examples import single_country, simple_single_country, search_examples
import json

api = APIRouter()


@api.put("/_scripts/{searchTemplateName}",
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
def save_search_template(
        searchTemplateName: str = Path(default="country-search-template",
                                       example="country-search-template"),
        request: dict = Body(
            ...,
            examples={
                "simple_search_template": {
                    "summary": "A simple Search Template",
                    "description": "A **simple** search template.",
                    "value": {
                        "script": {
                            "lang": "mustache",
                            "source": {
                                "query": {
                                    "match": {
                                        "name": "{{name}}"
                                    }
                                },
                                "from": "{{from}}{{^from}}0{{/from}}",
                                "size": "{{size}}{{^size}}10{{/size}}"
                            }
                        }
                    }
                },
                "search_template_with_mulitple_criteria": {
                    "summary": "A Search Template with multiple crtiera",
                    "description":
                    "A search template with multiple criteria. ",
                    "value": {
                        "script": {
                            "lang": "mustache",
                            "source": {
                                "query": {
                                    "bool": {
                                        "should": [{
                                            "match": {
                                                "name.keyword": {
                                                    "query": "{{name}}",
                                                    "boost": 5
                                                }
                                            }
                                        }, {
                                            "match_phrase": {
                                                "name": {
                                                    "query": "{{name}}",
                                                    "slop": 1,
                                                    "boost": 3
                                                }
                                            }
                                        }, {
                                            "match": {
                                                "name": {
                                                    "query": "{{name}}",
                                                    "boost": 3
                                                }
                                            }
                                        }]
                                    }
                                },
                                "size": "{{size}}{{^size}}10{{/size}}"
                            }
                        }
                    }
                }
            })):
    """
        This endpoint is used to save a search template into the cluster. Templates are written in the [Mustache](https://mustache.github.io/) templating language. 
        Once a template has been saved into the cluster it can be used to perform queries. Search templates are really handy when you want to be able to
        simplify the queries submited from your frontend application. Basically you can hide all of the complexity of the query. It also allows you to continue to 
        make tweaks to the queries without breaking the interface to the frontend.  
    """
    ##        All saved scripts can also be accessed through the `_cluster/state` endpoint.
    return _id


@api.post("/_render/template",
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
def render_search_template(
        request:
    dict = Body(
        ...,
        examples={
            "render_supplied_template_basic": {
                "summary": "Render simple supplied template",
                "description":
                "A search template with two input parameters size and country name. The size parameter has a default value of 10.",
                "value": {
                    "source": {
                        "size": "{{size}}{{^size}}10{{/size}}",
                        "query": {
                            "match": {
                                "name": "{{name}}"
                            }
                        }
                    },
                    "params": {
                        "name": "Afghanistan",
                        "size": "4"
                    }
                },
            },
            "render_supplied_template_multiple_search_types": {
                "summary":
                "Render supplied template into multiple search types",
                "description":
                "A search template with two input parameters size and country name. The size parameter has a default value of 10.",
                "value": {
                    "source": {
                        "query": {
                            "bool": {
                                "should": [{
                                    "match": {
                                        "name.keyword": {
                                            "query": "{{name}}",
                                            "boost": 5
                                        }
                                    }
                                }, {
                                    "match_phrase": {
                                        "name": {
                                            "query": "{{name}}",
                                            "slop": 1,
                                            "boost": 3
                                        }
                                    }
                                }, {
                                    "match": {
                                        "name": {
                                            "query": "{{name}}",
                                            "boost": 3
                                        }
                                    }
                                }]
                            }
                        },
                        "size": "{{size}}{{^size}}10{{/size}}"
                    },
                    "params": {
                        "name": "Afghanistan",
                        "size": "1"
                    }
                }
            },
            # "render_supplied_template_with_list_of_search_terms": {
            #     "summary": "Render supplied template with list of search terms",
            #     "description": "Render a template with a list of search terms.",
            #     "value": {
            #         "source": """
            #                     {
            #                     "query": {
            #                         "bool": {
            #                         "must": [
            #                             {
            #                             "match": {
            #                                 "name": {{#toJson}}name{{/toJson}}
            #                             }
            #                             }
            #                         ]
            #                         }
            #                     }
            #                     }
            #         """,
            #         "params": {
            #             "name": ["Australia", "New Zealand"]
            #         }
            #     }
            # },
            "render_saved_template": {
                "summary": "Render saved template",
                "description": "Render a saved template.",
                "value": {
                    "id": "country-search-template",
                    "params": {
                        "name": "Afghanistan",
                        "size": 5
                    }
                }
            }
        })):
    """
        This end point can be used in two ways:
        - To render a query based on a supplied query template - render inline query with supplied parameter). \n
        - To render a query based on a previously saved search template - render saved query with supplied parameters).
      """
    return _id


@api.post("/{index}/_search/template",
          responses={
              200: {
                  "description": "Success",
                  "content": {
                      "application/json": {
                          "examples": {
                              "JSON Response": {
                                  "summary": "JSON Response",
                                  "value": {
                                      "took": 2,
                                      "timed_out": False,
                                      "_shards": {
                                          "total": 1,
                                          "successful": 1,
                                          "skipped": 0,
                                          "failed": 0
                                      },
                                      "hits": {
                                          "total": {
                                              "value": 1,
                                              "relation": "eq"
                                          },
                                          "max_score":
                                          0.2876821,
                                          "hits": [{
                                              "_index": "country",
                                              "_type": "_doc",
                                              "_id": "123456",
                                              "_score": 0.2876821,
                                              "_source": {
                                                  "name": "Afghanistan",
                                                  "countryCode": "AF",
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
def run_search_template(
        index: str = Path(default="country", example="country"),
        request:
    dict = Body(
        ...,
        examples={
            "run_simple_inline_search_template": {
                "summary": "Run simple inline Search Template",
                "description":
                "A **simple** example of running a search template provided inline. The search template is populated and the query executed. ",
                "value": {
                    "source": {
                        "size": "{{size}}{{^size}}10{{/size}}",
                        "query": {
                            "match": {
                                "name": "{{countryName}}"
                            }
                        }
                    },
                    "params": {
                        "countryName": "Afghanistan",
                        "size": 4
                    }
                }
            },
            "run_complex_inline_search_template": {
                "summary": "Run complex inline Search Template",
                "description":
                "A ***complex** search template with two input parameters size and country name. The search template is populated and the query executed. ",
                "value": {
                    "source": {
                        "query": {
                            "bool": {
                                "should": [{
                                    "match": {
                                        "name.keyword": {
                                            "query": "{{name}}",
                                            "boost": 5
                                        }
                                    }
                                }, {
                                    "match_phrase": {
                                        "name": {
                                            "query": "{{name}}",
                                            "slop": 1,
                                            "boost": 3
                                        }
                                    }
                                }, {
                                    "match": {
                                        "name": {
                                            "query": "{{name}}",
                                            "boost": 3
                                        }
                                    }
                                }]
                            }
                        },
                        "size": "{{size}}{{^size}}10{{/size}}"
                    },
                    "params": {
                        "name": "Afghanistan",
                        "size": "1"
                    }
                }
            },
            "run_simple_saved_search_template": {
                "summary": "Run saved Search Template",
                "description":
                "A **simple** example of running a previously saved search template. The requests identifies the saved search template and the parameters that should be used to generate the query.",
                "value": {
                    "id": "country-search-template",
                    "params": {
                        "name": "Afghanistan",
                        "size": 5
                    }
                }
            }
        })):
    """
        Similar to the ```_render/template``` endpoint this end point can be used in two ways:
        - To run a templated query with the supplied parameters where the template is provided inline. \n
        - To run a templated query with the supplied query where the template was previously saved in the cluster state.
    """
    return _id


@api.get("/_scripts/{searchTemplateName}",
         responses={
             200: {
                 "description": "Success",
                 "content": {
                     "application/json": {
                         "examples": {
                             "JSON Response": {
                                 "summary": "JSON Response",
                                 "value": {
                                     "_id": "country-search-template",
                                     "found": True,
                                     "script": {
                                         "lang": "mustache",
                                         "source": """
    {"query":{"match":{"name":"{{searchTerms}}"}},
    "from":{{from}}{{^from}}0{{/from}},
    "size":{{size}}{{^size}}10{{/size}}}
    """,
                                         "options": {
                                             "content_type":
                                             "application/json; charset=UTF-8"
                                         }
                                     }
                                 }
                             }
                         }
                     }
                 }
             },
         })
def retrieve_search_template(searchTemplateName: str = Path(
    default="country-search-template", example="country-search-template")):
    """
       Retrieve a previously saved search template - based on the 
       search template name
    """
    return _id


@api.delete("/_scripts/{searchTemplateName}",
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
def delete_search_template(searchTemplateName: str = Path(
    default="country-search-template", example="country-search-template")):
    """
       Delete a previously saved search template - based on the search template name.
       
    """
    return _id
