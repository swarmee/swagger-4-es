update_document_examples = {
    "update_document_new_field": {
        "summary": "Add a field to a document",
        "description": "Add one additional field to a elasticsearch document",
        "value": {
            "doc": {
                "newField": "newFieldValue"
            }
        }
    },
    "update_document_script_remove_field": {
        "summary": "Remove a field from a document",
        "description": "Remove a field from one elasticsearch document",
        "value": {
            "script": "ctx._source.remove('newField')"
        }
    },
    "update_document_add_list": {
        "summary": "Add a list to a document",
        "description": "Add a list to an existing document",
        "value": {
            "doc": {
                "newList": [1, 3, 45, 777]
            }
        }
    },
    "update_document_add_item_to_list_if_not_present": {
        "summary": "Add an item to a list if not already present",
        "description":
        "Add an item to a list if not already present, note how the version number is not incremented and the result is `noop` when the value already exists in the list",
        "value": {
            "script": {
                "source":
                """/* first check to see if value is in the list */  if  (ctx._source.newList.contains(params.tag) != true) /* add it if not present */ {ctx._source.newList.add(params.tag)} else { ctx.op = 'none' }""",
                "lang": "painless",
                "params": {
                    "tag": 10000000000
                }
            }
        }
    }
}

update_document_by_query_examples = {
    "update_document_by_query_add_new_field": {
        "summary": "Add a field to documents that meet query",
        "description":
        "Add one additional field to all documents that meet the query",
        "value": {
            "script": {
                "source": "ctx._source.bulkAddedField = 'updateByQuery'",
                "lang": "painless"
            },
            "query": {
                "match": {
                    "subregion": "Asia"
                }
            }
        }
    },
    "update_document_by_query_remove_new_field": {
        "summary": "Remove a field from a document based on a query",
        "description": "Remove one  field to all documents that meet the query",
        "value": {
            "script": {
                "source": "ctx._source.remove('bulkAddedField')",
                "lang": "painless"
            },
            "query": {
                "match": {
                    "subregion": "Asia"
                }
            }
        }
    }
}