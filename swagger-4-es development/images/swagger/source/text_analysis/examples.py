index_analyze_examples = {

    "Standard_Analyzer - The Bermudas": {
        "summary": "Standard (Default) Anayzer - The Bermudas.",
        "description": "Standard analyzer - `The Bermudas` is present in the source document.",
        "value": {
            "analyzer": "standard",
            "text": "The Bermudas"
        }
    },
    "Custom_Analyzer - The Bermudas": {
        "summary": "Custom Analyzer - The Bermudas.",
        "description": "Custom analyzer - `The Bermudas` is present in the source document.",
        "value": {
            "field": "name",
            "text": "The Bermudas"
        }
    },
    "Standard_Analyzer - Bermuda Republic": {
        "summary": "Standard (Default) Anayzer - Bermuda Republic",
        "description": "Standard analyzer - `Bermuda Republic` is present in the source document.",
        "value": {
            "analyzer": "standard",
            "text": "Bermuda Republic"
        }
    },
    "Custom_Analyzer - Bermuda Republic": {
        "summary": "Custom Analyzer - Bermuda Republic",
        "description": "Custom analyzer - `Bermuda Republic` is present in the source document.",
        "value": {
            "field": "name",
            "text": "Bermuda Republic"
        }
    }
}




analysis_examples = {
    "Standard_Analyzer": {
        "summary": "Standard Analyzer",
        "description":
        "Standard analyzer, note the lowercasing and removal of non leters an numbers.",
        "value": {
            "analyzer": "standard",
            "text": "Johnny #5 is Alive!!"
        }
    },
    "Keyword_Analyzer": {
        "summary": "Keyword Analyzer",
        "description":
        "Basically no analysis, no lowercasing, no tokenization, no removing punctuation - (just phrase in phrase out). ",
        "value": {
            "analyzer": "keyword",
            "text": "Johnny #5 is Alive!!"
        }
    },
    "Stop_Analyzer": {
        "summary": "Stop Analyzer",
        "description":
        "Stop analyzer example. Note the removal of the term `The`.",
        "value": {
            "analyzer": "stop",
            "text": "Johnny #5 is Alive!!"
        }
    },
    "Mapping_Character_Filter": {
        "summary": "Mapping Character Filter",
        "description":
        "Map one or multiple characters to different text. In this example we are mapping emojis.",
        "value": {
            "char_filter": [{
                "type": "mapping",
                "mappings": [":) => good", ":( => bad"]
            }],
            "tokenizer":
            "standard",
            "text":
            "I feel :)"
        }
    },
    "HTML_Strip_Character_Filter": {
        "summary": "HTML Strip Character Filter",
        "description":
        "Remove HTML from text. Really helpful if you are scrapping and indexing the extracted html. You can see in the example that all the HTML tags are removed. ",
        "value": {
            "char_filter": [{
                "type": "html_strip"
            }],
            "tokenizer":
            "standard",
            "text":
            """<details><summary>Background</summary>
        <b>interesting text</b>
        </p>"""
        }
    },
    "Pattern_Replace_Character_Filter": {
        "summary": "Pattern(regex) Replace Character Filter",
        "description":
        "Identify text to be replaced with a regex pattern. The example takes an account number string and creates a number "
        "from all the numbers contained in the string. ",
        "value": {
            "tokenizer":
            "standard",
            "char_filter": [{
                "pattern": "[^0-9]",
                "type": "pattern_replace",
                "replacement": ""
            }],
            "text":
            "#128-523-832-1 AUD",
        }
    },
    "Standard_Tokenizing": {
        "summary":
        "Standard Tokenizer",
        "description":
        "Grammer based tokenisation - note however the apostrophe `s` is kept with the preceding word in the example. "
        "This is the default configured tokenizer - really good value - you can get a long way with this tokenizer"
        "Note in the example we have also provided a lowercase filter to the analysis chain.",
        "value": {
            "tokenizer": "standard",
            "filter": ["lowercase"],
            "text": "#1 A Driving Instructor's rule."
        }
    },
    "Simple_Tokenizing": {
        "summary":
        "Simple Tokenizer",
        "description":
        "If you don't want to use one of the default tokenisers you can make your own. Here we specify a few different tokenize on characters. \n \n"
        "The example is intended to highlight this is actually harder than you think and users never type in what you expect.",
        "value": {
            "tokenizer": {
                "type": "char_group",
                "tokenize_on_chars": ["whitespace", "-", "\n", "."]
            },
            "text": "... it was delicious,today  ..."
        }
    },
    "Classic_Tokenizier": {
        "summary":
        "Classic Tokenizer",
        "description":
        "Pretty good for english toeknization however `standard` is preferred now with more general language support). \n"
        "Each tokenizer comes with some configuration parameters. For example `max token length` for the classic tokenizer. ",
        "value": {
            "tokenizer": {
                "type": "classic",
                "max_token_length": 5
            },
            "text": "... it was delicious,Today  ..."
        }
    },
    "Ngram_Tokenizier": {
        "summary":
        "Ngram Tokenizer",
        "description":
        "Standard Ngram tokenization of each word. Noting for ngram matching you probably need to use a "
        "diffrent search time analyzer. \n"
        "Cause the default behaviour will be to tokenize the search term through this analysis chain. ",
        "value": {
            "tokenizer": {
                "type": "ngram",
                "min_gram": 5,
                "max_gram": 6,
                "token_chars": ["letter", "digit"]
            },
            "filter": ["lowercase"],
            "text": ["... it was delicious,Today  ..."]
        }
    },
    "Edge_Ngram_Tokenizier": {
        "summary":
        "Edge Ngram Tokenizer",
        "description":
        "Standard Edge Ngram tokenization of each word. Noting for ngram matching you probably need to use a "
        "diffrent search time analyzer. \n"
        "Cause the default behaviour will be to tokenize the search term through this analysis chain. ",
        "value": {
            "tokenizer": {
                "type": "edge_ngram",
                "min_gram": 5,
                "max_gram": 12,
                "token_chars": ["letter", "digit"]
            },
            "text": "... it was delicious,Today  ..."
        }
    },
    "Keyword_Tokenizier": {
        "summary":
        "Keyword Tokenizier",
        "description":
        "Keyword tokenizing is basically no tokenisation. However you may wish to pair"
        "keyword tokenisation with a lower case filter, so whey you perform a term aggregation on the text"
        "values with mixed case will be merged together. Of note in the example is that the "
        "analyze endpoint does support a list of terms to analyze.",
        "value": {
            "tokenizer": {
                "type": "keyword"
            },
            "filter": ["lowercase"],
            "text": ["John Smith", "john smith"]
        }
    },
    "Simple_Pattern_Tokenizier": {
        "summary":
        "Simple Pattern Tokenizier",
        "description":
        "Tokenizing based on supplied simple patten. In this example we have "
        "some medicine and we want to strip the volumes out of the names",
        "value": {
            "tokenizer": {
                "type": "simple_pattern",
                "pattern": "[0123456789]{3,7}"
            },
            "filter": ["lowercase"],
            "text": ["Ventolin 110mg", "Becloforte-1000-mg"]
        }
    },
    "Character_Group_Tokenizer": {
        "summary": "Chracter Group Tokenizier",
        "description":
        "Super simple example of CSV tokenizing using the character group tokenizer",
        "value": {
            "tokenizer": {
                "type": "char_group",
                "tokenize_on_chars": [","]
            },
            "text": "James,Brown,Rules"
        }
    },
    "Apostrophe_Filter": {
        "summary": "Apostrophe Filter",
        "description": "Remove apostrophes and following text",
        "value": {
            "tokenizer": "standard",
            "filter": [{
                "type": "apostrophe"
            }],
            "text": ["John's runners", "the company's accounts"],
        }
    },
    "Stopword_Filter": {
        "summary": "Stopword Filter",
        "description": "Remove configured stopwords",
        "value": {
            "tokenizer":
            "standard",
            "filter": [{
                "type":
                "stop",
                "ignore_case":
                True
            
            }],
            "text":
            "to be or not to be, that is the question"
        }
    },
    "Stemming_Snowball_Filter": {
        "summary": "Stemming Snowball Filter",
        "description": "Stemming of tokens using the snowball algorithm",
        "value": {
            "tokenizer":
            "standard",
            "filter": [{
                "type": "lowercase"
            }, {
                "type": "snowball",
                "language": "english"
            }],
            "text":
            "Tennis player's racquets",
        }
    },
    "Stemming_Kstem_Filter": {
        "summary":
        "Stemming Kstem Filter",
        "description":
        "Stemming of tokens using the Kstem algorithm. Equivalent to the `light_english` stemmer. "
        ". Most of these stemming algorithms assume that the text has already been lower cased"
        ". Hence why we have the lowercasign filter as the first filter.",
        "value": {
            "tokenizer": "standard",
            "filter": [{
                "type": "lowercase"
            }, {
                "type": "kstem"
            }],
            "text": "Tennis player's racquets"
        }
    },
    "Stemming_English_Filter": {
        "summary": "Stemming English Filter",
        "description":
        "Standard english stemming. Noting the additional filters applied. ",
        "value": {
            "tokenizer":
            "standard",
            "filter": [{
                "type": "lowercase"
            }, {
                "type": "apostrophe"
            }, {
                "type": "stemmer"
            }],
            "text":
            "Tennis player's racquets"
        }
    },
    "Full_Custom_Analysis_Chain": {
        "summary": "Fully Custom Analysis Example",
        "description": "Example full custom analysis Chain. ",
        "value": {
            "char_filter": [{
                "type": "mapping",
                "mappings": [":) => good", ":( => bad"]
            }],
            "tokenizer":
            "standard",
            "filter": [{
                "type": "lowercase"
            }, {
                "type": "stemmer",
                "language": "english"
            }, {
                "type": "stop",
                "stopwords": ["i'm"]
            }],
            "text":
            "I'm feeling :)"
        }
    },
}
