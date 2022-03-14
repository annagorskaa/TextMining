import clean_text as ct
import stemming_text as st

text = '''   <p> :-) Text mining techniques have become essential for supporting knowledge discovery as the volume 
and variety of digital text documents have increased, either in social networks and the Web or inside organizations. 
Text sources, :) as well as text mining applications, are varied. 
<b> Although there is not a consensual definition established among the different research communities [1] <b>, 
text mining can be seen as a set of methods used to analyze unstructured data and discover patterns ;(
that were unknown beforehand [2].<p>'''

# zadanie 1
print(ct.cleanup_text(text))


# zadanie 2
print(ct.delete_stop_words(text))


# zadanie 3
print(st.stemming_list(text))
