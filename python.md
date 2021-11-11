1)What data structures do you know and what their differences?

tuple, list, dictionary, set, string, class

More details here https://python.swaroopch.com/data_structures.html

list - mutable array, del - for removing
set - unordered set

Also, exist sequences, which related to tuples, strings, list, they have indexes, slices and `in` and `not in` operations

2) What libraries do you use
- luigi
- pandas
- sklearn 
- xgboost
- tenseflow
- searborn
- celery

3)	What the benefit of generators?

We don't use memory for creating list items, just use counter to iterate through the objects.

4) Why does pandas dataframe take up memory more memory than file where he saved?
Because of DF consist of three main parts in context of memory usage:
- data
- indexes
- columns data

Also when pands extracts data from the file it decides not th ebest types for columns, to make it better need to set up data types manually.

5)
