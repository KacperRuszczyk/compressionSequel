import streamlit as st

st.title(':orange[Algorithms]',anchor=False)
st.subheader('Here You can find brief explanations about the algorithms used in these three programs.',anchor=False)



cor1, col1, left, col2, right, col3 = st.columns([0.4,1, 0.8, 1, 0.8, 1])

with col1:
    st.header("Bzip2")   

with col2:
    st.header("Gzip")
    
with col3:
    st.header("Xz")
    
    
col1, left, col2, right, col3 = st.columns([1, 0.1, 1, 0.1, 1])
with col1:
    page4 = st.button("Burrows-Wheeler Transform")

with col2:
    page44 = st.button("Burrows-Wheeler Transform ")

with col3:
    page444 = st.button(" Burrows-Wheeler Transform")

with col1:
    page5 = st.button("Move-to-Front")

with col2:
    page55 = st.button(" Move-to-Front")

with col3:
    page6 = st.button("LZ77")

with col2:
    page66 = st.button("LZ77 ")

with col3:
    page7 = st.button("LZMA2")

with col2:
    page8 = st.button("Huffmana")





if page4 or page44 or page444:
    st.title('Burrows-Wheeler Transform (BWT)')  
    
    'The Burrows-Wheeler Transform is a data compression algorithm developed by Michael Burrows and David Wheeler.'
    'This technique transforms the input data sequence in such a way that similar characters are grouped together.'  
    'This transformation facilitates data compression. BWT sorts the data sequence, creating a new sequence where similar characters are close to each other.'

    st.image('images/Burrows-Wheeler.png', caption=None)

if page5 or page55:
    st.title('Move-to-Front (MTF)')
    
    'The Move-to-Front algorithm is a technique that transforms a data sequence by moving frequently occurring elements to the beginning of the sequence.'  
    'During the operation of the algorithm, the processed sequence is traversed, and each character is moved to the front.'  
    'Thanks to MTF, frequently occurring characters become easily encodable, leading to increased efficiency in the compression process.'  
    st.image('images/MTF.jpg')
if page6 or page66:
    st.title('LZ77')

    'The algorithm was developed in 1977 by Abraham Lempel and Ja’akow Ziv. A year later, the authors published an improved version of the method known as LZ78. The IEEE organization recognized the Lempel-Ziv algorithm as a milestone in the development of electronics and computer science.'  
    
    st.markdown('**Operation description:**') 
    
    '➖Initialization of the dictionary as an empty set.'
    '➖Analysis of the data sequence from left to right.' 
    '➖Searching for the longest repetition of a previously occurring fragment already present in the dictionary. The algorithm compares the current data fragment with phrases stored in the dictionary.'
    '➖If a repetition is found, information about it is saved in the form of a triplet (offset, length, next character) The offset represents the number of characters to backtrack in the data sequence to find the repetition. The length is the number of characters in the repetition, and the next character is the first character after the repetition.'
    '➖If no repetition is found, information about the current character is saved as a pair (0, current character), where 0 indicates no repetition, and the current character is directly stored.'
    '➖Information about repetitions is added to the dictionary for further comparison and compression of subsequent fragments.'
    st.image('images/LZ77.png')
if page8:
    st.title('Huffmana')

    'Developed by American computer scientist David Huffman in 1952, it is one of the simpler methods of lossless compression.'   
    'Therefore, it is used exclusively with other data compression algorithms, as in the case of the Gzip program where it is utilized alongside the LZ77 algorithm.'
    
    'The algorithm operates as follows:'
    
    st.markdown(':red[**Analysis of symbol frequencies:**]')
    '➖The algorithm begins by analyzing the data sequence to determine the frequencies of individual symbols. The number of occurrences of a symbol is called its frequency.'
     
    st.markdown(':red[**Construction of the Huffman tree:**]')
    '➖Based on frequency analysis, the algorithm constructs a tree with a binary structure, where nodes are labeled with symbols, and edges are labeled with 0 or 1.'
    
    '➖In the tree, symbols with higher frequencies are placed closer to the root, while symbols with lower frequencies are placed farther from the root.'
    
    st.markdown(':red[**Huffman coding:**]')
    '➖The algorithm assigns shorter bit codes to more frequently occurring symbols and longer bit codes to less frequently occurring symbols.'  
    '➖For each symbol, the Huffman code is determined by the path from the root to the leaf of the tree. This path consists of 0 and 1, where 0 denotes a left child transition, and 1 denotes a right child transition.'
    
    st.markdown(':red[**Generation of the compressed sequence:**]')
    '➖After assigning codes to symbols, the algorithm goes through the original data sequence and replaces each symbol with its corresponding code.'
    '➖As a result, a compressed data sequence is obtained, in which longer bit codes have been replaced with shorter codes for more frequently occurring symbols.'
    st.image('images/Hoffman.png')
if page7:
    st.title('LZMA // LZMA2')

    st.markdown(':red[**LZMA**]')
    'The algorithm, developed since 1996 or 1998 by Igor Pavlov, utilizes symbols and dictionary references as its fundamental compression units, similar to LZ77.' 
    'Symbols represent shorter data sequences that occur at a particular location, while references point to the position from which a pattern can be reconstructed in the dictionary. LZ77, on the other hand, directly uses references to previous occurrences of patterns in a sliding window, consisting of an offset (distance) and the length of the repeated fragment.'   
    'In addition to dictionary compression, LZMA also employs length encoding and other optimization techniques. Length encoding assigns shorter codes to more frequently occurring symbols, contributing to further size reduction.'


    st.markdown(':red[**LZMA2**]')
    'LZMA and LZMA2 are two versions of the same algorithm. LZMA2 introduces the concept of "filters" that can be applied in the compression process.'   
    'Filters are different compression algorithms that can be combined in chains to optimize compression for specific types of data.' 

    st.image('images/LZMA.png')
