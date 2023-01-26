
# Export Bookmarks from Pinboard.in to Raindrop.io

A simple script that will convert your [Pinboard](https://pinboard.in) bookmarks so they can be uploaded to [Raindrop.io](https://raindrop.io) 

# Usage

Step 1:

Use the Pinboard API to extract a full backup of your bookmarks in JSON format:
```
curl -s --header "Content-Type: application/x-www-form-urlencoded" \
"https://api.pinboard.in/v1/posts/all?format=json&auth_token=<TOKEN>" \
| jq . >> pinboard.json
```
You can find your API `auth_token` by going to - settings -> password in your Pinboard account.

Step 2:

```
python3 main.py --pinboard pinboard.json --csv raindrop_upload.csv --collection "Pinboard Uploads"
```

Step 3:

Go to Raindrop.io -> Settings -> Import Data and select raindrop_upload.csv 

# Documentation

See https://help.raindrop.io/import/#csv

# License
```
The MIT License (MIT)

Copyright (c) 2023 Usman Mahmood

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```
