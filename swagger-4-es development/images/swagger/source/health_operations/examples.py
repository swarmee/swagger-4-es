simple_single_country = {
    "name": "Afghanistan",
    "alpha2Code": "AF",
    "capital": "Kabul",
    "region": "Asia",
    "subregion": "Southern Asia",
    "area": 652230
}

complex_single_country = {
    "name":
    "Afghanistan",
    "topLevelDomain": [".af"],
    "alpha2Code":
    "AF",
    "alpha3Code":
    "AFG",
    "callingCodes": ["93"],
    "capital":
    "Kabul",
    "altSpellings": ["AF", "Afġānistān"],
    "region":
    "Asia",
    "subregion":
    "Southern Asia",
    "population":
    27657145,
    "latlng": [33, 65],
    "demonym":
    "Afghan",
    "area":
    652230,
    "gini":
    27.8,
    "timezones": ["UTC+04:30"],
    "borders": ["IRN", "PAK", "TKM", "UZB", "TJK", "CHN"],
    "nativeName":
    "افغانستان",
    "numericCode":
    "004",
    "currencies": [{
        "code": "AFN",
        "name": "Afghan afghani",
        "symbol": "؋"
    }],
    "languages": [{
        "iso639_1": "ps",
        "iso639_2": "pus",
        "name": "Pashto",
        "nativeName": "پښتو"
    }, {
        "iso639_1": "uz",
        "iso639_2": "uzb",
        "name": "Uzbek",
        "nativeName": "Oʻzbek"
    }, {
        "iso639_1": "tk",
        "iso639_2": "tuk",
        "name": "Turkmen",
        "nativeName": "Türkmen"
    }],
    "translations": {
        "de": "Afghanistan",
        "es": "Afganistán",
        "fr": "Afghanistan",
        "ja": "アフガニスタン",
        "it": "Afghanistan",
        "br": "Afeganistão",
        "pt": "Afeganistão",
        "nl": "Afghanistan",
        "hr": "Afganistan",
        "fa": "افغانستان"
    },
    "flag":
    "https://restcountries.eu/data/afg.svg",
    "regionalBlocs": [{
        "acronym": "SAARC",
        "name": "South Asian Association for Regional Cooperation",
        "otherAcronyms": [],
        "otherNames": []
    }],
    "cioc":
    "AFG"
}

create_examples = {
    "simple_single_country": {
        "summary": "A simple document",
        "description": "A **simple** document with only a few fields",
        "value": simple_single_country
    },
    "complex_single_country": {
        "summary": "A complex document",
        "description":
        "A `complex` document with many fields of different types",
        "value": complex_single_country
    }
}

simple_countries_sample = { "index" : { "_index" : "country", "_id" : 0 } }

