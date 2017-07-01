"""
This Source Code Form is subject to the terms of the Mozilla Public
License, v. 2.0. If a copy of the MPL was not distributed with this
file, You can obtain one at http://mozilla.org/MPL/2.0/.

"""
import urllib

from flask import Flask, request, send_file
from math import floor
from PIL import Image

_MAX_DIMEN_SIZE = 128
_OUT_FILE = './lol.png'

app = Flask(__name__)

@app.route('/', methods=['POST'])
def resize_image_path():
    url = request.form['url']  # Or use the hard-coded value.
    #url = 'https://upload.wikimedia.org/wikipedia/commons/8/8d/President_Barack_Obama.jpg'

    image = download_image(url)
    small_image = shrink_image(image)

    # TODO: I don't know if this actually saves pngs.
    # HACK: I don't know how to return file from memory so we save it.
    small_image.save(_OUT_FILE)
    return send_file(_OUT_FILE)

def download_image(im_url):
    # TODO: delete local file?
    # TODO: FileNotFoundError & OSError when non-image.
    local_filename, headers = urllib.request.urlretrieve(im_url)
    return Image.open(local_filename)  # File will be closed when data is processed.

def shrink_image(im):
    # Get an image with the largest dimension as MAX_DIMEN.
    width, height = im.size
    largest_dimen = width if width > height else height
    shrink_ratio = _MAX_DIMEN_SIZE / largest_dimen

    # values must be ints.
    new_size = tuple([floor(dimen * shrink_ratio) for dimen in im.size])
    return im.resize(new_size)
