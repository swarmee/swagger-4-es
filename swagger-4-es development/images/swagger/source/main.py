from fastapi import FastAPI, Body, Header, Depends
from pydantic import BaseModel
from typing import Optional
from create_operations import create_operations
from retrieve_operations import retrieve_operations
from update_operations import update_operations
from delete_operations import delete_operations
from alias_operations import alias_operations
from index_operations import index_operations
from text_analysis import text_analysis
from health_operations import health_operations
from ingest_operations import ingest_operations
from index_template_operations import index_template_operations
from search_templates import search_templates
from cluster_operations import cluster_operations
from fastapi.security import HTTPBasic, HTTPBasicCredentials

security = HTTPBasic()

app = FastAPI(
    title='swagger-4-es (elasticsearch)',
    root_path="/swagger",
    docs_url="/",
    servers=[{
        "url": "https://localhost/",
    }],
    root_path_in_servers=False,
    url="https://github.com/swarmee",
    version="1.0",
    description=
    ("This Swagger UI page runs through the basic [Elasticsearch](https://www.elastic.co/) API end points (it also works for [Opensearch](https://opensearch.org/) end points). "
     "It is intended to be used as a first introduction for anybody looking to pick upsome elasticsearch knowledge. \n\n"
     "The page runs through the basics of index management and the key `CRUD` operations. It then goes on to document a number of the more complex features. "
     "Sample payloads and responses have been provided for each endpoint to assist in the learning processing. "
     "Every CRUD end point requires that you specify an index name as a path parameter. "
     "For instructions on how to setup a elasticsearch cluster and connect up this Swagger UI page - head over to the "
     "[swagger-4-es Page](https://www.swarmee.net/swagger%204%20es/)."),
    long_description=(),
    long_description_content_type="text/markdown",
    openapi_tags=[
        {
            "name": "🎊 Cluster Basics",
            #  "description": "Cluster Operations 🚀",
            #  "externalDocs": {
            #      "description": "Docs",
            #      "url": "https://opensearch.org/docs/opensearch/index-data/",
            #  }
        },
        {
            "name": "✨ Index Operations",
            #  "description": "`Create` Document Operations 🚀",
            #  "externalDocs": {
            #      "description": "Docs",
            #      "url": "https://opensearch.org/docs/opensearch/index-data/",
            #  }
        },
        {
            "name": "🚀 Create Documents",
            #  "description": "`Create` Document Operations 🚀",
            #  "externalDocs": {
            #      "description": "Docs",
            #      "url": "https://opensearch.org/docs/opensearch/index-data/",
            #  }
        },
        {
            "name": "🎉 Retrieve Documents",
            # "description": "`Read` Document Operations 🚀",
            # "externalDocs": {
            #     "description": "Docs",
            #     "url": "https://opensearch.org/docs/opensearch/index-data/",
            # },
        },
        {
            "name": "🥳 Update Documents",
            # "description": "Update Document Operations 🚀",
            # "externalDocs": {
            #     "description": "Docs",
            #     "url": "https://opensearch.org/docs/opensearch/index-data/",
            # },
        },
        {
            "name": "🦄 Delete Documents",
            # "description": "`Delete` Document Operations 🚀",
            # "externalDocs": {
            #     "description": "Docs",
            #     "url": "https://opensearch.org/docs/opensearch/index-data/",
            # },
        },
        {
            "name": "🔥 Text Analysis",
            # "description": "`Delete` Document Operations 🚀",
            # "externalDocs": {
            #     "description": "Docs",
            #     "url": "https://opensearch.org/docs/opensearch/index-data/",
            # },
        },
        #  {
        #     "name": "Cluster Settings",
        #     "description": "Review and Modify Cluster Settings 🚀",
        #     "externalDocs": {
        #         "description": "Docs",
        #         "url": "https://opensearch.org/docs/opensearch/cluster/",
        #     }
        # }
    ],
    dependencies=[Depends(security)])
    

app.include_router(
    health_operations,
    #  prefix="/country",
    tags=["🎊 Cluster Basics"])

app.include_router(
    index_operations,
    #  prefix="/country",
    tags=["✨ Index Operations"])

app.include_router(update_operations, tags=["🥳 Update Documents"])

app.include_router(create_operations, tags=["🚀 Create Documents"])

app.include_router(retrieve_operations, tags=["🎉 Retrieve Documents"])

app.include_router(delete_operations, tags=["🦄 Delete Documents"])

app.include_router(text_analysis, tags=["🔥 Text Analysis"])

app.include_router(index_template_operations, tags=["🔆 Index Templates"])

app.include_router(ingest_operations, tags=["🎃 Ingest Pipelines"])

app.include_router(alias_operations, tags=["💜 Alias Operations"])

app.include_router(search_templates, tags=["💈 Search Templates"])

#### Fun emoji's for feature documentation
# ✨ Sparkles
# 💚 Green Heart
# ❗ Exclamation Mark
# 💙 Blue Heart
# 🎃 Jack-O-Lantern
# 💱 Currency Exchange
# 🔱 Trident Emblem
# 💜 Purple Heart
# 🤎 Brown Heart ☢️ Radioactive
# 🖤 Black Heart
# 🤍 White Heart
# 💯 Hundred Points
# 💢 Anger Symbol
# 💬 Speech Balloon
# 👁️‍🗨️ Eye in Speech Bubble
# 🗨️ Left Speech Bubble
# 🗯️ Right Anger Bubble
# 💭 Thought Balloon
# 💤 Zzz
# 💮 White Flower
# 🔥
# 😊

import json
from fastapi.openapi.utils import get_openapi
from copy import deepcopy

data = get_openapi(
            title=app.title,
            version=app.version,
            description=app.description,
            routes=app.routes,
            servers=app.servers,
            tags=app.openapi_tags,
        )

data1 = deepcopy(data)

for path in data['paths']:
    for methods in data['paths'][path].keys():
        for status_code in data['paths'][path][methods]['responses'].keys() :
            if status_code == "422":
                #print(data['paths'][path][methods]['responses'][status_code])
                del data1['paths'][path][methods]['responses'][status_code]



with open('./openapi/openapi.json', 'w') as outfile:
    json.dump(data1, outfile, indent=2)