complex_countries_sample = """{ "index" : { "_index" : "country" } }
{'name': 'Afghanistan', 'topLevelDomain': ['.af'], 'alpha2Code': 'AF', 'alpha3Code': 'AFG', 'callingCodes': ['93'], 'capital': 'Kabul', 'altSpellings': ['AF', 'Afġānistān'], 'region': 'Asia', 'subregion': 'Southern Asia', 'population': 27657145, 'latlng': [33, 65], 'demonym': 'Afghan', 'area': 652230, 'gini': 27.8, 'timezones': ['UTC+04:30'], 'borders': ['IRN', 'PAK', 'TKM', 'UZB', 'TJK', 'CHN'], 'nativeName': 'افغانستان', 'numericCode': '004', 'currencies': [{'code': 'AFN', 'name': 'Afghan afghani', 'symbol': '؋'}], 'languages': [{'iso639_1': 'ps', 'iso639_2': 'pus', 'name': 'Pashto', 'nativeName': 'پښتو'}, {'iso639_1': 'uz', 'iso639_2': 'uzb', 'name': 'Uzbek', 'nativeName': 'Oʻzbek'}, {'iso639_1': 'tk', 'iso639_2': 'tuk', 'name': 'Turkmen', 'nativeName': 'Türkmen'}], 'translations': {'de': 'Afghanistan', 'es': 'Afganistán', 'fr': 'Afghanistan', 'ja': 'アフガニスタン', 'it': 'Afghanistan', 'br': 'Afeganistão', 'pt': 'Afeganistão', 'nl': 'Afghanistan', 'hr': 'Afganistan', 'fa': 'افغانستان'}, 'flag': 'https://restcountries.eu/data/afg.svg', 'regionalBlocs': [{'acronym': 'SAARC', 'name': 'South Asian Association for Regional Cooperation', 'otherAcronyms': [], 'otherNames': []}], 'cioc': 'AFG'}
{ "index" : { "_index" : "country" } }
{'name': 'Åland Islands', 'topLevelDomain': ['.ax'], 'alpha2Code': 'AX', 'alpha3Code': 'ALA', 'callingCodes': ['358'], 'capital': 'Mariehamn', 'altSpellings': ['AX', 'Aaland', 'Aland', 'Ahvenanmaa'], 'region': 'Europe', 'subregion': 'Northern Europe', 'population': 28875, 'latlng': [60.116667, 19.9], 'demonym': 'Ålandish', 'area': 1580, 'gini': None, 'timezones': ['UTC+02:00'], 'borders': [], 'nativeName': 'Åland', 'numericCode': '248', 'currencies': [{'code': 'EUR', 'name': 'Euro', 'symbol': '€'}], 'languages': [{'iso639_1': 'sv', 'iso639_2': 'swe', 'name': 'Swedish', 'nativeName': 'svenska'}], 'translations': {'de': 'Åland', 'es': 'Alandia', 'fr': 'Åland', 'ja': 'オーランド諸島', 'it': 'Isole Aland', 'br': 'Ilhas de Aland', 'pt': 'Ilhas de Aland', 'nl': 'Ålandeilanden', 'hr': 'Ålandski otoci', 'fa': 'جزایر الند'}, 'flag': 'https://restcountries.eu/data/ala.svg', 'regionalBlocs': [{'acronym': 'EU', 'name': 'European Union', 'otherAcronyms': [], 'otherNames': []}], 'cioc': ''}
{ "index" : { "_index" : "country" } }
{'name': 'Albania', 'topLevelDomain': ['.al'], 'alpha2Code': 'AL', 'alpha3Code': 'ALB', 'callingCodes': ['355'], 'capital': 'Tirana', 'altSpellings': ['AL', 'Shqipëri', 'Shqipëria', 'Shqipnia'], 'region': 'Europe', 'subregion': 'Southern Europe', 'population': 2886026, 'latlng': [41, 20], 'demonym': 'Albanian', 'area': 28748, 'gini': 34.5, 'timezones': ['UTC+01:00'], 'borders': ['MNE', 'GRC', 'MKD', 'KOS'], 'nativeName': 'Shqipëria', 'numericCode': '008', 'currencies': [{'code': 'ALL', 'name': 'Albanian lek', 'symbol': 'L'}], 'languages': [{'iso639_1': 'sq', 'iso639_2': 'sqi', 'name': 'Albanian', 'nativeName': 'Shqip'}], 'translations': {'de': 'Albanien', 'es': 'Albania', 'fr': 'Albanie', 'ja': 'アルバニア', 'it': 'Albania', 'br': 'Albânia', 'pt': 'Albânia', 'nl': 'Albanië', 'hr': 'Albanija', 'fa': 'آلبانی'}, 'flag': 'https://restcountries.eu/data/alb.svg', 'regionalBlocs': [{'acronym': 'CEFTA', 'name': 'Central European Free Trade Agreement', 'otherAcronyms': [], 'otherNames': []}], 'cioc': 'ALB'}
{ "index" : { "_index" : "country" } }
{'name': 'Algeria', 'topLevelDomain': ['.dz'], 'alpha2Code': 'DZ', 'alpha3Code': 'DZA', 'callingCodes': ['213'], 'capital': 'Algiers', 'altSpellings': ['DZ', 'Dzayer', 'Algérie'], 'region': 'Africa', 'subregion': 'Northern Africa', 'population': 40400000, 'latlng': [28, 3], 'demonym': 'Algerian', 'area': 2381741, 'gini': 35.3, 'timezones': ['UTC+01:00'], 'borders': ['TUN', 'LBY', 'NER', 'ESH', 'MRT', 'MLI', 'MAR'], 'nativeName': 'الجزائر', 'numericCode': '012', 'currencies': [{'code': 'DZD', 'name': 'Algerian dinar', 'symbol': 'د.ج'}], 'languages': [{'iso639_1': 'ar', 'iso639_2': 'ara', 'name': 'Arabic', 'nativeName': 'العربية'}], 'translations': {'de': 'Algerien', 'es': 'Argelia', 'fr': 'Algérie', 'ja': 'アルジェリア', 'it': 'Algeria', 'br': 'Argélia', 'pt': 'Argélia', 'nl': 'Algerije', 'hr': 'Alžir', 'fa': 'الجزایر'}, 'flag': 'https://restcountries.eu/data/dza.svg', 'regionalBlocs': [{'acronym': 'AU', 'name': 'African Union', 'otherAcronyms': [], 'otherNames': ['الاتحاد الأفريقي', 'Union africaine', 'União Africana', 'Unión Africana', 'Umoja wa Afrika']}, {'acronym': 'AL', 'name': 'Arab League', 'otherAcronyms': [], 'otherNames': ['جامعة الدول العربية', 'Jāmiʻat ad-Duwal al-ʻArabīyah', 'League of Arab States']}], 'cioc': 'ALG'}
{ "index" : { "_index" : "country" } }
{'name': 'American Samoa', 'topLevelDomain': ['.as'], 'alpha2Code': 'AS', 'alpha3Code': 'ASM', 'callingCodes': ['1684'], 'capital': 'Pago Pago', 'altSpellings': ['AS', 'Amerika Sāmoa', 'Amelika Sāmoa', 'Sāmoa Amelika'], 'region': 'Oceania', 'subregion': 'Polynesia', 'population': 57100, 'latlng': [-14.33333333, -170], 'demonym': 'American Samoan', 'area': 199, 'gini': None, 'timezones': ['UTC-11:00'], 'borders': [], 'nativeName': 'American Samoa', 'numericCode': '016', 'currencies': [{'code': 'USD', 'name': 'United State Dollar', 'symbol': '$'}], 'languages': [{'iso639_1': 'en', 'iso639_2': 'eng', 'name': 'English', 'nativeName': 'English'}, {'iso639_1': 'sm', 'iso639_2': 'smo', 'name': 'Samoan', 'nativeName': "gagana fa'a Samoa"}], 'translations': {'de': 'Amerikanisch-Samoa', 'es': 'Samoa Americana', 'fr': 'Samoa américaines', 'ja': 'アメリカ領サモア', 'it': 'Samoa Americane', 'br': 'Samoa Americana', 'pt': 'Samoa Americana', 'nl': 'Amerikaans Samoa', 'hr': 'Američka Samoa', 'fa': 'ساموآی آمریکا'}, 'flag': 'https://restcountries.eu/data/asm.svg', 'regionalBlocs': [], 'cioc': 'ASA'}
{ "index" : { "_index" : "country" } }
{'name': 'Andorra', 'topLevelDomain': ['.ad'], 'alpha2Code': 'AD', 'alpha3Code': 'AND', 'callingCodes': ['376'], 'capital': 'Andorra la Vella', 'altSpellings': ['AD', 'Principality of Andorra', "Principat d'Andorra"], 'region': 'Europe', 'subregion': 'Southern Europe', 'population': 78014, 'latlng': [42.5, 1.5], 'demonym': 'Andorran', 'area': 468, 'gini': None, 'timezones': ['UTC+01:00'], 'borders': ['FRA', 'ESP'], 'nativeName': 'Andorra', 'numericCode': '020', 'currencies': [{'code': 'EUR', 'name': 'Euro', 'symbol': '€'}], 'languages': [{'iso639_1': 'ca', 'iso639_2': 'cat', 'name': 'Catalan', 'nativeName': 'català'}], 'translations': {'de': 'Andorra', 'es': 'Andorra', 'fr': 'Andorre', 'ja': 'アンドラ', 'it': 'Andorra', 'br': 'Andorra', 'pt': 'Andorra', 'nl': 'Andorra', 'hr': 'Andora', 'fa': 'آندورا'}, 'flag': 'https://restcountries.eu/data/and.svg', 'regionalBlocs': [], 'cioc': 'AND'}
{ "index" : { "_index" : "country" } }
{'name': 'Angola', 'topLevelDomain': ['.ao'], 'alpha2Code': 'AO', 'alpha3Code': 'AGO', 'callingCodes': ['244'], 'capital': 'Luanda', 'altSpellings': ['AO', 'República de Angola', "ʁɛpublika de an'ɡɔla"], 'region': 'Africa', 'subregion': 'Middle Africa', 'population': 25868000, 'latlng': [-12.5, 18.5], 'demonym': 'Angolan', 'area': 1246700, 'gini': 58.6, 'timezones': ['UTC+01:00'], 'borders': ['COG', 'COD', 'ZMB', 'NAM'], 'nativeName': 'Angola', 'numericCode': '024', 'currencies': [{'code': 'AOA', 'name': 'Angolan kwanza', 'symbol': 'Kz'}], 'languages': [{'iso639_1': 'pt', 'iso639_2': 'por', 'name': 'Portuguese', 'nativeName': 'Português'}], 'translations': {'de': 'Angola', 'es': 'Angola', 'fr': 'Angola', 'ja': 'アンゴラ', 'it': 'Angola', 'br': 'Angola', 'pt': 'Angola', 'nl': 'Angola', 'hr': 'Angola', 'fa': 'آنگولا'}, 'flag': 'https://restcountries.eu/data/ago.svg', 'regionalBlocs': [{'acronym': 'AU', 'name': 'African Union', 'otherAcronyms': [], 'otherNames': ['الاتحاد الأفريقي', 'Union africaine', 'União Africana', 'Unión Africana', 'Umoja wa Afrika']}], 'cioc': 'ANG'}
{ "index" : { "_index" : "country" } }
{'name': 'Anguilla', 'topLevelDomain': ['.ai'], 'alpha2Code': 'AI', 'alpha3Code': 'AIA', 'callingCodes': ['1264'], 'capital': 'The Valley', 'altSpellings': ['AI'], 'region': 'Americas', 'subregion': 'Caribbean', 'population': 13452, 'latlng': [18.25, -63.16666666], 'demonym': 'Anguillian', 'area': 91, 'gini': None, 'timezones': ['UTC-04:00'], 'borders': [], 'nativeName': 'Anguilla', 'numericCode': '660', 'currencies': [{'code': 'XCD', 'name': 'East Caribbean dollar', 'symbol': '$'}], 'languages': [{'iso639_1': 'en', 'iso639_2': 'eng', 'name': 'English', 'nativeName': 'English'}], 'translations': {'de': 'Anguilla', 'es': 'Anguilla', 'fr': 'Anguilla', 'ja': 'アンギラ', 'it': 'Anguilla', 'br': 'Anguila', 'pt': 'Anguila', 'nl': 'Anguilla', 'hr': 'Angvila', 'fa': 'آنگویلا'}, 'flag': 'https://restcountries.eu/data/aia.svg', 'regionalBlocs': [], 'cioc': ''}
{ "index" : { "_index" : "country" } }
{'name': 'Antarctica', 'topLevelDomain': ['.aq'], 'alpha2Code': 'AQ', 'alpha3Code': 'ATA', 'callingCodes': ['672'], 'capital': '', 'altSpellings': [], 'region': 'Polar', 'subregion': '', 'population': 1000, 'latlng': [-74.65, 4.48], 'demonym': '', 'area': 14000000, 'gini': None, 'timezones': ['UTC-03:00', 'UTC+03:00', 'UTC+05:00', 'UTC+06:00', 'UTC+07:00', 'UTC+08:00', 'UTC+10:00', 'UTC+12:00'], 'borders': [], 'nativeName': 'Antarctica', 'numericCode': '010', 'currencies': [{'code': 'AUD', 'name': 'Australian dollar', 'symbol': '$'}, {'code': 'GBP', 'name': 'British pound', 'symbol': '£'}], 'languages': [{'iso639_1': 'en', 'iso639_2': 'eng', 'name': 'English', 'nativeName': 'English'}, {'iso639_1': 'ru', 'iso639_2': 'rus', 'name': 'Russian', 'nativeName': 'Русский'}], 'translations': {'de': 'Antarktika', 'es': 'Antártida', 'fr': 'Antarctique', 'ja': '南極大陸', 'it': 'Antartide', 'br': 'Antártida', 'pt': 'Antárctida', 'nl': 'Antarctica', 'hr': 'Antarktika', 'fa': 'جنوبگان'}, 'flag': 'https://restcountries.eu/data/ata.svg', 'regionalBlocs': [], 'cioc': ''}
{ "index" : { "_index" : "country" } }
{'name': 'Antigua and Barbuda', 'topLevelDomain': ['.ag'], 'alpha2Code': 'AG', 'alpha3Code': 'ATG', 'callingCodes': ['1268'], 'capital': "Saint John's", 'altSpellings': ['AG'], 'region': 'Americas', 'subregion': 'Caribbean', 'population': 86295, 'latlng': [17.05, -61.8], 'demonym': 'Antiguan, Barbudan', 'area': 442, 'gini': None, 'timezones': ['UTC-04:00'], 'borders': [], 'nativeName': 'Antigua and Barbuda', 'numericCode': '028', 'currencies': [{'code': 'XCD', 'name': 'East Caribbean dollar', 'symbol': '$'}], 'languages': [{'iso639_1': 'en', 'iso639_2': 'eng', 'name': 'English', 'nativeName': 'English'}], 'translations': {'de': 'Antigua und Barbuda', 'es': 'Antigua y Barbuda', 'fr': 'Antigua-et-Barbuda', 'ja': 'アンティグア・バーブーダ', 'it': 'Antigua e Barbuda', 'br': 'Antígua e Barbuda', 'pt': 'Antígua e Barbuda', 'nl': 'Antigua en Barbuda', 'hr': 'Antigva i Barbuda', 'fa': 'آنتیگوا و باربودا'}, 'flag': 'https://restcountries.eu/data/atg.svg', 'regionalBlocs': [{'acronym': 'CARICOM', 'name': 'Caribbean Community', 'otherAcronyms': [], 'otherNames': ['Comunidad del Caribe', 'Communauté Caribéenne', 'Caribische Gemeenschap']}], 'cioc': 'ANT'}
{ "index" : { "_index" : "country" } }
{'name': 'Argentina', 'topLevelDomain': ['.ar'], 'alpha2Code': 'AR', 'alpha3Code': 'ARG', 'callingCodes': ['54'], 'capital': 'Buenos Aires', 'altSpellings': ['AR', 'Argentine Republic', 'República Argentina'], 'region': 'Americas', 'subregion': 'South America', 'population': 43590400, 'latlng': [-34, -64], 'demonym': 'Argentinean', 'area': 2780400, 'gini': 44.5, 'timezones': ['UTC-03:00'], 'borders': ['BOL', 'BRA', 'CHL', 'PRY', 'URY'], 'nativeName': 'Argentina', 'numericCode': '032', 'currencies': [{'code': 'ARS', 'name': 'Argentine peso', 'symbol': '$'}], 'languages': [{'iso639_1': 'es', 'iso639_2': 'spa', 'name': 'Spanish', 'nativeName': 'Español'}, {'iso639_1': 'gn', 'iso639_2': 'grn', 'name': 'Guaraní', 'nativeName': "Avañe'ẽ"}], 'translations': {'de': 'Argentinien', 'es': 'Argentina', 'fr': 'Argentine', 'ja': 'アルゼンチン', 'it': 'Argentina', 'br': 'Argentina', 'pt': 'Argentina', 'nl': 'Argentinië', 'hr': 'Argentina', 'fa': 'آرژانتین'}, 'flag': 'https://restcountries.eu/data/arg.svg', 'regionalBlocs': [{'acronym': 'USAN', 'name': 'Union of South American Nations', 'otherAcronyms': ['UNASUR', 'UNASUL', 'UZAN'], 'otherNames': ['Unión de Naciones Suramericanas', 'União de Nações Sul-Americanas', 'Unie van Zuid-Amerikaanse Naties', 'South American Union']}], 'cioc': 'ARG'}
{ "index" : { "_index" : "country" } }
{'name': 'Armenia', 'topLevelDomain': ['.am'], 'alpha2Code': 'AM', 'alpha3Code': 'ARM', 'callingCodes': ['374'], 'capital': 'Yerevan', 'altSpellings': ['AM', 'Hayastan', 'Republic of Armenia', 'Հայաստանի Հանրապետություն'], 'region': 'Asia', 'subregion': 'Western Asia', 'population': 2994400, 'latlng': [40, 45], 'demonym': 'Armenian', 'area': 29743, 'gini': 30.9, 'timezones': ['UTC+04:00'], 'borders': ['AZE', 'GEO', 'IRN', 'TUR'], 'nativeName': 'Հայաստան', 'numericCode': '051', 'currencies': [{'code': 'AMD', 'name': 'Armenian dram', 'symbol': None}], 'languages': [{'iso639_1': 'hy', 'iso639_2': 'hye', 'name': 'Armenian', 'nativeName': 'Հայերեն'}, {'iso639_1': 'ru', 'iso639_2': 'rus', 'name': 'Russian', 'nativeName': 'Русский'}], 'translations': {'de': 'Armenien', 'es': 'Armenia', 'fr': 'Arménie', 'ja': 'アルメニア', 'it': 'Armenia', 'br': 'Armênia', 'pt': 'Arménia', 'nl': 'Armenië', 'hr': 'Armenija', 'fa': 'ارمنستان'}, 'flag': 'https://restcountries.eu/data/arm.svg', 'regionalBlocs': [{'acronym': 'EEU', 'name': 'Eurasian Economic Union', 'otherAcronyms': ['EAEU'], 'otherNames': []}], 'cioc': 'ARM'}
{ "index" : { "_index" : "country" } }
{'name': 'Aruba', 'topLevelDomain': ['.aw'], 'alpha2Code': 'AW', 'alpha3Code': 'ABW', 'callingCodes': ['297'], 'capital': 'Oranjestad', 'altSpellings': ['AW'], 'region': 'Americas', 'subregion': 'Caribbean', 'population': 107394, 'latlng': [12.5, -69.96666666], 'demonym': 'Aruban', 'area': 180, 'gini': None, 'timezones': ['UTC-04:00'], 'borders': [], 'nativeName': 'Aruba', 'numericCode': '533', 'currencies': [{'code': 'AWG', 'name': 'Aruban florin', 'symbol': 'ƒ'}], 'languages': [{'iso639_1': 'nl', 'iso639_2': 'nld', 'name': 'Dutch', 'nativeName': 'Nederlands'}, {'iso639_1': 'pa', 'iso639_2': 'pan', 'name': '(Eastern) Punjabi', 'nativeName': 'ਪੰਜਾਬੀ'}], 'translations': {'de': 'Aruba', 'es': 'Aruba', 'fr': 'Aruba', 'ja': 'アルバ', 'it': 'Aruba', 'br': 'Aruba', 'pt': 'Aruba', 'nl': 'Aruba', 'hr': 'Aruba', 'fa': 'آروبا'}, 'flag': 'https://restcountries.eu/data/abw.svg', 'regionalBlocs': [], 'cioc': 'ARU'}
{ "index" : { "_index" : "country" } }
{'name': 'Australia', 'topLevelDomain': ['.au'], 'alpha2Code': 'AU', 'alpha3Code': 'AUS', 'callingCodes': ['61'], 'capital': 'Canberra', 'altSpellings': ['AU'], 'region': 'Oceania', 'subregion': 'Australia and New Zealand', 'population': 24117360, 'latlng': [-27, 133], 'demonym': 'Australian', 'area': 7692024, 'gini': 30.5, 'timezones': ['UTC+05:00', 'UTC+06:30', 'UTC+07:00', 'UTC+08:00', 'UTC+09:30', 'UTC+10:00', 'UTC+10:30', 'UTC+11:30'], 'borders': [], 'nativeName': 'Australia', 'numericCode': '036', 'currencies': [{'code': 'AUD', 'name': 'Australian dollar', 'symbol': '$'}], 'languages': [{'iso639_1': 'en', 'iso639_2': 'eng', 'name': 'English', 'nativeName': 'English'}], 'translations': {'de': 'Australien', 'es': 'Australia', 'fr': 'Australie', 'ja': 'オーストラリア', 'it': 'Australia', 'br': 'Austrália', 'pt': 'Austrália', 'nl': 'Australië', 'hr': 'Australija', 'fa': 'استرالیا'}, 'flag': 'https://restcountries.eu/data/aus.svg', 'regionalBlocs': [], 'cioc': 'AUS'}
{ "index" : { "_index" : "country" } }
{'name': 'Austria', 'topLevelDomain': ['.at'], 'alpha2Code': 'AT', 'alpha3Code': 'AUT', 'callingCodes': ['43'], 'capital': 'Vienna', 'altSpellings': ['AT', 'Österreich', 'Osterreich', 'Oesterreich'], 'region': 'Europe', 'subregion': 'Western Europe', 'population': 8725931, 'latlng': [47.33333333, 13.33333333], 'demonym': 'Austrian', 'area': 83871, 'gini': 26, 'timezones': ['UTC+01:00'], 'borders': ['CZE', 'DEU', 'HUN', 'ITA', 'LIE', 'SVK', 'SVN', 'CHE'], 'nativeName': 'Österreich', 'numericCode': '040', 'currencies': [{'code': 'EUR', 'name': 'Euro', 'symbol': '€'}], 'languages': [{'iso639_1': 'de', 'iso639_2': 'deu', 'name': 'German', 'nativeName': 'Deutsch'}], 'translations': {'de': 'Österreich', 'es': 'Austria', 'fr': 'Autriche', 'ja': 'オーストリア', 'it': 'Austria', 'br': 'áustria', 'pt': 'áustria', 'nl': 'Oostenrijk', 'hr': 'Austrija', 'fa': 'اتریش'}, 'flag': 'https://restcountries.eu/data/aut.svg', 'regionalBlocs': [{'acronym': 'EU', 'name': 'European Union', 'otherAcronyms': [], 'otherNames': []}], 'cioc': 'AUT'}
{ "index" : { "_index" : "country" } }
{'name': 'Azerbaijan', 'topLevelDomain': ['.az'], 'alpha2Code': 'AZ', 'alpha3Code': 'AZE', 'callingCodes': ['994'], 'capital': 'Baku', 'altSpellings': ['AZ', 'Republic of Azerbaijan', 'Azərbaycan Respublikası'], 'region': 'Asia', 'subregion': 'Western Asia', 'population': 9730500, 'latlng': [40.5, 47.5], 'demonym': 'Azerbaijani', 'area': 86600, 'gini': 33.7, 'timezones': ['UTC+04:00'], 'borders': ['ARM', 'GEO', 'IRN', 'RUS', 'TUR'], 'nativeName': 'Azərbaycan', 'numericCode': '031', 'currencies': [{'code': 'AZN', 'name': 'Azerbaijani manat', 'symbol': None}], 'languages': [{'iso639_1': 'az', 'iso639_2': 'aze', 'name': 'Azerbaijani', 'nativeName': 'azərbaycan dili'}], 'translations': {'de': 'Aserbaidschan', 'es': 'Azerbaiyán', 'fr': 'Azerbaïdjan', 'ja': 'アゼルバイジャン', 'it': 'Azerbaijan', 'br': 'Azerbaijão', 'pt': 'Azerbaijão', 'nl': 'Azerbeidzjan', 'hr': 'Azerbajdžan', 'fa': 'آذربایجان'}, 'flag': 'https://restcountries.eu/data/aze.svg', 'regionalBlocs': [], 'cioc': 'AZE'}
{ "index" : { "_index" : "country" } }
{'name': 'Bahamas', 'topLevelDomain': ['.bs'], 'alpha2Code': 'BS', 'alpha3Code': 'BHS', 'callingCodes': ['1242'], 'capital': 'Nassau', 'altSpellings': ['BS', 'Commonwealth of the Bahamas'], 'region': 'Americas', 'subregion': 'Caribbean', 'population': 378040, 'latlng': [24.25, -76], 'demonym': 'Bahamian', 'area': 13943, 'gini': None, 'timezones': ['UTC-05:00'], 'borders': [], 'nativeName': 'Bahamas', 'numericCode': '044', 'currencies': [{'code': 'BSD', 'name': 'Bahamian dollar', 'symbol': '$'}], 'languages': [{'iso639_1': 'en', 'iso639_2': 'eng', 'name': 'English', 'nativeName': 'English'}], 'translations': {'de': 'Bahamas', 'es': 'Bahamas', 'fr': 'Bahamas', 'ja': 'バハマ', 'it': 'Bahamas', 'br': 'Bahamas', 'pt': 'Baamas', 'nl': 'Bahama’s', 'hr': 'Bahami', 'fa': 'باهاما'}, 'flag': 'https://restcountries.eu/data/bhs.svg', 'regionalBlocs': [{'acronym': 'CARICOM', 'name': 'Caribbean Community', 'otherAcronyms': [], 'otherNames': ['Comunidad del Caribe', 'Communauté Caribéenne', 'Caribische Gemeenschap']}], 'cioc': 'BAH'}
{ "index" : { "_index" : "country" } }
{'name': 'Bahrain', 'topLevelDomain': ['.bh'], 'alpha2Code': 'BH', 'alpha3Code': 'BHR', 'callingCodes': ['973'], 'capital': 'Manama', 'altSpellings': ['BH', 'Kingdom of Bahrain', 'Mamlakat al-Baḥrayn'], 'region': 'Asia', 'subregion': 'Western Asia', 'population': 1404900, 'latlng': [26, 50.55], 'demonym': 'Bahraini', 'area': 765, 'gini': None, 'timezones': ['UTC+03:00'], 'borders': [], 'nativeName': '\u200fالبحرين', 'numericCode': '048', 'currencies': [{'code': 'BHD', 'name': 'Bahraini dinar', 'symbol': '.د.ب'}], 'languages': [{'iso639_1': 'ar', 'iso639_2': 'ara', 'name': 'Arabic', 'nativeName': 'العربية'}], 'translations': {'de': 'Bahrain', 'es': 'Bahrein', 'fr': 'Bahreïn', 'ja': 'バーレーン', 'it': 'Bahrein', 'br': 'Bahrein', 'pt': 'Barém', 'nl': 'Bahrein', 'hr': 'Bahrein', 'fa': 'بحرین'}, 'flag': 'https://restcountries.eu/data/bhr.svg', 'regionalBlocs': [{'acronym': 'AL', 'name': 'Arab League', 'otherAcronyms': [], 'otherNames': ['جامعة الدول العربية', 'Jāmiʻat ad-Duwal al-ʻArabīyah', 'League of Arab States']}], 'cioc': 'BRN'}
{ "index" : { "_index" : "country" } }
{'name': 'Bangladesh', 'topLevelDomain': ['.bd'], 'alpha2Code': 'BD', 'alpha3Code': 'BGD', 'callingCodes': ['880'], 'capital': 'Dhaka', 'altSpellings': ['BD', "People's Republic of Bangladesh", 'Gônôprôjatôntri Bangladesh'], 'region': 'Asia', 'subregion': 'Southern Asia', 'population': 161006790, 'latlng': [24, 90], 'demonym': 'Bangladeshi', 'area': 147570, 'gini': 32.1, 'timezones': ['UTC+06:00'], 'borders': ['MMR', 'IND'], 'nativeName': 'Bangladesh', 'numericCode': '050', 'currencies': [{'code': 'BDT', 'name': 'Bangladeshi taka', 'symbol': '৳'}], 'languages': [{'iso639_1': 'bn', 'iso639_2': 'ben', 'name': 'Bengali', 'nativeName': 'বাংলা'}], 'translations': {'de': 'Bangladesch', 'es': 'Bangladesh', 'fr': 'Bangladesh', 'ja': 'バングラデシュ', 'it': 'Bangladesh', 'br': 'Bangladesh', 'pt': 'Bangladeche', 'nl': 'Bangladesh', 'hr': 'Bangladeš', 'fa': 'بنگلادش'}, 'flag': 'https://restcountries.eu/data/bgd.svg', 'regionalBlocs': [{'acronym': 'SAARC', 'name': 'South Asian Association for Regional Cooperation', 'otherAcronyms': [], 'otherNames': []}], 'cioc': 'BAN'}
{ "index" : { "_index" : "country" } }
{'name': 'Barbados', 'topLevelDomain': ['.bb'], 'alpha2Code': 'BB', 'alpha3Code': 'BRB', 'callingCodes': ['1246'], 'capital': 'Bridgetown', 'altSpellings': ['BB'], 'region': 'Americas', 'subregion': 'Caribbean', 'population': 285000, 'latlng': [13.16666666, -59.53333333], 'demonym': 'Barbadian', 'area': 430, 'gini': None, 'timezones': ['UTC-04:00'], 'borders': [], 'nativeName': 'Barbados', 'numericCode': '052', 'currencies': [{'code': 'BBD', 'name': 'Barbadian dollar', 'symbol': '$'}], 'languages': [{'iso639_1': 'en', 'iso639_2': 'eng', 'name': 'English', 'nativeName': 'English'}], 'translations': {'de': 'Barbados', 'es': 'Barbados', 'fr': 'Barbade', 'ja': 'バルバドス', 'it': 'Barbados', 'br': 'Barbados', 'pt': 'Barbados', 'nl': 'Barbados', 'hr': 'Barbados', 'fa': 'باربادوس'}, 'flag': 'https://restcountries.eu/data/brb.svg', 'regionalBlocs': [{'acronym': 'CARICOM', 'name': 'Caribbean Community', 'otherAcronyms': [], 'otherNames': ['Comunidad del Caribe', 'Communauté Caribéenne', 'Caribische Gemeenschap']}], 'cioc': 'BAR'}
{ "index" : { "_index" : "country" } }
{'name': 'Belarus', 'topLevelDomain': ['.by'], 'alpha2Code': 'BY', 'alpha3Code': 'BLR', 'callingCodes': ['375'], 'capital': 'Minsk', 'altSpellings': ['BY', 'Bielaruś', 'Republic of Belarus', 'Белоруссия', 'Республика Беларусь', 'Belorussiya', 'Respublika Belarus’'], 'region': 'Europe', 'subregion': 'Eastern Europe', 'population': 9498700, 'latlng': [53, 28], 'demonym': 'Belarusian', 'area': 207600, 'gini': 26.5, 'timezones': ['UTC+03:00'], 'borders': ['LVA', 'LTU', 'POL', 'RUS', 'UKR'], 'nativeName': 'Белару́сь', 'numericCode': '112', 'currencies': [{'code': 'BYN', 'name': 'New Belarusian ruble', 'symbol': 'Br'}, {'code': 'BYR', 'name': 'Old Belarusian ruble', 'symbol': 'Br'}], 'languages': [{'iso639_1': 'be', 'iso639_2': 'bel', 'name': 'Belarusian', 'nativeName': 'беларуская мова'}, {'iso639_1': 'ru', 'iso639_2': 'rus', 'name': 'Russian', 'nativeName': 'Русский'}], 'translations': {'de': 'Weißrussland', 'es': 'Bielorrusia', 'fr': 'Biélorussie', 'ja': 'ベラルーシ', 'it': 'Bielorussia', 'br': 'Bielorrússia', 'pt': 'Bielorrússia', 'nl': 'Wit-Rusland', 'hr': 'Bjelorusija', 'fa': 'بلاروس'}, 'flag': 'https://restcountries.eu/data/blr.svg', 'regionalBlocs': [{'acronym': 'EEU', 'name': 'Eurasian Economic Union', 'otherAcronyms': ['EAEU'], 'otherNames': []}], 'cioc': 'BLR'}
{ "index" : { "_index" : "country" } }
{'name': 'Belgium', 'topLevelDomain': ['.be'], 'alpha2Code': 'BE', 'alpha3Code': 'BEL', 'callingCodes': ['32'], 'capital': 'Brussels', 'altSpellings': ['BE', 'België', 'Belgie', 'Belgien', 'Belgique', 'Kingdom of Belgium', 'Koninkrijk België', 'Royaume de Belgique', 'Königreich Belgien'], 'region': 'Europe', 'subregion': 'Western Europe', 'population': 11319511, 'latlng': [50.83333333, 4], 'demonym': 'Belgian', 'area': 30528, 'gini': 33, 'timezones': ['UTC+01:00'], 'borders': ['FRA', 'DEU', 'LUX', 'NLD'], 'nativeName': 'België', 'numericCode': '056', 'currencies': [{'code': 'EUR', 'name': 'Euro', 'symbol': '€'}], 'languages': [{'iso639_1': 'nl', 'iso639_2': 'nld', 'name': 'Dutch', 'nativeName': 'Nederlands'}, {'iso639_1': 'fr', 'iso639_2': 'fra', 'name': 'French', 'nativeName': 'français'}, {'iso639_1': 'de', 'iso639_2': 'deu', 'name': 'German', 'nativeName': 'Deutsch'}], 'translations': {'de': 'Belgien', 'es': 'Bélgica', 'fr': 'Belgique', 'ja': 'ベルギー', 'it': 'Belgio', 'br': 'Bélgica', 'pt': 'Bélgica', 'nl': 'België', 'hr': 'Belgija', 'fa': 'بلژیک'}, 'flag': 'https://restcountries.eu/data/bel.svg', 'regionalBlocs': [{'acronym': 'EU', 'name': 'European Union', 'otherAcronyms': [], 'otherNames': []}], 'cioc': 'BEL'}
{ "index" : { "_index" : "country" } }
{'name': 'Belize', 'topLevelDomain': ['.bz'], 'alpha2Code': 'BZ', 'alpha3Code': 'BLZ', 'callingCodes': ['501'], 'capital': 'Belmopan', 'altSpellings': ['BZ'], 'region': 'Americas', 'subregion': 'Central America', 'population': 370300, 'latlng': [17.25, -88.75], 'demonym': 'Belizean', 'area': 22966, 'gini': 53.1, 'timezones': ['UTC-06:00'], 'borders': ['GTM', 'MEX'], 'nativeName': 'Belize', 'numericCode': '084', 'currencies': [{'code': 'BZD', 'name': 'Belize dollar', 'symbol': '$'}], 'languages': [{'iso639_1': 'en', 'iso639_2': 'eng', 'name': 'English', 'nativeName': 'English'}, {'iso639_1': 'es', 'iso639_2': 'spa', 'name': 'Spanish', 'nativeName': 'Español'}], 'translations': {'de': 'Belize', 'es': 'Belice', 'fr': 'Belize', 'ja': 'ベリーズ', 'it': 'Belize', 'br': 'Belize', 'pt': 'Belize', 'nl': 'Belize', 'hr': 'Belize', 'fa': 'بلیز'}, 'flag': 'https://restcountries.eu/data/blz.svg', 'regionalBlocs': [{'acronym': 'CARICOM', 'name': 'Caribbean Community', 'otherAcronyms': [], 'otherNames': ['Comunidad del Caribe', 'Communauté Caribéenne', 'Caribische Gemeenschap']}, {'acronym': 'CAIS', 'name': 'Central American Integration System', 'otherAcronyms': ['SICA'], 'otherNames': ['Sistema de la Integración Centroamericana,']}], 'cioc': 'BIZ'}

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