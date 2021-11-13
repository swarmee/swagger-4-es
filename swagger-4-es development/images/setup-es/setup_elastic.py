import requests
from sample_data import *
import time

print('Start Checking to See if Elasticsearch Up')


def check_elastic():
    try:
        r = requests.get('http://opensearch:9200/_cluster/health')
        r = r.json()
        if r['status'] in ['green', 'yellow']:
            return True
    except:
        return False


while check_elastic() == False:
    print('Waiting For Elasticsearch to Come Up .....')
    time.sleep(10)

print('ElasticSearch Up Loading Data .....')

### Delete Existing Index
r = requests.delete('http://opensearch:9200/country', timeout=60)
print(r.text)

### Delete Existing Template
r = requests.delete('http://opensearch:9200/_index_template/country')
print(r.text)

### Load Mapping
r = requests.put('http://opensearch:9200/_index_template/country',
                 json=sample_mapping)
print(r.text)

### Load Sample Data 1
r = requests.post('http://opensearch:9200/country/_doc/1',
                  json=sample_data_1)
print(r.text)

### Load Sample Data 2
r = requests.post('http://opensearch:9200/country/_doc/2',
                  json=sample_data_2)
print(r.text)

### Load Sample Data 3
r = requests.post('http://opensearch:9200/country/_doc/3',
                  json=sample_data_3)
print(r.text)

### Load Sample Data 4
r = requests.post('http://opensearch:9200/country/_doc/4',
                  json=sample_data_4)
print(r.text)

### Load Sample Data 5
r = requests.post('http://opensearch:9200/country/_doc/5',
                  json=sample_data_5)
print(r.text)
### Load Sample Data 6
r = requests.post('http://opensearch:9200/country/_doc/6',
                  json=sample_data_6)
print(r.text)
### Load Sample Data 7
r = requests.post('http://opensearch:9200/country/_doc/7',
                  json=sample_data_7)
print(r.text)

print('Sample Data Loaded.')