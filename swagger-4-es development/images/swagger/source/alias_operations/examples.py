alias_management_request_examples = {
    "create_alias": {
        "summary": "A simple alias creation request",
        "description": "A **simple** alias creation request.",
        "value": {
            "actions": [{
                "add": {
                    "index": "country-2021-*",
                    "alias": "country"
                }
            }]
        }
    },
    "remove_alias": {
        "summary": "A index alias removal request",
        "description": "A **simple** alias removal request.",
        "value": {
            "actions": [{
                "remove": {
                    "index": "country-2021-*",
                    "alias": "country"
                }
            }]
        }
    },
    "replace_alias": {
        "summary": "Replace a index alias request",
        "description":
        "The aliases API allows you can perform multiple actions in a **single atomic** operation.",
        "value": {
            "actions": [{
                "remove": {
                    "index": "country-2021-*",
                    "alias": "country"
                }
            }, {
                "add": {
                    "index": "country-2022-*",
                    "alias": "country"
                }
            }]
        }
    },
    "filter_alias": {
        "summary": "Create a filter alias request",
        "description": "Create an filtered alias of an index.",
        "value": {
            "actions": [{
                "add": {
                    "index": "country-2021-*",
                    "alias": "country",
                    "filter": {
                        "bool": {
                            "filter": [{
                                "range": {
                                    "@timestamp": {
                                        "gte": "now-1d/d",
                                       
                                    }
                                }
                            }]
                        }
                    }
                }
            }]
        }
    }
}
