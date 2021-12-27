# swagger-4-es Dev

This folder contains the fastapi app that is used to generate the Swagger UI specification for elasticsearch/opensearch. 


https://localhost/swagger/   -- for the fastapi swagger page (path based routing)
https://localhost/docs/index.html -- for the swagger ui page (.html and .json based routing)
https://localhost/  -- for Opensearch (default routing)
https://localhost/dashboards/   -- for the Opensearch Kibana equivalent - which is called ```Dashboards```.

The openapi specification is passed through the ```openapi-fiddle.ipynb``` notebook to remove the 422 error response from the openapi specification. 