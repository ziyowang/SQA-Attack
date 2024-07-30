# Evaluation Code for:" Enhanced Query-Recovery Attacks against Searchable Encryption using Highly Distinctive Keywords"

# About 
This repository contains files to simulate our attack. The code should work, but there also have a lot of content that can be enhanced. And we have to emphasize that **we conduct our experiments in  ***Ubuntu*** and we do not test in ***windows*****.

# Attack code 
the code to conduct all attack are included in **Attacks** document and some relevant defense code are alsso included in the document.


# Similarity metric to calculate the distance 
In the **Similarity_cal** document, we list some relevant similarity metric that can be used to calcualte the distance between queires and keywords. Each metric is computed differently and adapted to different scenarios. In our experiments, we used the metric Ochiia because we found it to be effective in calculating the similarity and paired it with our similarity matrix.

# Query methods
DIfferent query methods can achieve different result. And the important distribution about ***ZIF*** are shown in document `utils` and the method that we use to calcualte **g_index** is also shown in this document.

# Utils 
Some methonds that can be used to solve programme problems are included in this document.

# Datasets

## Enron 
The Enron dataset we used can be downloaded from https://www.cs.cmu.edu/~enron/.

## Lucene
The Lucene dataset we used can be downloaded from downloaded from http://mail-archives.apache.org/mod_mbox/lucene-java-user.

## Lucene_reduced 
The Lucene_reduced we used can be acquired from the file `create_lucene_reduced.py` in dataset document. The main idea that we use this dataset is to make the size of **Enron** and **Lucene** are equal.
 
 
