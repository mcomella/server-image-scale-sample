# server-image-rescale
This is a quick sample of how a server might downscale images that are sent to
it.

The server takes a POST request to `/` with the following *encoded* parameters:
* url: the url of an image you want the server to downscaled

The server will return the downscaled image.

## Setup
Run the following:
```sh
virtualenv -p python3 venv  # Create virtualenv.
source venv/bin/activate  # Start the virtualenv.
pip install -r requirements.txt  # Install dependencies.
```

## Running
With the virtualenv activated, run the server:

```sh
FLASK_APP=main.py flask run
```

By default, it will run at http://127.0.0.1:5000/.

## Testing the server
You can test the server with a curl request. For example, to request the server
to downscale, save the downscaled image to a file, and open it (on OS X), you
might call:

```sh
curl --data "url=https%3A%2F%2Fupload.wikimedia.org%2Fwikipedia%2Fcommons%2F8%2F8d%2FPresident_Barack_Obama.jpg" 127.0.0.1:5000/ > lol.png && open lol.png
```

The server will return a downscaled version of [this
image](https://upload.wikimedia.org/wikipedia/commons/8/8d/President_Barack_Obama.jpg).
