from flask import Flask, request
from flask_limiter import Limiter
from flask_limiter.util import get_ipaddr
from flask_cors import CORS, cross_origin
from jinja2 import Template
import json
import random
import os

api_url = os.getenv("SAAS_API_URL")
if api_url == None:
    api_url = "https://saas.woohoojin.dev"

app = Flask(__name__)
CORS(app, support_credentials=True)

limiter = Limiter(
    app,
    key_func=lambda: request.headers.get("X-Real-Ip"),
)


@app.route("/build", methods=["GET"])
@limiter.limit("100 per day")
@cross_origin(support_credentials=True)
def service():
    return (
        parse_templated_file("return/build.yml.j2"),
        200,
    )


@app.route("/service", methods=["GET"])
@limiter.limit("100 per day")
@cross_origin(support_credentials=True)
def service():
    return (
        parse_templated_file("return/application.py.j2"),
        200,
    )


@app.route("/license/<service_name>", methods=["GET"])
@limiter.limit("100 per day")
@cross_origin(support_credentials=True)
def license(service_name):
    if " " in service_name:
        return "Bad request", 400
    return (
        parse_templated_file("return/license.j2", service_name=service_name.title()),
        200,
    )


@app.route("/requirements", methods=["GET"])
@limiter.limit("100 per day")
@cross_origin(support_credentials=True)
def requirements():
    return (
        parse_templated_file("return/requirements.j2"),
        200,
    )


@app.route("/readme/<service_name>", methods=["GET"])
@limiter.limit("100 per day")
@cross_origin(support_credentials=True)
def readme(service_name):
    if " " in service_name:
        return "Bad request", 400
    return (
        parse_templated_file("return/readme.j2", service_name=service_name.title()),
        200,
    )


@app.route("/dockerfile/<service_name>", methods=["GET"])
@limiter.limit("100 per day")
@cross_origin(support_credentials=True)
def dockerfile(service_name):
    if " " in service_name:
        return "Bad request", 400
    return (
        parse_templated_file("return/dockerfile.j2", service_name=service_name),
        200,
    )


@app.route("/create/<service_name>", methods=["GET"])
@limiter.limit("100 per day")
@cross_origin(support_credentials=True)
def create_service(service_name):
    if " " in service_name:
        return "Bad request", 400
    return (
        parse_templated_file(
            "return/install.sh.j2", service_name=service_name, api_url=api_url
        ),
        200,
    )


def parse_templated_file(file_path, **kwargs):
    with open(file_path, "r") as template_file:
        template = Template(template_file.read())
        return template.render(**kwargs)


if __name__ == "__main__":
    app.run(debug=False, host="0.0.0.0")
