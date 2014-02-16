import subprocess
from flask import render_template, flash, redirect
from app import app, http_auth
from download_form import DownloadForm
from streaming_form import StreamingForm
from functools import wraps
from flask import request, Response

# index view function suppressed for brevity

@app.route('/download', methods = ['GET', 'POST'])
#@http_auth.requires_auth
def download():
    form = DownloadForm()
    if form.validate_on_submit():
	if form.download_mode.data=='uploaded':
		subprocess.Popen(["plowdown","-a","USERNAME:PASSWORD",form.url.data])
		flash('Download using Uploaded account requested for URL="' + form.url.data + '"')
	elif form.download_mode.data=='wget':
		subprocess.Popen(["wget",form.url.data])
		flash('Download using wget requested for URL="' + form.url.data + '"')
    return render_template('download.html',
        form = form)

@app.route('/stream', methods = ['GET', 'POST'])
def stream():
    form = StreamingForm()
    if form.validate_on_submit():
	   subprocess.Popen(["killall","livestreamer"])
           subprocess.Popen(["livestreamer",form.url.data,"best","--player","mplayer"])
           flash('Streaming URL="' + form.url.data + '"')
    return render_template('streaming.html',
        form = form)


