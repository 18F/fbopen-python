# fbopen-python-client

Python access to the [FBOpen API](http://18f.github.io/fbopen/).

## Installation (tdb--git clone for now)

## Usage

```python
from fbopen import fbopen

FBOpen = fbopen.FBOpen

# Initialize with api key 
FBOpen.init("myKey")

# You can get a key at api.data.gov
# Keyless entry through this library is coming soon

# Search Opps
collection = FBOpen.Opp.search("computer software")

# Search with options
collection = FBOpen.Opp.search("bioinformatics", {"start" : 2})

# Inspect the collection
collection.numFound
collection.maxScore
collection.start

# Get the Opps
opps = collection.opps

# Inspect an Opp
opp = opps[1]
opp.id
opp.title
opp.agency
opp.description
opp.summary
opp.listing_url
# and many more ...
# see http://18f.github.io/fbopen/ for a full list
```

### Development

To run the tests, create a `.env` in the root of this library:

```sh
cp .env.example .env
```

Go to https://api.data.gov/signup/ to get an API key and add that to your new `.env` file.

Then:

```sh
$ pip install -r requirements.txt
$ python setup.py test
```

### TODO

1. Better tests
2. Documentation (readthedocs.org ?)
3. Deploy on pip
4. Choose between `.rst` or `.md`


### Public domain

This project is in the worldwide [public domain](LICENSE.md). As stated in [CONTRIBUTING](CONTRIBUTING.md):

> This project is in the public domain within the United States, and copyright and related rights in the work worldwide are waived through the [CC0 1.0 Universal public domain dedication](https://creativecommons.org/publicdomain/zero/1.0/).
>
> All contributions to this project will be released under the CC0 dedication. By submitting a pull request, you are agreeing to comply with this waiver of copyright interest.

