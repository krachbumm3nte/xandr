# Documentation of the Xandr-Investigation by netzpolitik.org

This repository contains the core tools used to investigate a [list of Advertisement-segments](https://web.archive.org/web/20230525225839/https://docs.xandr.com/en-US/bundle/monetize_monetize-standard/page/topics/data-marketplace-buyer-overview.html) accidentally published by Xandr/Microsoft on their website. This repository is not active, and only serves to archive our process and allow others to reproduce and expand on our findings. The results of this analysis were published on netzpolitik.org in August of 2023. # TODO: add link.

In this document, we will briefly cover the process that we employed:

## 1. Cleaning the data

The dataset (stored in [xandr_segments.csv](xandr_segments.csv)) contains roughly 650.000 Segments from over 90 Databrokers. Each row represents one segment, which is specified by four values: `Data Provider Name, Data Provider ID, Segment ID`  and `Segment Name`

A first look reveals that the data is somewhat messy: Most segment names appear to be hierarchically organized, i.e.:

`Cross Pixel > Audience portraits > Finance > Insurance Seekers`

Yet, providers use different styles to separate these hierarchical elements. Some providers do not structure their segments in a hierarchical fashion at all, and some do not even use human readable segment names. To deal with this, the dataset is being preprocessed in [01_cleanup.ipynb](01_cleanup.ipynb). This includes converting segment names to lowercase, replacing [diactrics](https://en.wikipedia.org/wiki/Diacritic) and removing some clutter. Segment names are then split in order to obtain a list of substrings that hopefully resembles the intended structure of the segment closely. Finally, some obviously useless segments are dropped from the Dataset.

Executing the notebook top to bottom produces (among others) the [xandr_segments_itemized.csv](xandr_segments_itemized.csv) file, on which all further analysis is based.


## 2. Identifying segments with regional data

With the [GDPR](https://gdpr-info.eu/), the EU has some of the more rigorous privacy laws in the world, and regluates collection and processing of [some specific types of data](https://gdpr-info.eu/art-9-gdpr/) strictly. Because of this (and the fact that we are a european medium), the EU was the focus of our investigation. To identify a segments that relate to people in the EU, several different approaches were used in concert. 

The file [eu_countries.json](eu_countries.json) contains relevant search strings for each of its member states:

- We accounted for country names in different languages, as well as reference to a language or ethnicity, i.e. `"denmark", "danish", "danmark"`. 

- Furthermore, we searched for [2- and 3-letter countrycodes](https://en.wikipedia.org/wiki/List_of_ISO_3166_country_codes) within the segment name. Since the string `"dk"` for example is rather common in the dataframe, country codes have to exactly match one of the hierarchical elements of a segment which we identified perviously.

- Finally, we identified a few country-specific branches of data providers which our script wouldn't have found without some assistance. For example, the strings `"xaxisdk"` and `"dk ndr"` occur repeatedly in the dataset. We identified these as the data providers "Xaxis" and "Nordic Data Resources", which also have branches in other countries, i.e. `"xaxisit", "xaxisnl" "xaxisfr"` or `"fi ndr", "se ndr"`, etc.. 
**Disclaimer: We made a judgement call here, and decided that segments identified by these strings most likely refer to the data these brokers collected about people in the respective countries. This seemed the most likely explanation for our findings, but remains unconfirmed.**

In [02_find_regional_segments.ipynb](02_find_regional_segments.ipynb) we filter the preprocessed dataframe according to these patterns. 

The dataset contains hundreds of segments relating to potential travel destinations, as well as some repeated false positives. Thus, we exclude some of the more obvious ones like `tour de france` and words relating to travelling like `destination, tourism`, etc.. 

The notebook stores all segments that likely refer to an EU-country in the file [xandr_segments_eu.csv](xandr_segments_eu.csv). In order to contrast our findings with the kind of data collected about people in the USA, a file called [xandr_segments_us.csv](xandr_segments_us.csv) is also created, which follows the same basic principles.


## 3. Sensitive data
To find segments that contain potentially sensitive information, we came up with several lists of terms ([spicy_words.py](spicy_words.py)) that might indicate such data. The keywords are roughly separated into the categories:  `'financial', 'personality', 'health', 'sex',  'latent_racism', 'religion', 'political'`. Some of the strings in these lists  are regex-formatted, in order to reduce the number of search terms required, so don't expect readability here.

In [03_find_spicy_segments.ipynb](03_find_spicy_segments.ipynb) the EU-dataset is scanned for matches with these regular expressions, and results are stored in separate files according to the aforementioned categories. 

### 3.1. Manual filtering
At this point, we had found a lot of segments that likely reference the EU, all of which contain a string that indicates that they might contain sensitive data. 

The number of false-positives was expectedly quite large, so we had to manually sift through the segments. We dropped segments where we felt that the local relation was too ambiguous. Judging how sensitive the data behind a segment is, naturally is much more nuanced work. We chose not to include  many of the edge-cases where the intention behind a segment was difficult to estimate. The fruits of our labour are found in [sensitive_eu_segments_master.csv](sensitive_eu_segments_master.csv).

Furthermore, we selected some of the most egregious segments - the filet - which are displayed as highlights on the map, and were furthermore discussed in the article. We separated between segments relating to the EU, the US, and those that do not refer to a any locality. The results can be found in the files [filet_eu.json](filet_eu.json), [filet_us.json](filet_us.json) and [filet_global.json](filet_global.json)  


## 4. Post-processing and visualization

Finally, we performed some minor post-processing and created files that could be directly uploaded to DataWrapper. This process is documented in [04_post_process_hand_filtered_dataset.ipynb](04_post_process_hand_filtered_dataset.ipynb).



# Credits

Johannes Gille and Sebastian Meineck for [netzpolitik.org](netzpolitik.org), August 2023

# License

This project is released under the GPLv3 License. 


