from flask import Flask, request
import json
import requests
import os
from watson_developer_cloud import ConversationV1
from flask_mail import Mail, Message


app = Flask(__name__)

# This needs to be filled with the Page Access Token that will be provided
# by the Facebook App that will be created.
PAT = 'EAAbvzNAp0ZCABAEGZAA26nf7P5sdLYdLkW89JRr2jqpJGJBgkJck2rIoT8er9EQXqIC1YojXJ7XZBmx3OtB7SrtIFMMGs4BK1uq9KnUxptaoc2SZCnMV5ZBkiiZCD6R4nFv5MZApnJNcBfxUL8PjMjnVDe0sDZB40wx8mDCZCtnQvnAZDZD'
#context_glob=dict()

@app.route('/', methods=['GET'])
def handle_verification():
  print "Handling Verification."
  if request.args.get('hub.verify_token', ''
