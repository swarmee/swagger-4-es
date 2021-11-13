sample_data_1 = {
    "name": "Afghanistan",
    "countryCode": "AF",
    "capital": "Kabul",
    "region": "Asia",
    "subregion": "Southern Asia",
    "area": 652230
}

sample_data_2 = {
    "name": "Commonwealth of the Bahamas",
    "countryCode": "BS",
    "capital": "Nassau",
    "area": 630,
    "region": "Americas"
}

sample_data_3 = {
    "name": "Republic of Uganda",
    "countryCode": "UG",
    "capital": "Kampala",
    "region": "Africa"
}

sample_data_4 = {
    "name":
    "The Bermudas",
    "countryCode":
    "BM",
    "capital":
    "Hamilton",
    "region":
    "Americas",
    "gdp": [{
        "year": 2020,
        "amount": 8000000000
    }, {
        "year": 2010,
        "amount": 6000000000
    }]
}

sample_data_5 = {
    "name":
    "Angola",
    "countryCode":
    "AO",
    "capital":
    "Luanda",
    "region":
    "Africa",
    "subregion":
    "Middle Africa",
    "latlng": [-12.5, 18.5],
    "area":
    1246000,
    "gdp": [{
        "year": 2020,
        "amount": 62000000000
    }, {
        "year": 2010,
        "amount": 83000000000
    }]
}

sample_data_6 = {
    "name":
    "Zambia",
    "countryCode":
    "ZM",
    "capital":
    "Lusaka",
    "region":
    "Africa",
    "area":
    21111100,
    "gdp": [{
        "year": 2020,
        "amount": 5200000000
    }, {
        "year": 2010,
        "amount": 100000000
    }]
}

sample_data_7 = {
    "name":
    "Zimbabwe",
    "countryCode":
    "ZW",
    "capital":
    "Harare",
    "region":
    "Africa",
    "area":
    21111100,
    "gdp": [{
        "year": 2020,
        "amount": 520000000
    }, {
        "year": 2010,
        "amount": 10000000
    }]
}

sample_mapping = {
    "index_patterns": ["country"],
    "template": {
        "settings": {
            "number_of_shards": 1,
            "number_of_replicas": 0,
            "codec": "best_compression"
        },
        "mappings": {
            "properties": {
                "countryCode": {
                    "type": "keyword"
                }
            }
        }
    }
}