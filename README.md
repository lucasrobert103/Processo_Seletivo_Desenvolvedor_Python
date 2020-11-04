# Processo_Seletivo_Desenvolvedor_Pyton
Shooju Simple Task

By: lucas Robert Dos Santos Bueno


Desafio


### Background

* General info on the data is here `https://www.jodidata.org/gas/database/data-downloads-beta.aspx` and a detailed description of the dataset here `https://www.jodidata.org/_resources/files/downloads/manuals/jodi-gas-manual.pdf`
* General time series info is here `https://en.wikipedia.org/wiki/Time_series`

### Task

The goal is to create a *single* python2/3 file that *uses only standard libraries* that:

1. Uses only the URL `https://www.jodidata.org/_resources/files/downloads/gas-data/jodi_gas_csv_beta.zip` as input
2. Downloads, unzips, parses based on that single URL input
3. Writes to stdout a new line delimited (\n) JSON series-by-series representation of the input CSV

Each JSON series representation should be an object with 3 keys:

* series_id: some unique series id; it should be meaningful to the series it is identifying
* points: an array of date(time)/float arrays; the date(time) should be in ISO format as defined at `https://en.wikipedia.org/wiki/ISO_8601`
* fields: an object of any additional metadata available at the source that helps to describe and identify the data; a series representing Brazilian GDP might have two main keys: "country" and "concept" as in the example below

Below is an example of a single JSON series (with new lines only for readability; this data is not related to the data from the task above -- it just shows structure):

    {
        "series_id":"my-data\\brazil\\GDP",
        "points":[
          ["2016-01-01", 12.3],
          ["2017-01-01", 12.7],
          ["2018-01-01", 13.1]
        ],
        "fields":{
          "country":"Brazil",
          "concept":"Gross Domestic Product",
          "units":"USD, Millions",
          "source":"IMF"
        }
    }

The python script should output one series per line, and each line should be valid JSON (like above).