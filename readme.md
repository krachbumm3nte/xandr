# Documentation of the Xandr-Investigation by netzpolitik.org


This repository contains the core tools used to investigate a [list of Advertisement-segments](https://web.archive.org/web/20230525225839/https://docs.xandr.com/en-US/bundle/monetize_monetize-standard/page/topics/data-marketplace-buyer-overview.html) accidentally published by Xandr/Microsoft on their website. This repository is not active, and only serves to archive our process and allow others to reproduce and expand on our findings. The results of this analysis were published on netzpolitik.org in August of 2023. # TODO: add link.


In this document, we will briefly cover the process that we employed in our data analysis and explain the content of the repository:


## 1. Cleaning the data


The dataset (stored in [xandr_segments.csv](xandr_segments.csv)) contains roughly 650.000 Segments. The names of about 90 data brokers are assigned to them. Each row represents one segment, which is specified by four values: Data Provider Name, Data Provider ID, Segment ID and Segment Name


A first look reveals that the data is somewhat messy: Most segment names appear to be hierarchically organized, i.e.:


Cross Pixel > Audience portraits > Finance > Insurance Seekers


Yet, depending on the named provider there are different styles to separate these hierarchical elements. Some segments are not structured in a hierarchical fashion at all, and some do not even have human readable segment names. To deal with this, the dataset is being preprocessed in [01_cleanup.ipynb](01_cleanup.ipynb). This includes converting segment names to lowercase, replacing [diactrics](https://en.wikipedia.org/wiki/Diacritic) and removing some clutter. Segment names are then split in order to obtain a list of substrings that hopefully resembles the intended structure of the segment closely. Finally, some obviously useless segments are dropped from the Dataset.


Executing the notebook top to bottom produces (among others) the [xandr_segments_itemized.csv](xandr_segments_itemized.csv) file, on which all further analysis is based.



## 2. Identifying segments with regional data


With the [GDPR](https://gdpr-info.eu/), the EU has some of the more rigorous privacy laws in the world, and regulates collection and processing of [some specific types of data](https://gdpr-info.eu/art-9-gdpr/) strictly. Because of this (and the fact that we are a European medium), the EU was the focus of our investigation. To identify segments that apparently relate to people in the EU, several different approaches were used in concert.


The file [eu_countries.json](eu_countries.json) contains relevant search strings for each of its member states:

- We accounted for country names in different languages, as well as reference to a language or ethnicity, i.e. "denmark", "danmark", "danish". 

- Furthermore, we searched for [2- and 3-letter countrycodes](https://en.wikipedia.org/wiki/List_of_ISO_3166_country_codes) within the segment name. Since the string "dk" for example is rather common in the dataframe, country codes have to exactly match one of the hierarchical elements of a segment which we identified previously.

- Finally, we identified a few country-specific branches of data providers which our script wouldn't have found without some assistance. For example, the strings "xaxisdk" and "dk ndr" occur repeatedly in the dataset. We identified these as the data providers "Xaxis" and "Nordic Data Resources", which also have branches in other countries, i.e. "xaxisit", "xaxisnl" "xaxisfr" or "fi ndr", "se ndr", etc.. **Disclaimer: We made a judgment call here, and decided that segments identified by these strings most likely refer to people in the respective countries. At least none of the data vendors we confronted denied that the country codes refer to EU countries.**

In [02_find_regional_segments.ipynb](02_find_regional_segments.ipynb) we filter the preprocessed dataframe according to these patterns.


The dataset contains hundreds of segments relating to potential travel destinations, as well as some repeated false positives. Thus, we exclude some of the more obvious ones like "tour de france" and words relating to traveling like "destination", "tourism", etc..


The notebook stores all segments that likely refer to an EU-country in the file [xandr_segments_eu.csv](xandr_segments_eu.csv). In order to contrast our findings with the kind of data collected about people in the USA, a file called [xandr_segments_us.csv](xandr_segments_us.csv) is also created, which is generated by the same principles.



## 3. Data on personal characteristics

To find segments that may contain data on personal characteristics or even sensitive data, we came up with several lists of terms ([spicy_words.py](spicy_words.py)) that might indicate such data. The keywords are roughly separated into the categories: 'financial', 'personality', 'health', 'sexuality', 'race', 'religion', 'political', 'children'. Some of the strings in these lists are regex-formatted, in order to reduce the number of search terms required, so don't expect readability here.


In [03_find_spicy_segments.ipynb](03_find_spicy_segments.ipynb) the EU-dataset is scanned for matches with these regular expressions, and results are stored in separate files according to the aforementioned categories.


### 3.1. Manual filtering
At this point, we had found a lot of segments that likely reference the EU, all of which contain a string that indicates that they might relate to the categories we previously defined. 


The number of false-positives was expectedly quite large, so we had to manually sift through the segments. Each segment has been vetted by two **people**. We dropped segments where we felt that the local relation was too ambiguous. Judging how personal the data behind a segment is, naturally is much more nuanced work. We chose not to include many of the edge-cases where the intention behind a segment was difficult to estimate. The fruits of our labor are found in [filtered_eu_segments_master.csv](filtered_eu_segments_master.csv).

Furthermore, we selected some some illustrative segments - the filet - which are displayed as highlights on the maps and/or further discussed in our article. We separated between segments relating to the EU, the US, and those that apparently do not refer to a any locality. The results can be found in the files [filet_eu.json](filet_eu.json), [filet_us.csv](filet_us.csv) and [filet_global.csv](filet_global.csv)


## 4. Post-processing and visualization

Finally, we performed some minor post-processing for better readability and created files that could be directly uploaded to DataWrapper. This process is documented in [04_post_process_hand_filtered_dataset.ipynb](04_post_process_hand_filtered_dataset.ipynb). This script also creates three folders in which the potentially sensitive segments with reference to the EU are structured into individual files by [broker](eu_segments_by_broker), by [category](eu_segments_by_category) and by [country](eu_segments_by_country).



For the interpretation, analysis and limitations of our research, please refer to the article on [netzpolitik.org](netzpolitik.org)


# Credits


Johannes Gille and Sebastian Meineck for [netzpolitik.org](netzpolitik.org), August 2023


# License

This project is released under the GPLv3 License.
