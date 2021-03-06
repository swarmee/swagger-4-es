simple_single_country1 = {
    "name": "Afghanistan",
    "countryCode": "AF",
    "capital": "Kabul",
    "region": "Asia",
    "subregion": "Southern Asia",
    "area": 652230,
}

simple_single_country2 = {
    "name": "Commonwealth of the Bahamas",
    "countryCode": "BS",
    "capital": "Nassau",
    "area": 630,
    "region": "Americas"
}

simple_single_country3 = {
    "name": "Republic of Uganda",
    "countryCode": "UG",
    "capital": "Kampala",
    "region": "Africa"
}

simple_single_country4 = {
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

simple_single_country5 = {
    'name':
    'Angola',
    'countryCode':
    'AO',
    'capital':
    'Luanda',
    'region':
    'Africa',
    'subregion':
    'Middle Africa',
    'latlng': [-12.5, 18.5],
    'area':
    1246000,
    "gdp": [{
        "year": 2020,
        "amount": 62000000000
    }, {
        "year": 2010,
        "amount": 83000000000
    }]
}

create_index_examples = {
    "simple_index_creation": {
        "summary": "A simple index configuration",
        "description":
        "A **simple** index configuration. In this example we are just setting the number of shards and replicas",
        "value": {
            "settings": {
                "index": {
                    "number_of_replicas": 0
                }
            }
        }
    },
    "complex_index_country": {
        "summary": "A more complex index configuration",
        "description":
        "A more `complex` document with many fields of different types",
        "value": {
            "settings": {
                "index": {
                    "codec": "best_compression",
                    "number_of_replicas": 0,
                    "number_of_shards": 1,
                    "refresh_interval": "30s"
                }
            }
        }
    }
}

create_examples = {
    "simple_single_country1": {
        "summary": "A simple country document (1)",
        "description":
        "A **simple** Afghanistan document with only a few fields",
        "value": simple_single_country1
    },
    "simple_single_country2": {
        "summary": "A simple country document (2)",
        "description": "A **simple** Bahamas document with only a few fields",
        "value": simple_single_country2
    },
    "simple_single_country3": {
        "summary": "A simple country document (3)",
        "description": "A **simple** Uganda document with only a few fields",
        "value": simple_single_country3
    },
    "simple_single_country4": {
        "summary": "A simple country document (4)",
        "description": "A **simple** Bermuda document with only a few fields",
        "value": simple_single_country4
    },
    "simple_single_country5": {
        "summary": "A simple country document (5)",
        "description":
        "A **simple** Angola document with many fields of different types",
        "value": simple_single_country5 
    }
}

simple_countries_sample = {"index": {"_index": "country", "_id": 0}}

complex_countries_sample = """{ "index" : { "_index" : "country" } }
{'name': 'Afghanistan', 'topLevelDomain': ['.af'], 'alpha2Code': 'AF', 'alpha3Code': 'AFG', 'callingCodes': ['93'], 'capital': 'Kabul', 'altSpellings': ['AF', 'Af????nist??n'], 'region': 'Asia', 'subregion': 'Southern Asia', 'population': 27657145, 'latlng': [33, 65], 'demonym': 'Afghan', 'area': 652230, 'gini': 27.8, 'timezones': ['UTC+04:30'], 'borders': ['IRN', 'PAK', 'TKM', 'UZB', 'TJK', 'CHN'], 'nativeName': '??????????????????', 'numericCode': '004', 'currencies': [{'code': 'AFN', 'name': 'Afghan afghani', 'symbol': '??'}], 'languages': [{'iso639_1': 'ps', 'iso639_2': 'pus', 'name': 'Pashto', 'nativeName': '????????'}, {'iso639_1': 'uz', 'iso639_2': 'uzb', 'name': 'Uzbek', 'nativeName': 'O??zbek'}, {'iso639_1': 'tk', 'iso639_2': 'tuk', 'name': 'Turkmen', 'nativeName': 'T??rkmen'}], 'translations': {'de': 'Afghanistan', 'es': 'Afganist??n', 'fr': 'Afghanistan', 'ja': '?????????????????????', 'it': 'Afghanistan', 'br': 'Afeganist??o', 'pt': 'Afeganist??o', 'nl': 'Afghanistan', 'hr': 'Afganistan', 'fa': '??????????????????'}, 'flag': 'https://restcountries.eu/data/afg.svg', 'regionalBlocs': [{'acronym': 'SAARC', 'name': 'South Asian Association for Regional Cooperation', 'otherAcronyms': [], 'otherNames': []}], 'cioc': 'AFG'}
{ "index" : { "_index" : "country" } }
{'name': '??land Islands', 'topLevelDomain': ['.ax'], 'alpha2Code': 'AX', 'alpha3Code': 'ALA', 'callingCodes': ['358'], 'capital': 'Mariehamn', 'altSpellings': ['AX', 'Aaland', 'Aland', 'Ahvenanmaa'], 'region': 'Europe', 'subregion': 'Northern Europe', 'population': 28875, 'latlng': [60.116667, 19.9], 'demonym': '??landish', 'area': 1580, 'gini': None, 'timezones': ['UTC+02:00'], 'borders': [], 'nativeName': '??land', 'numericCode': '248', 'currencies': [{'code': 'EUR', 'name': 'Euro', 'symbol': '???'}], 'languages': [{'iso639_1': 'sv', 'iso639_2': 'swe', 'name': 'Swedish', 'nativeName': 'svenska'}], 'translations': {'de': '??land', 'es': 'Alandia', 'fr': '??land', 'ja': '?????????????????????', 'it': 'Isole Aland', 'br': 'Ilhas de Aland', 'pt': 'Ilhas de Aland', 'nl': '??landeilanden', 'hr': '??landski otoci', 'fa': '?????????? ????????'}, 'flag': 'https://restcountries.eu/data/ala.svg', 'regionalBlocs': [{'acronym': 'EU', 'name': 'European Union', 'otherAcronyms': [], 'otherNames': []}], 'cioc': ''}
{ "index" : { "_index" : "country" } }
{'name': 'Albania', 'topLevelDomain': ['.al'], 'alpha2Code': 'AL', 'alpha3Code': 'ALB', 'callingCodes': ['355'], 'capital': 'Tirana', 'altSpellings': ['AL', 'Shqip??ri', 'Shqip??ria', 'Shqipnia'], 'region': 'Europe', 'subregion': 'Southern Europe', 'population': 2886026, 'latlng': [41, 20], 'demonym': 'Albanian', 'area': 28748, 'gini': 34.5, 'timezones': ['UTC+01:00'], 'borders': ['MNE', 'GRC', 'MKD', 'KOS'], 'nativeName': 'Shqip??ria', 'numericCode': '008', 'currencies': [{'code': 'ALL', 'name': 'Albanian lek', 'symbol': 'L'}], 'languages': [{'iso639_1': 'sq', 'iso639_2': 'sqi', 'name': 'Albanian', 'nativeName': 'Shqip'}], 'translations': {'de': 'Albanien', 'es': 'Albania', 'fr': 'Albanie', 'ja': '???????????????', 'it': 'Albania', 'br': 'Alb??nia', 'pt': 'Alb??nia', 'nl': 'Albani??', 'hr': 'Albanija', 'fa': '????????????'}, 'flag': 'https://restcountries.eu/data/alb.svg', 'regionalBlocs': [{'acronym': 'CEFTA', 'name': 'Central European Free Trade Agreement', 'otherAcronyms': [], 'otherNames': []}], 'cioc': 'ALB'}
{ "index" : { "_index" : "country" } }
{'name': 'Algeria', 'topLevelDomain': ['.dz'], 'alpha2Code': 'DZ', 'alpha3Code': 'DZA', 'callingCodes': ['213'], 'capital': 'Algiers', 'altSpellings': ['DZ', 'Dzayer', 'Alg??rie'], 'region': 'Africa', 'subregion': 'Northern Africa', 'population': 40400000, 'latlng': [28, 3], 'demonym': 'Algerian', 'area': 2381741, 'gini': 35.3, 'timezones': ['UTC+01:00'], 'borders': ['TUN', 'LBY', 'NER', 'ESH', 'MRT', 'MLI', 'MAR'], 'nativeName': '??????????????', 'numericCode': '012', 'currencies': [{'code': 'DZD', 'name': 'Algerian dinar', 'symbol': '??.??'}], 'languages': [{'iso639_1': 'ar', 'iso639_2': 'ara', 'name': 'Arabic', 'nativeName': '??????????????'}], 'translations': {'de': 'Algerien', 'es': 'Argelia', 'fr': 'Alg??rie', 'ja': '??????????????????', 'it': 'Algeria', 'br': 'Arg??lia', 'pt': 'Arg??lia', 'nl': 'Algerije', 'hr': 'Al??ir', 'fa': '??????????????'}, 'flag': 'https://restcountries.eu/data/dza.svg', 'regionalBlocs': [{'acronym': 'AU', 'name': 'African Union', 'otherAcronyms': [], 'otherNames': ['?????????????? ????????????????', 'Union africaine', 'Uni??o Africana', 'Uni??n Africana', 'Umoja wa Afrika']}, {'acronym': 'AL', 'name': 'Arab League', 'otherAcronyms': [], 'otherNames': ['?????????? ?????????? ??????????????', 'J??mi??at ad-Duwal al-??Arab??yah', 'League of Arab States']}], 'cioc': 'ALG'}
{ "index" : { "_index" : "country" } }
{'name': 'American Samoa', 'topLevelDomain': ['.as'], 'alpha2Code': 'AS', 'alpha3Code': 'ASM', 'callingCodes': ['1684'], 'capital': 'Pago Pago', 'altSpellings': ['AS', 'Amerika S??moa', 'Amelika S??moa', 'S??moa Amelika'], 'region': 'Oceania', 'subregion': 'Polynesia', 'population': 57100, 'latlng': [-14.33333333, -170], 'demonym': 'American Samoan', 'area': 199, 'gini': None, 'timezones': ['UTC-11:00'], 'borders': [], 'nativeName': 'American Samoa', 'numericCode': '016', 'currencies': [{'code': 'USD', 'name': 'United State Dollar', 'symbol': '$'}], 'languages': [{'iso639_1': 'en', 'iso639_2': 'eng', 'name': 'English', 'nativeName': 'English'}, {'iso639_1': 'sm', 'iso639_2': 'smo', 'name': 'Samoan', 'nativeName': "gagana fa'a Samoa"}], 'translations': {'de': 'Amerikanisch-Samoa', 'es': 'Samoa Americana', 'fr': 'Samoa am??ricaines', 'ja': '????????????????????????', 'it': 'Samoa Americane', 'br': 'Samoa Americana', 'pt': 'Samoa Americana', 'nl': 'Amerikaans Samoa', 'hr': 'Ameri??ka Samoa', 'fa': '???????????? ????????????'}, 'flag': 'https://restcountries.eu/data/asm.svg', 'regionalBlocs': [], 'cioc': 'ASA'}
{ "index" : { "_index" : "country" } }
{'name': 'Andorra', 'topLevelDomain': ['.ad'], 'alpha2Code': 'AD', 'alpha3Code': 'AND', 'callingCodes': ['376'], 'capital': 'Andorra la Vella', 'altSpellings': ['AD', 'Principality of Andorra', "Principat d'Andorra"], 'region': 'Europe', 'subregion': 'Southern Europe', 'population': 78014, 'latlng': [42.5, 1.5], 'demonym': 'Andorran', 'area': 468, 'gini': None, 'timezones': ['UTC+01:00'], 'borders': ['FRA', 'ESP'], 'nativeName': 'Andorra', 'numericCode': '020', 'currencies': [{'code': 'EUR', 'name': 'Euro', 'symbol': '???'}], 'languages': [{'iso639_1': 'ca', 'iso639_2': 'cat', 'name': 'Catalan', 'nativeName': 'catal??'}], 'translations': {'de': 'Andorra', 'es': 'Andorra', 'fr': 'Andorre', 'ja': '????????????', 'it': 'Andorra', 'br': 'Andorra', 'pt': 'Andorra', 'nl': 'Andorra', 'hr': 'Andora', 'fa': '????????????'}, 'flag': 'https://restcountries.eu/data/and.svg', 'regionalBlocs': [], 'cioc': 'AND'}
{ "index" : { "_index" : "country" } }
{'name': 'Angola', 'topLevelDomain': ['.ao'], 'alpha2Code': 'AO', 'alpha3Code': 'AGO', 'callingCodes': ['244'], 'capital': 'Luanda', 'altSpellings': ['AO', 'Rep??blica de Angola', "????publika de an'????la"], 'region': 'Africa', 'subregion': 'Middle Africa', 'population': 25868000, 'latlng': [-12.5, 18.5], 'demonym': 'Angolan', 'area': 1246700, 'gini': 58.6, 'timezones': ['UTC+01:00'], 'borders': ['COG', 'COD', 'ZMB', 'NAM'], 'nativeName': 'Angola', 'numericCode': '024', 'currencies': [{'code': 'AOA', 'name': 'Angolan kwanza', 'symbol': 'Kz'}], 'languages': [{'iso639_1': 'pt', 'iso639_2': 'por', 'name': 'Portuguese', 'nativeName': 'Portugu??s'}], 'translations': {'de': 'Angola', 'es': 'Angola', 'fr': 'Angola', 'ja': '????????????', 'it': 'Angola', 'br': 'Angola', 'pt': 'Angola', 'nl': 'Angola', 'hr': 'Angola', 'fa': '????????????'}, 'flag': 'https://restcountries.eu/data/ago.svg', 'regionalBlocs': [{'acronym': 'AU', 'name': 'African Union', 'otherAcronyms': [], 'otherNames': ['?????????????? ????????????????', 'Union africaine', 'Uni??o Africana', 'Uni??n Africana', 'Umoja wa Afrika']}], 'cioc': 'ANG'}
{ "index" : { "_index" : "country" } }
{'name': 'Anguilla', 'topLevelDomain': ['.ai'], 'alpha2Code': 'AI', 'alpha3Code': 'AIA', 'callingCodes': ['1264'], 'capital': 'The Valley', 'altSpellings': ['AI'], 'region': 'Americas', 'subregion': 'Caribbean', 'population': 13452, 'latlng': [18.25, -63.16666666], 'demonym': 'Anguillian', 'area': 91, 'gini': None, 'timezones': ['UTC-04:00'], 'borders': [], 'nativeName': 'Anguilla', 'numericCode': '660', 'currencies': [{'code': 'XCD', 'name': 'East Caribbean dollar', 'symbol': '$'}], 'languages': [{'iso639_1': 'en', 'iso639_2': 'eng', 'name': 'English', 'nativeName': 'English'}], 'translations': {'de': 'Anguilla', 'es': 'Anguilla', 'fr': 'Anguilla', 'ja': '????????????', 'it': 'Anguilla', 'br': 'Anguila', 'pt': 'Anguila', 'nl': 'Anguilla', 'hr': 'Angvila', 'fa': '??????????????'}, 'flag': 'https://restcountries.eu/data/aia.svg', 'regionalBlocs': [], 'cioc': ''}
{ "index" : { "_index" : "country" } }
{'name': 'Antarctica', 'topLevelDomain': ['.aq'], 'alpha2Code': 'AQ', 'alpha3Code': 'ATA', 'callingCodes': ['672'], 'capital': '', 'altSpellings': [], 'region': 'Polar', 'subregion': '', 'population': 1000, 'latlng': [-74.65, 4.48], 'demonym': '', 'area': 14000000, 'gini': None, 'timezones': ['UTC-03:00', 'UTC+03:00', 'UTC+05:00', 'UTC+06:00', 'UTC+07:00', 'UTC+08:00', 'UTC+10:00', 'UTC+12:00'], 'borders': [], 'nativeName': 'Antarctica', 'numericCode': '010', 'currencies': [{'code': 'AUD', 'name': 'Australian dollar', 'symbol': '$'}, {'code': 'GBP', 'name': 'British pound', 'symbol': '??'}], 'languages': [{'iso639_1': 'en', 'iso639_2': 'eng', 'name': 'English', 'nativeName': 'English'}, {'iso639_1': 'ru', 'iso639_2': 'rus', 'name': 'Russian', 'nativeName': '??????????????'}], 'translations': {'de': 'Antarktika', 'es': 'Ant??rtida', 'fr': 'Antarctique', 'ja': '????????????', 'it': 'Antartide', 'br': 'Ant??rtida', 'pt': 'Ant??rctida', 'nl': 'Antarctica', 'hr': 'Antarktika', 'fa': '??????????????'}, 'flag': 'https://restcountries.eu/data/ata.svg', 'regionalBlocs': [], 'cioc': ''}
{ "index" : { "_index" : "country" } }
{'name': 'Antigua and Barbuda', 'topLevelDomain': ['.ag'], 'alpha2Code': 'AG', 'alpha3Code': 'ATG', 'callingCodes': ['1268'], 'capital': "Saint John's", 'altSpellings': ['AG'], 'region': 'Americas', 'subregion': 'Caribbean', 'population': 86295, 'latlng': [17.05, -61.8], 'demonym': 'Antiguan, Barbudan', 'area': 442, 'gini': None, 'timezones': ['UTC-04:00'], 'borders': [], 'nativeName': 'Antigua and Barbuda', 'numericCode': '028', 'currencies': [{'code': 'XCD', 'name': 'East Caribbean dollar', 'symbol': '$'}], 'languages': [{'iso639_1': 'en', 'iso639_2': 'eng', 'name': 'English', 'nativeName': 'English'}], 'translations': {'de': 'Antigua und Barbuda', 'es': 'Antigua y Barbuda', 'fr': 'Antigua-et-Barbuda', 'ja': '????????????????????????????????????', 'it': 'Antigua e Barbuda', 'br': 'Ant??gua e Barbuda', 'pt': 'Ant??gua e Barbuda', 'nl': 'Antigua en Barbuda', 'hr': 'Antigva i Barbuda', 'fa': '?????????????? ?? ??????????????'}, 'flag': 'https://restcountries.eu/data/atg.svg', 'regionalBlocs': [{'acronym': 'CARICOM', 'name': 'Caribbean Community', 'otherAcronyms': [], 'otherNames': ['Comunidad del Caribe', 'Communaut?? Carib??enne', 'Caribische Gemeenschap']}], 'cioc': 'ANT'}
{ "index" : { "_index" : "country" } }
{'name': 'Argentina', 'topLevelDomain': ['.ar'], 'alpha2Code': 'AR', 'alpha3Code': 'ARG', 'callingCodes': ['54'], 'capital': 'Buenos Aires', 'altSpellings': ['AR', 'Argentine Republic', 'Rep??blica Argentina'], 'region': 'Americas', 'subregion': 'South America', 'population': 43590400, 'latlng': [-34, -64], 'demonym': 'Argentinean', 'area': 2780400, 'gini': 44.5, 'timezones': ['UTC-03:00'], 'borders': ['BOL', 'BRA', 'CHL', 'PRY', 'URY'], 'nativeName': 'Argentina', 'numericCode': '032', 'currencies': [{'code': 'ARS', 'name': 'Argentine peso', 'symbol': '$'}], 'languages': [{'iso639_1': 'es', 'iso639_2': 'spa', 'name': 'Spanish', 'nativeName': 'Espa??ol'}, {'iso639_1': 'gn', 'iso639_2': 'grn', 'name': 'Guaran??', 'nativeName': "Ava??e'???"}], 'translations': {'de': 'Argentinien', 'es': 'Argentina', 'fr': 'Argentine', 'ja': '??????????????????', 'it': 'Argentina', 'br': 'Argentina', 'pt': 'Argentina', 'nl': 'Argentini??', 'hr': 'Argentina', 'fa': '????????????????'}, 'flag': 'https://restcountries.eu/data/arg.svg', 'regionalBlocs': [{'acronym': 'USAN', 'name': 'Union of South American Nations', 'otherAcronyms': ['UNASUR', 'UNASUL', 'UZAN'], 'otherNames': ['Uni??n de Naciones Suramericanas', 'Uni??o de Na????es Sul-Americanas', 'Unie van Zuid-Amerikaanse Naties', 'South American Union']}], 'cioc': 'ARG'}
{ "index" : { "_index" : "country" } }
{'name': 'Armenia', 'topLevelDomain': ['.am'], 'alpha2Code': 'AM', 'alpha3Code': 'ARM', 'callingCodes': ['374'], 'capital': 'Yerevan', 'altSpellings': ['AM', 'Hayastan', 'Republic of Armenia', '?????????????????? ??????????????????????????????'], 'region': 'Asia', 'subregion': 'Western Asia', 'population': 2994400, 'latlng': [40, 45], 'demonym': 'Armenian', 'area': 29743, 'gini': 30.9, 'timezones': ['UTC+04:00'], 'borders': ['AZE', 'GEO', 'IRN', 'TUR'], 'nativeName': '????????????????', 'numericCode': '051', 'currencies': [{'code': 'AMD', 'name': 'Armenian dram', 'symbol': None}], 'languages': [{'iso639_1': 'hy', 'iso639_2': 'hye', 'name': 'Armenian', 'nativeName': '??????????????'}, {'iso639_1': 'ru', 'iso639_2': 'rus', 'name': 'Russian', 'nativeName': '??????????????'}], 'translations': {'de': 'Armenien', 'es': 'Armenia', 'fr': 'Arm??nie', 'ja': '???????????????', 'it': 'Armenia', 'br': 'Arm??nia', 'pt': 'Arm??nia', 'nl': 'Armeni??', 'hr': 'Armenija', 'fa': '????????????????'}, 'flag': 'https://restcountries.eu/data/arm.svg', 'regionalBlocs': [{'acronym': 'EEU', 'name': 'Eurasian Economic Union', 'otherAcronyms': ['EAEU'], 'otherNames': []}], 'cioc': 'ARM'}
{ "index" : { "_index" : "country" } }
{'name': 'Aruba', 'topLevelDomain': ['.aw'], 'alpha2Code': 'AW', 'alpha3Code': 'ABW', 'callingCodes': ['297'], 'capital': 'Oranjestad', 'altSpellings': ['AW'], 'region': 'Americas', 'subregion': 'Caribbean', 'population': 107394, 'latlng': [12.5, -69.96666666], 'demonym': 'Aruban', 'area': 180, 'gini': None, 'timezones': ['UTC-04:00'], 'borders': [], 'nativeName': 'Aruba', 'numericCode': '533', 'currencies': [{'code': 'AWG', 'name': 'Aruban florin', 'symbol': '??'}], 'languages': [{'iso639_1': 'nl', 'iso639_2': 'nld', 'name': 'Dutch', 'nativeName': 'Nederlands'}, {'iso639_1': 'pa', 'iso639_2': 'pan', 'name': '(Eastern) Punjabi', 'nativeName': '??????????????????'}], 'translations': {'de': 'Aruba', 'es': 'Aruba', 'fr': 'Aruba', 'ja': '?????????', 'it': 'Aruba', 'br': 'Aruba', 'pt': 'Aruba', 'nl': 'Aruba', 'hr': 'Aruba', 'fa': '??????????'}, 'flag': 'https://restcountries.eu/data/abw.svg', 'regionalBlocs': [], 'cioc': 'ARU'}
{ "index" : { "_index" : "country" } }
{'name': 'Australia', 'topLevelDomain': ['.au'], 'alpha2Code': 'AU', 'alpha3Code': 'AUS', 'callingCodes': ['61'], 'capital': 'Canberra', 'altSpellings': ['AU'], 'region': 'Oceania', 'subregion': 'Australia and New Zealand', 'population': 24117360, 'latlng': [-27, 133], 'demonym': 'Australian', 'area': 7692024, 'gini': 30.5, 'timezones': ['UTC+05:00', 'UTC+06:30', 'UTC+07:00', 'UTC+08:00', 'UTC+09:30', 'UTC+10:00', 'UTC+10:30', 'UTC+11:30'], 'borders': [], 'nativeName': 'Australia', 'numericCode': '036', 'currencies': [{'code': 'AUD', 'name': 'Australian dollar', 'symbol': '$'}], 'languages': [{'iso639_1': 'en', 'iso639_2': 'eng', 'name': 'English', 'nativeName': 'English'}], 'translations': {'de': 'Australien', 'es': 'Australia', 'fr': 'Australie', 'ja': '?????????????????????', 'it': 'Australia', 'br': 'Austr??lia', 'pt': 'Austr??lia', 'nl': 'Australi??', 'hr': 'Australija', 'fa': '????????????????'}, 'flag': 'https://restcountries.eu/data/aus.svg', 'regionalBlocs': [], 'cioc': 'AUS'}
{ "index" : { "_index" : "country" } }
{'name': 'Austria', 'topLevelDomain': ['.at'], 'alpha2Code': 'AT', 'alpha3Code': 'AUT', 'callingCodes': ['43'], 'capital': 'Vienna', 'altSpellings': ['AT', '??sterreich', 'Osterreich', 'Oesterreich'], 'region': 'Europe', 'subregion': 'Western Europe', 'population': 8725931, 'latlng': [47.33333333, 13.33333333], 'demonym': 'Austrian', 'area': 83871, 'gini': 26, 'timezones': ['UTC+01:00'], 'borders': ['CZE', 'DEU', 'HUN', 'ITA', 'LIE', 'SVK', 'SVN', 'CHE'], 'nativeName': '??sterreich', 'numericCode': '040', 'currencies': [{'code': 'EUR', 'name': 'Euro', 'symbol': '???'}], 'languages': [{'iso639_1': 'de', 'iso639_2': 'deu', 'name': 'German', 'nativeName': 'Deutsch'}], 'translations': {'de': '??sterreich', 'es': 'Austria', 'fr': 'Autriche', 'ja': '??????????????????', 'it': 'Austria', 'br': '??ustria', 'pt': '??ustria', 'nl': 'Oostenrijk', 'hr': 'Austrija', 'fa': '??????????'}, 'flag': 'https://restcountries.eu/data/aut.svg', 'regionalBlocs': [{'acronym': 'EU', 'name': 'European Union', 'otherAcronyms': [], 'otherNames': []}], 'cioc': 'AUT'}
{ "index" : { "_index" : "country" } }
{'name': 'Azerbaijan', 'topLevelDomain': ['.az'], 'alpha2Code': 'AZ', 'alpha3Code': 'AZE', 'callingCodes': ['994'], 'capital': 'Baku', 'altSpellings': ['AZ', 'Republic of Azerbaijan', 'Az??rbaycan Respublikas??'], 'region': 'Asia', 'subregion': 'Western Asia', 'population': 9730500, 'latlng': [40.5, 47.5], 'demonym': 'Azerbaijani', 'area': 86600, 'gini': 33.7, 'timezones': ['UTC+04:00'], 'borders': ['ARM', 'GEO', 'IRN', 'RUS', 'TUR'], 'nativeName': 'Az??rbaycan', 'numericCode': '031', 'currencies': [{'code': 'AZN', 'name': 'Azerbaijani manat', 'symbol': None}], 'languages': [{'iso639_1': 'az', 'iso639_2': 'aze', 'name': 'Azerbaijani', 'nativeName': 'az??rbaycan dili'}], 'translations': {'de': 'Aserbaidschan', 'es': 'Azerbaiy??n', 'fr': 'Azerba??djan', 'ja': '????????????????????????', 'it': 'Azerbaijan', 'br': 'Azerbaij??o', 'pt': 'Azerbaij??o', 'nl': 'Azerbeidzjan', 'hr': 'Azerbajd??an', 'fa': '??????????????????'}, 'flag': 'https://restcountries.eu/data/aze.svg', 'regionalBlocs': [], 'cioc': 'AZE'}
{ "index" : { "_index" : "country" } }
{'name': 'Bahamas', 'topLevelDomain': ['.bs'], 'alpha2Code': 'BS', 'alpha3Code': 'BHS', 'callingCodes': ['1242'], 'capital': 'Nassau', 'altSpellings': ['BS', 'Commonwealth of the Bahamas'], 'region': 'Americas', 'subregion': 'Caribbean', 'population': 378040, 'latlng': [24.25, -76], 'demonym': 'Bahamian', 'area': 13943, 'gini': None, 'timezones': ['UTC-05:00'], 'borders': [], 'nativeName': 'Bahamas', 'numericCode': '044', 'currencies': [{'code': 'BSD', 'name': 'Bahamian dollar', 'symbol': '$'}], 'languages': [{'iso639_1': 'en', 'iso639_2': 'eng', 'name': 'English', 'nativeName': 'English'}], 'translations': {'de': 'Bahamas', 'es': 'Bahamas', 'fr': 'Bahamas', 'ja': '?????????', 'it': 'Bahamas', 'br': 'Bahamas', 'pt': 'Baamas', 'nl': 'Bahama???s', 'hr': 'Bahami', 'fa': '????????????'}, 'flag': 'https://restcountries.eu/data/bhs.svg', 'regionalBlocs': [{'acronym': 'CARICOM', 'name': 'Caribbean Community', 'otherAcronyms': [], 'otherNames': ['Comunidad del Caribe', 'Communaut?? Carib??enne', 'Caribische Gemeenschap']}], 'cioc': 'BAH'}
{ "index" : { "_index" : "country" } }
{'name': 'Bahrain', 'topLevelDomain': ['.bh'], 'alpha2Code': 'BH', 'alpha3Code': 'BHR', 'callingCodes': ['973'], 'capital': 'Manama', 'altSpellings': ['BH', 'Kingdom of Bahrain', 'Mamlakat al-Ba???rayn'], 'region': 'Asia', 'subregion': 'Western Asia', 'population': 1404900, 'latlng': [26, 50.55], 'demonym': 'Bahraini', 'area': 765, 'gini': None, 'timezones': ['UTC+03:00'], 'borders': [], 'nativeName': '\u200f??????????????', 'numericCode': '048', 'currencies': [{'code': 'BHD', 'name': 'Bahraini dinar', 'symbol': '.??.??'}], 'languages': [{'iso639_1': 'ar', 'iso639_2': 'ara', 'name': 'Arabic', 'nativeName': '??????????????'}], 'translations': {'de': 'Bahrain', 'es': 'Bahrein', 'fr': 'Bahre??n', 'ja': '???????????????', 'it': 'Bahrein', 'br': 'Bahrein', 'pt': 'Bar??m', 'nl': 'Bahrein', 'hr': 'Bahrein', 'fa': '??????????'}, 'flag': 'https://restcountries.eu/data/bhr.svg', 'regionalBlocs': [{'acronym': 'AL', 'name': 'Arab League', 'otherAcronyms': [], 'otherNames': ['?????????? ?????????? ??????????????', 'J??mi??at ad-Duwal al-??Arab??yah', 'League of Arab States']}], 'cioc': 'BRN'}
{ "index" : { "_index" : "country" } }
{'name': 'Bangladesh', 'topLevelDomain': ['.bd'], 'alpha2Code': 'BD', 'alpha3Code': 'BGD', 'callingCodes': ['880'], 'capital': 'Dhaka', 'altSpellings': ['BD', "People's Republic of Bangladesh", 'G??n??pr??jat??ntri Bangladesh'], 'region': 'Asia', 'subregion': 'Southern Asia', 'population': 161006790, 'latlng': [24, 90], 'demonym': 'Bangladeshi', 'area': 147570, 'gini': 32.1, 'timezones': ['UTC+06:00'], 'borders': ['MMR', 'IND'], 'nativeName': 'Bangladesh', 'numericCode': '050', 'currencies': [{'code': 'BDT', 'name': 'Bangladeshi taka', 'symbol': '???'}], 'languages': [{'iso639_1': 'bn', 'iso639_2': 'ben', 'name': 'Bengali', 'nativeName': '???????????????'}], 'translations': {'de': 'Bangladesch', 'es': 'Bangladesh', 'fr': 'Bangladesh', 'ja': '?????????????????????', 'it': 'Bangladesh', 'br': 'Bangladesh', 'pt': 'Bangladeche', 'nl': 'Bangladesh', 'hr': 'Banglade??', 'fa': '??????????????'}, 'flag': 'https://restcountries.eu/data/bgd.svg', 'regionalBlocs': [{'acronym': 'SAARC', 'name': 'South Asian Association for Regional Cooperation', 'otherAcronyms': [], 'otherNames': []}], 'cioc': 'BAN'}
{ "index" : { "_index" : "country" } }
{'name': 'Barbados', 'topLevelDomain': ['.bb'], 'alpha2Code': 'BB', 'alpha3Code': 'BRB', 'callingCodes': ['1246'], 'capital': 'Bridgetown', 'altSpellings': ['BB'], 'region': 'Americas', 'subregion': 'Caribbean', 'population': 285000, 'latlng': [13.16666666, -59.53333333], 'demonym': 'Barbadian', 'area': 430, 'gini': None, 'timezones': ['UTC-04:00'], 'borders': [], 'nativeName': 'Barbados', 'numericCode': '052', 'currencies': [{'code': 'BBD', 'name': 'Barbadian dollar', 'symbol': '$'}], 'languages': [{'iso639_1': 'en', 'iso639_2': 'eng', 'name': 'English', 'nativeName': 'English'}], 'translations': {'de': 'Barbados', 'es': 'Barbados', 'fr': 'Barbade', 'ja': '???????????????', 'it': 'Barbados', 'br': 'Barbados', 'pt': 'Barbados', 'nl': 'Barbados', 'hr': 'Barbados', 'fa': '????????????????'}, 'flag': 'https://restcountries.eu/data/brb.svg', 'regionalBlocs': [{'acronym': 'CARICOM', 'name': 'Caribbean Community', 'otherAcronyms': [], 'otherNames': ['Comunidad del Caribe', 'Communaut?? Carib??enne', 'Caribische Gemeenschap']}], 'cioc': 'BAR'}
{ "index" : { "_index" : "country" } }
{'name': 'Belarus', 'topLevelDomain': ['.by'], 'alpha2Code': 'BY', 'alpha3Code': 'BLR', 'callingCodes': ['375'], 'capital': 'Minsk', 'altSpellings': ['BY', 'Bielaru??', 'Republic of Belarus', '????????????????????', '???????????????????? ????????????????', 'Belorussiya', 'Respublika Belarus???'], 'region': 'Europe', 'subregion': 'Eastern Europe', 'population': 9498700, 'latlng': [53, 28], 'demonym': 'Belarusian', 'area': 207600, 'gini': 26.5, 'timezones': ['UTC+03:00'], 'borders': ['LVA', 'LTU', 'POL', 'RUS', 'UKR'], 'nativeName': '??????????????????', 'numericCode': '112', 'currencies': [{'code': 'BYN', 'name': 'New Belarusian ruble', 'symbol': 'Br'}, {'code': 'BYR', 'name': 'Old Belarusian ruble', 'symbol': 'Br'}], 'languages': [{'iso639_1': 'be', 'iso639_2': 'bel', 'name': 'Belarusian', 'nativeName': '???????????????????? ????????'}, {'iso639_1': 'ru', 'iso639_2': 'rus', 'name': 'Russian', 'nativeName': '??????????????'}], 'translations': {'de': 'Wei??russland', 'es': 'Bielorrusia', 'fr': 'Bi??lorussie', 'ja': '???????????????', 'it': 'Bielorussia', 'br': 'Bielorr??ssia', 'pt': 'Bielorr??ssia', 'nl': 'Wit-Rusland', 'hr': 'Bjelorusija', 'fa': '????????????'}, 'flag': 'https://restcountries.eu/data/blr.svg', 'regionalBlocs': [{'acronym': 'EEU', 'name': 'Eurasian Economic Union', 'otherAcronyms': ['EAEU'], 'otherNames': []}], 'cioc': 'BLR'}
{ "index" : { "_index" : "country" } }
{'name': 'Belgium', 'topLevelDomain': ['.be'], 'alpha2Code': 'BE', 'alpha3Code': 'BEL', 'callingCodes': ['32'], 'capital': 'Brussels', 'altSpellings': ['BE', 'Belgi??', 'Belgie', 'Belgien', 'Belgique', 'Kingdom of Belgium', 'Koninkrijk Belgi??', 'Royaume de Belgique', 'K??nigreich Belgien'], 'region': 'Europe', 'subregion': 'Western Europe', 'population': 11319511, 'latlng': [50.83333333, 4], 'demonym': 'Belgian', 'area': 30528, 'gini': 33, 'timezones': ['UTC+01:00'], 'borders': ['FRA', 'DEU', 'LUX', 'NLD'], 'nativeName': 'Belgi??', 'numericCode': '056', 'currencies': [{'code': 'EUR', 'name': 'Euro', 'symbol': '???'}], 'languages': [{'iso639_1': 'nl', 'iso639_2': 'nld', 'name': 'Dutch', 'nativeName': 'Nederlands'}, {'iso639_1': 'fr', 'iso639_2': 'fra', 'name': 'French', 'nativeName': 'fran??ais'}, {'iso639_1': 'de', 'iso639_2': 'deu', 'name': 'German', 'nativeName': 'Deutsch'}], 'translations': {'de': 'Belgien', 'es': 'B??lgica', 'fr': 'Belgique', 'ja': '????????????', 'it': 'Belgio', 'br': 'B??lgica', 'pt': 'B??lgica', 'nl': 'Belgi??', 'hr': 'Belgija', 'fa': '??????????'}, 'flag': 'https://restcountries.eu/data/bel.svg', 'regionalBlocs': [{'acronym': 'EU', 'name': 'European Union', 'otherAcronyms': [], 'otherNames': []}], 'cioc': 'BEL'}
{ "index" : { "_index" : "country" } }
{'name': 'Belize', 'topLevelDomain': ['.bz'], 'alpha2Code': 'BZ', 'alpha3Code': 'BLZ', 'callingCodes': ['501'], 'capital': 'Belmopan', 'altSpellings': ['BZ'], 'region': 'Americas', 'subregion': 'Central America', 'population': 370300, 'latlng': [17.25, -88.75], 'demonym': 'Belizean', 'area': 22966, 'gini': 53.1, 'timezones': ['UTC-06:00'], 'borders': ['GTM', 'MEX'], 'nativeName': 'Belize', 'numericCode': '084', 'currencies': [{'code': 'BZD', 'name': 'Belize dollar', 'symbol': '$'}], 'languages': [{'iso639_1': 'en', 'iso639_2': 'eng', 'name': 'English', 'nativeName': 'English'}, {'iso639_1': 'es', 'iso639_2': 'spa', 'name': 'Spanish', 'nativeName': 'Espa??ol'}], 'translations': {'de': 'Belize', 'es': 'Belice', 'fr': 'Belize', 'ja': '????????????', 'it': 'Belize', 'br': 'Belize', 'pt': 'Belize', 'nl': 'Belize', 'hr': 'Belize', 'fa': '????????'}, 'flag': 'https://restcountries.eu/data/blz.svg', 'regionalBlocs': [{'acronym': 'CARICOM', 'name': 'Caribbean Community', 'otherAcronyms': [], 'otherNames': ['Comunidad del Caribe', 'Communaut?? Carib??enne', 'Caribische Gemeenschap']}, {'acronym': 'CAIS', 'name': 'Central American Integration System', 'otherAcronyms': ['SICA'], 'otherNames': ['Sistema de la Integraci??n Centroamericana,']}], 'cioc': 'BIZ'}

"""

bulk_create_example = {
    "simple_countries": {
        "summary": "A List of Complex Countries",
        "description":
        "A `complex` document with many fields of different types",
        "value": simple_countries_sample
    },
    "complex_countries": {
        "summary": "A List of Complex Countries",
        "description":
        "A `complex` document with many fields of different types",
        "value": complex_countries_sample
    }
}
