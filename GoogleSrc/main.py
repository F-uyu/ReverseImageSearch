from PIL import Image
import imagehash, requests, lxml, re, urllib.request, json, os
from bs4 import BeautifulSoup
from io import BytesIO

"""crew = 'TestImages/img_1.jpg'
crew_img = Image.open(crew)
crew_hash = imagehash.whash(crew_img)
print(crew_hash)
short = 'https://di2ponv0v5otw.cloudfront.net/posts/2019/06/11/5d000d3e26219ffabbfae37d/m_5d000d46689ebcbdb63a2952.jpg'
short_img = Image.open(short)
short_hash = imagehash.whash(short_img)
print(short_hash)
similarity = crew_hash-short_hash
print(similarity)"""
