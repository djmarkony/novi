from __future__ import print_function
from flask import Flask, render_template, request
from flaskext.mysql import MySQL


import tagdb as tagdb
import boto3
import os, stat

from apiclient.discovery import build
from apiclient.errors import HttpError
from oauth2client.tools import argparser

import unicodedata
import json
import config
import codecs

app = Flask(__name__)

# mysql connection
app.config['MYSQL_DATABASE_HOST'] = config.MYSQL_DATABASE_HOST
app.config['MYSQL_DATABASE_USER'] = config.MYSQL_DATABASE_USER
app.config['MYSQL_DATABASE_PASSWORD'] = config.MYSQL_DATABASE_PASSWORD
app.config['MYSQL_DATABASE_DB'] = config.MYSQL_DATABASE_DB
app.config['MYSQL_CHARSET'] = 'utf8'
mysql = MySQL(app)

import searcher as searcher

@app.route('/test')
def test():
    return 'test'

# @app.route('/fetchVideos/<category>/<subcategory>/<number_of_videos>')
# def fetchVideos(category,subcategory,number_of_videos):
#     q = tagdb.getRandomTag(category, subcategory).lower()
#     out_string = searcher.youtube_search(q, max_results, category)
#
#     return ""

@app.route('/showVideos')
def showVideos():
    categories = searcher.get_all_categories()
    data = searcher.get_videos()
    return render_template('index.html', categories=categories, data=data)

@app.route('/approvedVideos')
def approvedVideos():
    categories = searcher.get_all_categories()
    data = searcher.get_approved_videos()
    return render_template('approvedVideos.html', categories=categories, data=data)

@app.route('/getApprovedVideosByCategory/<id>', methods=['POST'])
def getApprovedVideosByCategory(id):
    videos = searcher.get_approved_videos_by_category(id)
    return render_template('approved_table_video.html', data=videos)

@app.route('/getVideosByCategory/<id>', methods=['POST'])
def getVideosByCategory(id):
    videos = searcher.get_videos_by_category(id)
    return render_template('table_video.html', data=videos)

@app.route('/approveVideo', methods=['POST'])
def approveVideo():
    ids = request.form['data']
    ids = json.loads(ids)
    print (ids)
    videos = searcher.approveVideos(ids)
    return render_template('table_video.html', data=videos)
if __name__ == '__main__':
    # handler()
    app.run()



# def lambda_handler(event, context):
#     handler(event,context)
