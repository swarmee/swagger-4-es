delete_examples = {
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
        "summary": "A match query example",
        "description": "A **normal** item works correctly.",
        "value": {
            "query": {
                "match": {
                    "region": "asia"
                }
            }
        },
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
    }
}
