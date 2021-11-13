from fastapi import APIRouter, Query, Response, Request, Body, Path
from typing import Optional, List
from .schema import *
from .examples import cluster_settings_requests
import json

api = APIRouter()


# Compact and aligned text (CAT) APIsedit
# Introductionedit
# JSON is great…​ for computers. Even if it’s pretty-printed, trying to find relationships in the data is tedious. Human eyes, especially when looking at a terminal, need compact and aligned text. The compact and aligned text (CAT) APIs aim to meet this need.


@api.get("/_cat/nodes")
def node_details(
        format: str = Query(default="json"),
        h:
    str = Query(
        "ip,name,id,port,nodeRole,master,heapPercent,ramPercent,fileDescriptorPercent,diskUsedPercent,uptime",
        name="node details")):
    """
        Get Details on the Nodes in the Cluster
        E.g. find out which nodes is currently the master
    """
    return _id



@api.get("/_cluster/settings")
def retireve_cluster_settings():
    """
        Retrieve Cluster Settings
    """
    return _id


@api.put("/_cluster/settings")
def set_cluster_settings(request: dict = Body(
    ..., examples=cluster_settings_requests)):
    """
        Post Cluster Settings
    """
    return _id
