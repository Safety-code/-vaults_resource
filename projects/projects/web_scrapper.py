from cgitb import html
import urllib.request
#from urllib import urlopen

# url = "http://olympus.realpython.org/profiles/aphrodite"



# page = urllib.request.urlopen(url)

# html_bytes = page.read()
# html = html_bytes.decode("utf-8")

# print(html)

# #extracting text from html with string methods
# title_index = html.find('<title>')
# print(title_index)

# start_index = title_index + len("<title>")
# print(start_index)

# end_index = html.find("</title>")
# print(end_index)

# title = html[start_index:end_index]
# print(title)


#Second url to scrape
# url = "http://olympus.realpython.org/profiles/poseidon"
# page = urllib.request.urlopen(url)
# html = page.read().decode("utf-8")
# start_index = html.find("<title>") + len("<title>")
# end_index = html.find("</title>")
# title = html[start_index:end_index]
# print(title)

#REGEX 
import re
first = re.findall("ab*c", "ac")
first = re.findall("ab*c", "abcd")
first = re.findall("ab*c", "acc")
first = re.findall("ab*c", "abcac")
first = re.findall("ab*c", "abdc")
first = re.findall("ab*c", "ABC", re.IGNORECASE)
print(first)

#(.) looks for single characters in regular expressions
secre = re.findall("a.c", "abc")
secre = re.findall("a.c", "abbc")
secre = re.findall("a.c", "ac")
secre = re.findall("a.c", "acc")
print(secre)



