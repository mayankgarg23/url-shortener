## Url Shortener

**{bitlink} -> shortened url with domain name and unique hash value everytime shorten url or create url is called**

**{bitlink} - 'link' field of response from request**

**Shorten a Link**
-----

Converts a long url to a Bitlink.

POST /v4/shorten

**Request**
```
curl \
-H 'Content-Type: application/json' \
-X POST \
-d '{
  "long_url": "https://www.google.com",
  "domain": "clone_bit.ly"
}' \
http://localhost:5000/v4/shorten
```
**Response**
```
{"created_at":"03/10/2021 18:54:52", "link":"clone_bit.ly/FDFl2dt", "long_url":"https://www.google.com"}
```


**Redirect a Bitlink**
-----

Redirect the bitlink to original url

GET /{bitlink}

**{bitlink} - 'link' field of response from previous request**
```
Hit the following url in the browser - http://localhost:5000/{bitlink}
```

OR
```
curl \
-H 'Content-Type: application/json' \
-X GET \
http://localhost:5000/{bitlink}
```


**Create a Bitlink**
-----

POST /v4/bitlinks 

Converts a long url to a Bitlink and sets additional parameters like 'title'.

**Request**
```
curl \
-H 'Content-Type: application/json' \
-X POST \
-d '{
  "long_url": "https://www.amazon.com",
  "domain": "clone_bit.ly",
  "title": "Amazon"
}' \
http://localhost:5000/v4/bitlinks
```

**Response**
```
{"created_at":"03/10/2021 19:05:08", "link":"clone_bit.ly/kmi517I", "long_url":"https://www.amazon.com", "title":"Amazon"}
```


**Retrieve a Bitlink**
-----

Returns information for the specified link.

GET /v4/bitlinks/{bitlink}

**Request**
```
curl \
-H 'Content-Type: application/json' \
-X GET \
http://localhost:5000/v4/bitlinks/{bitlink}
```

**Response**
```
{"created_at":"03/10/2021 19:05:08", "link":"clone_bit.ly/kmi517I", "long_url":"https://www.amazon.com", "title":"Amazon"}
```


**Update a Bitlink**
-----

Updates fields in the specified link.

PATCH /v4/bitlinks/{bitlink} 

**Request**
```
curl \
-H 'Content-Type: application/json' \
-X PATCH \
-d '{
  "long_url": "https://www.amazon.com",
  "title": "Amazon WebPage"
}' \
http://localhost:5000/v4/bitlinks/{bitlink}
```

**Response**
```
{"created_at":"03/10/2021 19:05:08", "link":"clone_bit.ly/kmi517I", "long_url":"https://www.amazon.com", "title":"Amazon WebPage"}
```


**Get Clicks for a Bitlink**
-----

Returns the click counts for the specified link.

GET /v4/bitlinks/{bitlink}/clicks

**Request** 
```
curl \
-H 'Content-Type: application/json' \
-X GET \
http://localhost:5000/v4/bitlinks/{bitlink}/clicks
```

**Response**
```
{"clicks":1, "created_at":"03/10/2021 19:05:08"}
```
