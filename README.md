![](service_as_a_service_logo.png)

# SAAS (Service as a Service)

Have you ever wanted a simple REST API that enabled you to easily scaffold up your next simple REST API?

Look no further.

Service as a Service (SAAS) provides users with an easy, robust, reliable, and atomic REST API for all of your easy, robust, reliable, and atomic REST API needs. If your requirements for creating a service fall under the following:

1. You wish to create a simple REST API
2. You wish to avoid the hassle of scaffolding a simple REST API
3. **You're willing to pipe a curl directly into bash**

Then you are welcome to use SAAS for your simple REST API needs!

SAAS can be reached at https://saas.woohoojin.dev/

# Table of Contents

1. [Usage](#usage-example)
1. [API Documentation](#api-documentation)
   1. [Create Service](#create)
   1. [Get Boilerplate Code](#service)
   1. [Get License](#license)
   1. [Get Readme](#readme)
   1. [Get Dockerfile](#dockerfile)
   1. [Get Requirements](#requirements)

# Usage Example

```sh
curl -s https://saas.woohoojin.dev/create/my_service | sh
```

# API Documentation

## Create

**URL** : `/create/<service_name>`

**Method** : `GET`

**Auth required** : NO

**Permissions required** : None

**Rate limit** : 100 requests per day

**Description** : Returns a creation script for the given service name.

## Success Response

**Code** : `200 OK`

**Content examples**

For a request with `service_name = sample`

```bash
echo "[+] Creating service directory..."
mkdir -p sample

echo "[+] Entering service directory..."
cd sample

echo "[+] Creating service code..."
curl https://saas.woohoojin.dev/service > sample.py

echo "[+] Creating license file..."
curl https://saas.woohoojin.dev/license/sample > LICENSE

echo "[+] Creating requirements..."
curl https://saas.woohoojin.dev/requirements > requirements.txt

echo "[+] Creating readme..."
curl https://saas.woohoojin.dev/readme/sample > README.md

echo "[+] Creating dockerfile..."
curl https://saas.woohoojin.dev/dockerfile/sample > Dockerfile
touch .gitignore

echo "\033[0;32m[+] All done! Enjoy your Service!"
```

## Failure Responses

**Code** : `400 Bad Request`

**Content examples**

For a request with `service_name = Bob's Burgers` (service_name contains a space)

```json
Bad request
```

## Service

**URL** : `/service`

**Method** : `GET`

**Auth required** : NO

**Permissions required** : None

**Rate limit** : 100 requests per day

**Description** : Returns the boilerplate simple REST API python code.

## Success Response

**Code** : `200 OK`

**Content examples**

```python
from flask import Flask, request
from flask_limiter import Limiter
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app, support_credentials=True)

limiter = Limiter(
    app,
    key_func=lambda: request.headers.get("X-Real-Ip"),
)


@app.route("/sample", methods=["GET"])
@cross_origin(support_credentials=True)
@limiter.limit("1 per day")
def sample():
    return "Hello World!", 200


if __name__ == "__main__":
    app.run(debug=False, host="0.0.0.0")
```

## License

**URL** : `/license/<service_name>`

**Method** : `GET`

**Auth required** : NO

**Permissions required** : None

**Rate limit** : 100 requests per day

**Description** : Generates a license (MIT) for the given service name.

## Success Response

**Code** : `200 OK`

**Content examples**

For a request with `service_name = sample`

```text
MIT License

Copyright (c) 2020 sample

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

## Failure Responses

**Code** : `400 Bad Request`

**Content examples**

For a request with `service_name = Bob's Burgers` (service_name contains a space)

```json
Bad request
```

## README

**URL** : `/readme/<service_name>`

**Method** : `GET`

**Auth required** : NO

**Permissions required** : None

**Rate limit** : 100 requests per day

**Description** : Generates a readme (md) for the given service name.

## Success Response

**Code** : `200 OK`

**Content examples**

For a request with `service_name = sample`

```md
# Sample

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Proin sit amet risus ex. Sed tempor vitae lacus nec pretium. Integer at auctor justo. Suspendisse posuere nibh velit, vitae euismod lectus euismod vitae. Mauris orci tortor, tempor ac dui vel, malesuada mollis eros. Quisque tempus malesuada aliquet.

1. Integer scelerisque libero eu nibh tincidunt pellentesque.
2. Sed faucibus, mi vitae venenatis aliquam, nunc ex vulputate odio, maximus bibendum lorem justo ut odio.
3. Sed vitae justo malesuada, vehicula tortor non, ullamcorper nibh.

# Table of Contents

1. [Usage](#usage-example)
2. [API Documentation](#api-documentation)

# Usage Example

\`\`\`python
def todo():
return "Implement me"
\`\`\`

# API Documentation

**URL** : `/sample`

**Method** : `GET`

**Auth required** : NO

**Permissions required** : None

**Rate limit** : 1 request per day

**Description** : Returns the string "Hello World!".

## Success Response

**Code** : `200 OK`

**Content examples**

\`\`\`json
Hello World!
\`\`\`

**Code** : `429 Too Many Requests`

**Content examples**

For a request made less than 24 hours before the previous request

\`\`\`json
Too Many Requests
1 per 1 day
\`\`\`
```

## Failure Responses

**Code** : `400 Bad Request`

**Content examples**

For a request with `service_name = Bob's Burgers` (service_name contains a space)

```json
Bad request
```

## Dockerfile

**URL** : `/dockerfile/<service_name>`

**Method** : `GET`

**Auth required** : NO

**Permissions required** : None

**Rate limit** : 100 requests per day

**Description** : Generates a dockerfile for the given service name.

## Success Response

**Code** : `200 OK`

**Content examples**

For a request with `service_name = sample`

```dockerfile
FROM python:3
ADD sample.py /
ADD requirements.txt /

RUN pip install -r requirements.txt

ENTRYPOINT [ "python3", "sample.py" ]
```

## Failure Responses

**Code** : `400 Bad Request`

**Content examples**

For a request with `service_name = Bob's Burgers` (service_name contains a space)

```json
Bad request
```

## Requirements

**URL** : `/requirements`

**Method** : `GET`

**Auth required** : NO

**Permissions required** : None

**Rate limit** : 100 requests per day

**Description** : Returns the boilerplate simple REST API `requirements.txt` file.

## Success Response

**Code** : `200 OK`

**Content examples**

```text
flask
flask_cors
flask_limiter
```
