# -*- coding: utf-8 -*-
"""
Python script to download web page(s) passed in
Returns metadata for the downloaded web pages (number of links, number of images, date fetched
Arguments: File path for web page download, URL (can be multiple URLs)
Written by Matthew Dill
"""

import sys
import requests
import validators
from bs4 import BeautifulSoup
from datetime import datetime
from pywebcopy import save_webpage

#Function to return image count from web page
def get_img_count(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'lxml')
    print("Images: " + str(len(soup.find_all('img'))))

#Function to return link count from web page
def get_links(url):
    r = requests.get(url)
    html_content = r.text
    soup = BeautifulSoup(html_content, 'lxml')
    links = [a.get('href') for a in soup.find_all('a', href=True)]
    print("Links: " + str(len(links)))

#read arguments from command line
input_list = sys.argv
input_list.pop(0)
filepath = input_list.pop(0)

#iterate through each url from input, 
#download web page data, and print metadata
for url in input_list:
    if(validators.url(url)):
        kwargs = {'bypass_robots': True, 'project_name': 'fetch'}
        save_webpage(url, filepath, **kwargs)
        print("\nSite: " + url)
        get_links(url)
        get_img_count(url)
        print("Last Fetch: " + datetime.today().strftime('%Y-%m-%d %H:%M:%S'))
    else:
        print("\nInvalid url")
