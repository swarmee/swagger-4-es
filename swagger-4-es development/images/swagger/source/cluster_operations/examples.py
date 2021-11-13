cluster_settings_requests = {
    "change_auto_create_index": {
        "summary": "Set the auto create index flag",
        "description": "Set the auto create index flag to true",
        "value": {
            "persistent": {
                "action": {
                    "auto_create_index": "true"
                }
            }
        }
    },
    "change_cluster_metadata": {
        "summary": "Change Cluster Metadata",
        "description": "Change Cluster Metadata",
        "value": {
            "persistent": {
                "cluster": {
                    "metadata": {
                        "display_name": "swarmee",
                        "cluster_purpose": "testing"
                    }
                }
            }
        }
    },
    "remove_read_only_cluster": {
        "summary": "Change Cluster Read Only Seeting",
        "description":
        "Some times often when there are space issues a cluster will set itself to read only. This request reverses this read only setting",
        "value": {
            "persistent": {
                "cluster": {
                    "blocks": {
                        "read_only": False
                    }
                }
            }
        }
    }
}
