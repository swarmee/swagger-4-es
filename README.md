`Swagger-4-es` provides a Swagger UI page for the key elasticsearch (and Opensearch) endpoints. It's aimed at being a training resource to engineers starting off with elasticsearch. You may also consider customising the openapi specification (additional endpoints and notes) to become a training resource specific to your organisation.   

There are two ways you can use the Swagger UI page:

1. From this website, by [clicking here](https://www.swarmee.net/swagger-4-es/swagger.html). This will allow you to connect to a cloud based elasticsearch cluster (that is enabled for CORS). This setup option is by far the easiest for beginners, there is no need to setup any software on your PC. After clicking this link you will be asked to provide the URL of your elasticsearch cluster - you can follow the instructions [here](https://www.swarmee.net/swagger-4-es/elasticsearch-cloud-instance-setup/) for setting up an elasticsearch cloud instance. 

2. Cloning the [swagger-4-es](https://github.com/swarmee/swagger-4-es) repository, and running an opensearch (elasticsearch compatible) and nginx container locally, this option requires you to have docker and docker-compose setup on your PC , instructions on this can be found below. 

<details><summary>Local Cluster Setup Steps</summary>      

Follow these steps if you are going with the second option above. 

### Prerequisite

The following software and configuration is required on your computer to boot up the containers:

- `docker`. See these [docs](https://docs.docker.com/get-docker/) for instructions.
- `docker-compose`. See these [docs](https://docs.docker.com/compose/install/) for instructions.
- Increase the `mmap` count on linux systems. See these [docs](https://www.elastic.co/guide/en/elasticsearch/reference/current/vm-max-map-count.html) for instructions.


### Usage

```shell
docker-compose up
```

Then open [https://localhost/index.html](https://index/swagger.html) to see the Swagger UI page.

**Noting**:

- The local cluster is actually a [Opensearch](https://opensearch.org/) cluster - however this is compatible with Elasticsearch 7.10.2.
- The Opensearch cluster will take a little while to boot up - at least 15 seconds (you should see the messages scrolling through on your terminal as it starts up).
- The container starts a nginx reverse proxy to host the Swagger UI page, it generates a self signed certificate so you will need to accept the warning message in your browser. I.e. it is expected to see a `Warning: Potential Security Risk Ahead` message when you open the Swagger UI link (Click Proceed).
- No authentication is required for the local cluster. 

The cluster is also avaliable directly at [http://localhost:9200](http://localhost:9200)

</details>

<details><summary>How to Create Your Own Swagger UI page for Elastic</summary>    

The way to set this up fo yourself is very straight forward:

1. Document your schema as a `openapi.json` file - [Swagger Hub](https://app.swaggerhub.com) can help with this.
2. Copy the `dist` folder from the [Swagger UI](https://github.com/swagger-api/swagger-ui/blob/master/docs/usage/installation.md) github page.
3. Drop in your `openapi.json` from step one into the same folder as the HTML index file.
4. change the `url` parameter in the `index.html` to "./openapi.json". so it looks like this :

```javascript
const ui = SwaggerUIBundle({
  url: "./openapi.json",
  dom_id: "#swagger-ui",
  defaultModelsExpandDepth: -1,
  defaultModelExpandDepth: -1,
  docExpansion: "none",
  displayRequestDuration: true,
  useUnsafeMarkdown: true,
  deepLinking: true,
  presets: [SwaggerUIBundle.presets.apis, SwaggerUIStandalonePreset],
  plugins: [SwaggerUIBundle.plugins.DownloadUrl],
  layout: "StandaloneLayout",
});
```

It's also possible to include the openapi schema directly in the `index.html` file. To do this replace the `url` parameter with the `spec` parameter and make it equal the openapi schema. 

</details>

<details><summary>Why Create Your Own Swagger UI Page</summary>    


Why would you want to setup your own Swagger Page to Elasticsearch:

- Documenting the key endpoints saves a lot of google searching for precise parameters and lets you annotate specific end points (e.g. issues in dev/test check to see if the cluster has gone read-only due to space constraints). The example Swagger UI page provided in the repo demonstrates how to use the Swagger UI page for basic elasticsearch training.   

- It's also much more precise and faster to go to a Swagger UI page and hit `try it out` and select a preconfigured payload from a list, than go into dev tools in kibana and write out a payload.

- It allows you to build automated tests again the openapi specification using tools like [schemathesis](https://schemathesis.readthedocs.io/en/stable/). So when you want to upgrade elasticsearch you can test the APIs and your configuration are performing the way you expect. The openapi specification can be used to drive your tests by having endpoints that create indexes with data and then query that data.

- It allows you to create mock elasticsearch enpoints for frontend development with tools such as [postman.co](https://postman.co) or [openapi-mock](https://github.com/muonsoft/openapi-mock). 

</details>

### Screenshot

[![Swagger UI Screenshot](./docs/Swagger-UI-Screenshot.png)](./docs/Swagger-UI-Screenshot.png)
