from fastapi import APIRouter, Query, Response, Request, Body, Depends, Form, File
from typing import Optional, List
from .schema import *
from .examples import create_examples, bulk_create_example
from fastapi.security import HTTPBasic, HTTPBasicCredentials

api = APIRouter()


@api.get("/_cluster/health",
         responses={
             200: {
                 "description": "Success",
                 "content": {
                     "application/json": {
                         "examples": {
                             "JSON Response": {
                                 "summary":
                                 "JSON Response",
                                 "value": {
                                     "cluster_name":
                                     "swarmee",
                                     "status":
                                     "yellow",
                                     "timed_out":
                                     False,
                                     "number_of_nodes":
                                     1,
                                     "number_of_data_nodes":
                                     1,
                                     "discovered_master":
                                     True,
                                     "active_primary_shards":
                                     1,
                                     "active_shards":
                                     1,
                                     "relocating_shards":
                                     0,
                                     "initializing_shards":
                                     0,
                                     "unassigned_shards":
                                     2,
                                     "delayed_unassigned_shards":
                                     0,
                                     "number_of_pending_tasks":
                                     0,
                                     "number_of_in_flight_fetch":
                                     0,
                                     "task_max_waiting_in_queue_millis":
                                     0,
                                     "active_shards_percent_as_number":
                                     33.33333333333333
                                 }
                             }
                         }
                     }
                 }
             },
         })
def retrieve_cluster_health():
    """
        Retrieve Cluster Health \n
        Ideally your cluster is green (which means no unreplicated shards) \n
        Yellow means you have some unreplicated shards - if you create an index it may by default have mulitple shards.
    """
    return _id


# @api.get("/_cat")
# def node_details():
#     """
#         List of `cat` end points (Compact and aligned text). \n
#         Cat end points are intended for humans to read. Noting the majority have a format query parameter
#         that lets you review the data as json.
#     """
#     return _id
