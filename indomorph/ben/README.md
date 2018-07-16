# Morphological Analyzer for Bengali

This is a simple morph analyzer for Bengali (Bangla). Currently, it only analyzes nouns, though a version with some coverage of verbs is forthcoming.

Usage:

```shell
$ foma -l ben.xfst -s # Compile the FST
$ echo "" | flookup -a ben.fst
```
