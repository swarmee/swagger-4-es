search_examples = {
    "match_all_query": {
        "summary": "A match all example",
        "value": {
            "query": {
                "match_all": {                }
            }
        }
    },    
    "query_string_query": {
        "summary": "A query string example",
        "value": {
            "query": {
                "query_string": {
                    "query": "af"
                }
            }
        }
    },
    "match_query": {
        "summary":
        "A match query example",
        "description":
        "With the default mapping `Bermuda Republic` is not found and the name in the source document is `The Bermudas`. "
        "however when the index is created with the supplied mapping (which leverages a custom analyzer) then `Bermuda Republic` is a match for `The Bermudas`. "
        "The reason being is that the source document and the search terms are processed to both become `Bermuda`",
        "value": {
            "query": {
                "match": {
                    "name": "Bermuda Republic"
                }
            }
        }
    },
    "range_query": {
        "summary": "A range query example",
        "description":
        "Basically return all country documents with an area of greater than or equal to `1`",
        "value": {
            "query": {
                "range": {
                    "area": {
                        "gte": 1
                    }
                }
            }
        },
    },
    "sub_document_query_without_nesting": {
        "summary": "Subdocument querying without index nesting",
        "description":
        "Subdocument querying without index nesting. This incorrectly returns `The Bermudas` document. \n"
        "Basically what is saved without index nesting is gdp.year = [`2010`, `2020`] and gdp.amount = [`6000000000`, `8000000000`]."
        "There is no correlation between the sub documents. ",
        "value": {
            "query": {
                "bool": {
                    "must": [{
                        "range": {
                            "gdp.year": {
                                "lte": 2015
                            }
                        }
                    }, {
                        "range": {
                            "gdp.amount": {
                                "gte": 7000000000
                            }
                        }
                    }]
                }
            }
        }
    },
    "sub_document_query_with_nesting": {
        "summary": "Subdocument querying with index nesting configured",
        "description":
        "Subdocument querying with index nesting. This correctly does not return the `The Bermudas` document",
        "value": {
            "query": {
                "nested": {
                    "path": "gdp",
                    "query": {
                        "bool": {
                            "must": [{
                                "range": {
                                    "gdp.year": {
                                        "lte": 2015
                                    }
                                }
                            }, {
                                "range": {
                                    "gdp.amount": {
                                        "gte": 7000000000
                                    }
                                }
                            }]
                        }
                    }
                }
            }
        }
    },
    # "multi_field_name_query": {
    #     "summary":
    #     "A multifield query example",
    #     "description":
    #     "A boolean query across the `name` field indexed by three different analyzers. The higher quality analyzers are boosted. This query also demostrates named queries. "
    #     "Allowing you to see which sub queries hit the underlying document.",
    #     "value": {
    #         "query": {
    #             "bool": {
    #                 "should": [{
    #                     "match": {
    #                         "alternativeName.keyword": {
    #                             "query": "Jumping Jack's Jumpers",
    #                             "_name": "name.keyword",
    #                             "boost": 3
    #                         }
    #                     }
    #                 }, {
    #                     "match": {
    #                         "alternativeName": {
    #                             "query": "Jumping Jack's Jumpers",
    #                             "_name": "alternativeName.standard",
    #                             "operator": "AND",
    #                             "boost": 2
    #                         }
    #                     }
    #                 }, {
    #                     "match": {
    #                         "alternativeName.snowball": {
    #                             "query": "Jumping Jack's Jumpers",
    #                             "_name": "alternativeName.snowball",
    #                             "operator": "and",
    #                             "boost": 1
    #                         }
    #                     }
    #                 }]
    #             }
    #         }
    #     }
    # }
}

simple_single_country = {
    "name": "Afghanistan",
    "alpha2Code": "AF",
    "capital": "Kabul",
    "region": "Asia",
    "subregion": "Southern Asia"
}

single_country = {
    "name":
    "Afghanistan",
    "topLevelDomain": [".af"],
    "alpha2Code":
    "AF",
    "alpha3Code":
    "AFG",
    "callingCodes": ["93"],
    "capital":
    "Kabul",
    "altSpellings": ["AF", "Afġānistān"],
    "region":
    "Asia",
    "subregion":
    "Southern Asia",
    "population":
    27657145,
    "latlng": [33, 65],
    "demonym":
    "Afghan",
    "area":
    652230,
    "gini":
    27.8,
    "timezones": ["UTC+04:30"],
    "borders": ["IRN", "PAK", "TKM", "UZB", "TJK", "CHN"],
    "nativeName":
    "افغانستان",
    "numericCode":
    "004",
    "currencies": [{
        "code": "AFN",
        "name": "Afghan afghani",
        "symbol": "؋"
    }],
    "languages": [{
        "iso639_1": "ps",
        "iso639_2": "pus",
        "name": "Pashto",
        "nativeName": "پښتو"
    }, {
        "iso639_1": "uz",
        "iso639_2": "uzb",
        "name": "Uzbek",
        "nativeName": "Oʻzbek"
    }, {
        "iso639_1": "tk",
        "iso639_2": "tuk",
        "name": "Turkmen",
        "nativeName": "Türkmen"
    }],
    "translations": {
        "de": "Afghanistan",
        "es": "Afganistán",
        "fr": "Afghanistan",
        "ja": "アフガニスタン",
        "it": "Afghanistan",
        "br": "Afeganistão",
        "pt": "Afeganistão",
        "nl": "Afghanistan",
        "hr": "Afganistan",
        "fa": "افغانستان"
    },
    "flag":
    "https://restcountries.eu/data/afg.svg",
    "regionalBlocs": [{
        "acronym": "SAARC",
        "name": "South Asian Association for Regional Cooperation",
        "otherAcronyms": [],
        "otherNames": []
    }],
    "cioc":
    "AFG"
}
