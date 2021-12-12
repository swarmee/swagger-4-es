FROM opensearchproject/opensearch:latest

RUN /usr/share/opensearch/bin/opensearch-plugin remove opensearch-security
RUN /usr/share/opensearch/bin/opensearch-plugin remove opensearch-sql
RUN /usr/share/opensearch/bin/opensearch-plugin remove opensearch-knn
RUN /usr/share/opensearch/bin/opensearch-plugin remove opensearch-anomaly-detection
RUN /usr/share/opensearch/bin/opensearch-plugin remove opensearch-alerting
#RUN /usr/share/opensearch/bin/opensearch-plugin remove opensearch-dashboards
#RUN /usr/share/opensearch/bin/opensearch-plugin remove ingest-geoip
#RUN /usr/share/opensearch/bin/opensearch-plugin remove ingest-user-agent
#RUN /usr/share/opensearch/bin/opensearch-plugin remove percolator
#RUN /usr/share/opensearch/bin/opensearch-plugin remove opensearch-notebooks
RUN /usr/share/opensearch/bin/opensearch-plugin remove opensearch-asynchronous-search
RUN /usr/share/opensearch/bin/opensearch-plugin remove opensearch-reports-scheduler
RUN /usr/share/opensearch/bin/opensearch-plugin remove opensearch-cross-cluster-replication
#RUN /usr/share/opensearch/bin/opensearch-plugin remove opensearch-performance-analyzer
RUN /usr/share/opensearch/bin/opensearch-plugin remove opensearch-index-management

RUN /usr/share/opensearch/bin/opensearch-plugin list

# ##RUN /usr/share/opensearch/bin/opensearch-plugin install --batch <plugin-name-or-url>
COPY --chown=opensearch:opensearch ./opensearch.yml /usr/share/opensearch/config/
# COPY --chown=opensearch:opensearch ./root-ca.pem /usr/share/opensearch/config/root-ca.pem 
# COPY --chown=opensearch:opensearch ./admin-key.pem /usr/share/opensearch/config/admin-key.pem 
# COPY --chown=opensearch:opensearch ./admin.pem /usr/share/opensearch/config/admin.pem 
COPY --chown=opensearch:opensearch ./jvm.options /usr/share/opensearch/config/jvm.options

