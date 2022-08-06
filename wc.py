from os import path
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

from wordcloud import WordCloud, STOPWORDS


# Read the whole text.
text = open('raw/input.txt').read()

# read the mask image
# taken from
# http://www.stencilry.org/stencils/movies/alice%20in%20wonderland/255fk.jpg
jasmine_mask = np.array(Image.open( "kank.jpg" ))

stopwords = set(STOPWORDS)
# stopwords.add("KN")

wc = WordCloud(background_color="white", max_words=2000, mask=jasmine_mask,
               stopwords=stopwords)

# generate word cloud
wc.generate(text)

# store to file
wc.to_file("jasmine.png")

# show
plt.imshow(wc, interpolation='bilinear')
plt.axis("off")
plt.figure()
plt.imshow(jasmine_mask, cmap=plt.cm.gray, interpolation='bilinear')
plt.axis("off")
plt.show()
