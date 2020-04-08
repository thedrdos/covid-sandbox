"""
Created on 2020/03/31

@author: David O. Sigthorsson (sigthorsson@gmail.com)

Make a website out of some of the COVID data and processing work in an adjacent project

"""

import os
import markdown
import codecs
import webbrowser
from datetime import datetime
import time

# Copy plots from original project
os.system('cp ../../DOS-Covid-Code/Plots/*sandbox.html ./Plots/')

# Log current time
now = datetime.now();
now = now.strftime("%d-%b-%Y (%H:%M:%S)")

# Assign input/output files
md_file = "./main.md"
html_file = "./index.html"
plots_path= "./Plots/"

# Read the markdown document and encoded it
input_file = codecs.open(md_file, mode="r", encoding="utf-8")
text = input_file.read()
text = text+"\n* Updated on "+now+"\n"

# Automatically add all html plots
plots_names = []
for f_name in os.listdir(plots_path): # Find all the plots ending in html
     if f_name.endswith('sandbox.html'):
         plots_names.append(f_name)

str = [];
for name in plots_names: # construct the appropriate inclusion of the html plots in markdown
#     str.append('''
# ## {}
# <iframe src="{}"
#     sandbox="allow-same-origin allow-scripts"
#     width="100%"
#     height="100%"
#     scrolling="no"
#     seamless="seamless"
#     frameborder="0">
# </iframe>
# '''.format(name[:-5], plots_path+name))
    str.append('''
## [{}]({})
<iframe src="{}"
sandbox="allow-same-origin allow-scripts"
width="100%"
height="100%"
scrolling="yes"
seamless="seamless"
frameborder="10">
</iframe>
'''.format(name[:-5], plots_path+name,plots_path+name))


text = text+"".join(str) # Join with the markdown header

text = text+"## End";

# Make the webpage from the markdown
html = markdown.markdown(text)

# Write the encoded markdown to a file
output_file = codecs.open(html_file, "w",
                          encoding="utf-8",
                          errors="xmlcharrefreplace"
)
output_file.write(html)
output_file.close();

# Open the webpage to check it locally
webbrowser.open("file://"+os.path.abspath(html_file))

# Post to the website
os.system('git ca "Updated using script on: '+now+'"'+'; git push')
