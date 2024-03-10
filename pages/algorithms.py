import streamlit as st




'''Bzip2:
Burrows-Wheeler Transform (BWT)
Move-to-Front (MTF)

Gzip:
Burrows-Wheeler Transform (BWT)
Move-to-Front (MTF)
LZ77
Huffmana

Xz:
Burrows-Wheeler Transform (BWT)
LZ77
LZMA2'''


st.set_page_config(
    page_title='Algorithms information',
    page_icon='📄',
    initial_sidebar_state='expanded'
)



st.markdown('Burrows-Wheeler Transform (BWT)')
BWT = '''The Burrows-Wheeler Transform is a data compression algorithm developed by Michael Burrows and David Wheeler.  
This technique transforms the input data sequence in such a way that similar characters are grouped together.  
This transformation facilitates data compression. BWT sorts the data sequence, creating a new sequence where similar characters are close to each other.  
The Burrows-Wheeler Transform algorithm has been utilized in programs such as Gzip, Bzip2, and Xz.'''

st.markdown(BWT)

st.markdown('Move-to-Front (MTF)')
MTF = '''The Move-to-Front algorithm is a technique that transforms a data sequence by moving frequently occurring elements to the beginning of the sequence.  
During the operation of the algorithm, the processed sequence is traversed, and each character is moved to the front.  
Thanks to MTF, frequently occurring characters become easily encodable, leading to increased efficiency in the compression process.  
The Move-to-Front algorithm has been used in the Gzip and Bzip2 programs.'''

st.markdown(MTF)

st.markdown('LZ77')
LZ77 = '''The algorithm was developed in 1977 by Abraham Lempel and Ja’akow Ziv.  
A year later, the authors published an improved version of the method known as LZ78.  
The IEEE organization recognized the Lempel-Ziv algorithm as a milestone in the development of electronics and computer science.  

The LZ77 algorithm has been utilized in programs such as Gzip and Xz.   

Operation description:  

➖Initialization of the dictionary as an empty set.  
➖Analysis of the data sequence from left to right.  
➖Searching for the longest repetition of a previously occurring fragment already present in the dictionary.
  The algorithm compares the current data fragment with phrases stored in the dictionary.
➖If a repetition is found, information about it is saved in the form of a triplet (offset, length, next character). 
  The offset represents the number of characters to backtrack in the data sequence to find the repetition.  
  The length is the number of characters in the repetition, and the next character is the first character after the repetition.
➖If no repetition is found, information about the current character is saved as a pair (0, current character),
  where 0 indicates no repetition, and the current character is directly stored.
➖Information about repetitions is added to the dictionary for further comparison and compression of subsequent fragments.'''

st.markdown(LZ77)


st.markdown('Huffmana')
Huffmana = '''Developed by American computer scientist David Huffman in 1952, it is one of the simpler methods of lossless compression.   
Therefore, it is used exclusively with other data compression algorithms, as in the case of the Gzip program where it is  
utilized alongside the LZ77 algorithm. The algorithm operates as follows:

Analysis of symbol frequencies:
➖The algorithm begins by analyzing the data sequence to determine the frequencies of individual symbols.
  The number of occurrences of a symbol is called its frequency.
  
Construction of the Huffman tree:
➖Based on frequency analysis, the algorithm constructs a tree with a binary  
  structure, where nodes are labeled with symbols, and edges are labeled with 0 or 1.
  
➖In the tree, symbols with higher frequencies are placed closer to the root,  
  while symbols with lower frequencies are placed farther from the root.
  
Huffman coding:
➖The algorithm assigns shorter bit codes to more frequently occurring symbols and  
  longer bit codes to less frequently occurring symbols.  
➖For each symbol, the Huffman code is determined by the path from the root to the  
  leaf of the tree. This path consists of 0 and 1, where 0 denotes a left child transition,
  and 1 denotes a right child transition.
  
Generation of the compressed sequence:
➖After assigning codes to symbols, the algorithm goes through the original data   
  sequence and replaces each symbol with its corresponding code.
➖As a result, a compressed data sequence is obtained, in which longer bit codes  
  have been replaced with shorter codes for more frequently occurring symbols.'''

st.markdown(Huffmana)


st.markdown('LZMA')
LZMA = '''The algorithm, developed since 1996 or 1998 by Igor Pavlov, 
utilizes symbols and dictionary references as its fundamental compression units, similar to LZ77.  
Symbols represent shorter data sequences that occur at a particular location, 
while references point to the position from which a pattern can be reconstructed in the dictionary. 
LZ77, on the other hand, directly uses references to previous occurrences of patterns in a sliding window, 
consisting of an offset (distance) and the length of the repeated fragment.  

In addition to dictionary compression, LZMA also employs length encoding and other optimization techniques.  
Length encoding assigns shorter codes to more frequently occurring symbols, contributing to further size reduction.'''

st.markdown(LZMA)

st.markdown('LZMA2')
LZMA2 = '''LZMA and LZMA2 are two versions of the same algorithm.  
LZMA2 introduces the concept of "filters" that can be applied in the compression process.   
 Filters are different compression algorithms that can be combined in chains to optimize compression for specific types of data.   
 
 The LZMA algorithm has been used in the Xz program.'''
st.markdown(LZMA2)
