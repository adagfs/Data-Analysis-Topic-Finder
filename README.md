# Data-Analysis-Topic-Finder

This is a data-analysis pipeline coded in Python. Below are a list of steps that are found within the code. Given a file we label document.txt, we 

1. read the file, creating a list which consists of the paragraphs that make up the document. 
2. Using ntlk and the TF-IDF algorithm, which was taking from https://github.com/yebrahim/TF-IDF-Generator (mildly tweaked and added documentation), find and score the frequency of words found in each paragraph.
3. Create an Array which contained pairs of paragraphs and the corresponding three words (tags) with the highest TF-IDF scores 
4. Create a csv file with the first column representing paragraphs and the second column representing the corresponding tags. 

##Limitations 
As I use the TF-IDF algorithm, this works best when given a very large document to look over. If only given a few small paragraphs, this algorithm will likely not find the best words that would be used as topics. 
