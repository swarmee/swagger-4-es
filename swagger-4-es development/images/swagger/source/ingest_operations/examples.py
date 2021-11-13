create_index_examples = {
    "simple_index_creation": {
        "summary": "A simple index setting configuration",
        "description":
        "A **simple** index configuration. In this example we are just setting the number of shards and replicas",
        "value": {
            "settings": {
                "index": {
                    "number_of_replicas": 0
                }
            }
        }
    },
    "complex_index_creation": {
        "summary": "A more complex index settings configuration",
        "description": "A more **complex** index settings example",
        "value": {
            "settings": {
                "index": {
                    "codec": "best_compression",
                    "number_of_replicas": 0,
                    "number_of_shards": 1,
                    "refresh_interval": "30s"
                }
            }
        }
    },
    "custom_analyzer_index_creation": {
        "summary": "A custom analyzer index configuration",
        "description":
        "This example highlights how to apply a custom analyzer to a specific field.",
        "value": {
            "mappings": {
                "properties": {
                    "name": {
                        "type": "text",
                        "analyzer": "custom_analyzer",   "fields": {
                            "keyword": {
                                "type": "keyword",
                                "ignore_above": 256
                            }
                        }
                    }
                }
            },
            "settings": {
                "analysis": {
                    "analyzer": {
                        "custom_analyzer": {
                            "tokenizer":
                            "standard",
                            "filter": [
                                "lowercase", "stopword_filter",
                                "snowball_filter"
                            ]
                        }
                    },
                    "filter": {
                        "snowball_filter": {
                            "type": "snowball"
                        },
                        "stopword_filter": {
                            "type": "stop",
                            "stopwords": ["a", "the", "republic"]
                        }
                    }
                }
            }
        }
    },
    "nested_index_creation": {
        "summary": "A nested index configuration",
        "description":
        "Illustration on how to basically create subdocuments in elasticsearch",
        "value": {
            "mappings": {
                "properties": {
                    "gdp": {
                        "type": "nested",
                        "properties": {
                            "amount": {
                                "type": "long"
                            },
                            "year": {
                                "type": "long"
                            }
                        }
                    }
                }
            }
        }
    },
    # "multi_field_index_creation": {
    #     "summary":
    #     "A multifield index configuration",
    #     "description":
    #     "This example highlights how one input field (name in this example) can be indexed multiple ways. What we have setup in this example "
    #     "is the name field being processed by three analyzers; the out of the box `standard` analyzer, and two custom analyzers. The first "
    #     "using the `keyword` and `lowercase` filters the second using the the `snowball` and `lowercase` filters.",
    #     "value": {
    #         "mappings": {
    #             "properties": {
    #                 "name": {
    #                     "type": "nested",
    #                     "properties": {
    #                         "amount": {
    #                             "type": "long"
    #                         },
    #                         "year": {
    #                             "type": "long"
    #                         }
    #                     }
    #                 }
    #             }
    #         }
    #     }
    # }
}

###   "multi_field_index_creation": {

# "multi_field_index_creation": {
#     "summary":
#     "A multi-field index configuration",
#     "description":
#     "This example highlights how one input field (name in this example) can be indexed multiple ways. What we have setup in this example "
#     "is the name field being processed by three analyzers; the out of the box `standard` analyzer, and two custom analyzers. The first "
#     "using the `keyword` and `lowercase` filters the second using the the `snowball` and `lowercase` filters.",
#     "value": {
#         "mappings": {
#             "properties": {
#                 "name": {
#                     "type": "nested",
#                     "properties": {
#                         "amount": {
#                             "type": "long"
#                         },
#                         "year": {
#                             "type": "long"
#                         }
#                     }
#                 }
#             }
#         }
#     }
# }

# "simple_index_mapping": {
#     "summary": "A custom index mapping/analysis",
#     "description": "A custom index mapping/analysis configuration",
#     "value": {
#         "mappings": {
#             "properties": {
#                 "lastUpdateDatetime": {
#                     "type":
#                     "date",
#                     "format":
#                     "yyyy-MM-dd'T'HH:mm:ssZ||yyyy-MM-dd||strict_date_optional_time"
#                 },
#                 "name": {
#                     "type": "text",
#                     "fields": {
#                         "keyword": {
#                             "type": "keyword"
#                         },
#                         "snowball": {
#                             "type": "text",
#                             "analyzer": "snowball_analyzer"
#                         },
#                         "snowballWithSynonyms": {
#                             "type": "text",
#                             "analyzer": "snowball_analyzer_with_synonyms"
#                         },
#                         "lightStemmer": {
#                             "type": "text",
#                             "analyzer": "light_stemmer_analyzer"
#                         },
#                         "minimalStemmer": {
#                             "type": "text",
#                             "analyzer": "minimal_stemmer_analyzer"
#                         }
#                     }
#                 },
#                 "description": {
#                     "type": "text"
#                 },
#                 "idNumber": "long",
#                 "analyzer": "numbers_only_analyzer"
#             }
#         },
#         "settings": {
#             "analysis": {
#                 "analyzer": {
#                     "snowball_analyzer": {
#                         "tokenizer": "standard",
#                         "filter": ["lowercase", "snowball_filter"],
#                         "char_filter": ["html_strip"]
#                     },
#                     "snowball_analyzer_with_synonyms": {
#                         "tokenizer":
#                         "standard",
#                         "filter": [
#                             "lowercase", "name_synonyms_filter",
#                             "snowball_filter"
#                         ]
#                     },
#                     "numbers_only_analyzer": {
#                         "char_filter": ["number_only_char_filter"],
#                         "tokenizer": "standard"
#                     },
#                     "light_stemmer_analyzer": {
#                         "tokenizer": "standard",
#                         "filter": ["lowercase", "light_stemmer"]
#                     },
#                     "minimal_stemmer_analyzer": {
#                         "tokenizer": "standard",
#                         "filter": ["lowercase", "minimal_stemmer"]
#                     }
#                 },
#                 "filter": {
#                     "snowball_filter": {
#                         "type": "snowball"
#                     },
#                     "name_synonyms_filter": {
#                         "type":
#                         "synonym",
#                         "synonyms": [
#                             "data engineer, hadoop engineer, cloudera => software engineer",
#                             "baking, pastry chef => baker"
#                         ],
#                         "tokenizer":
#                         "standard"
#                     },
#                     "char_filter": {
#                         "number_only_char_filter": {
#                             "pattern": "[^0-9]",
#                             "type": "pattern_replace",
#                             "replacement": ""
#                         }
#                     },
#                     "light_stemmer": {
#                         "type": "stemmer",
#                         "name": "light_english"
#                     },
#                     "minimal_stemmer": {
#                         "type": "stemmer",
#                         "name": "minimal_english"
#                     }
#                 }
#             },
#             "index": {
#                 "codec": "best_compression",
#                 "refresh_interval": "1s",
#                 "number_of_shards": "1",
#                 "number_of_replicas": "0",
#             }
#         }
#     }
# }

update_index_settings_examples = {
    "update_index_setting": {
        "summary": "A update to an index setting",
        "description": "A **simple** update index setting example",
        "value": {
            "index": {
                "number_of_replicas": 2
            }
        }
    }
}
