"""Simple service on flask. Convert xml to json."""
from flask import Flask, jsonify, request
from xmljson import badgerfish as bf
from xml.etree.ElementTree import fromstring

helloResponse = "You can convert XML->JSON. Post to /postxml"

app = Flask(__name__)

def convert(xmlfile):
	"""
	convert(xmlfile)
	Makes input xml, convert it and return json
	"""
	tree = fromstring(xmlfile)
	jsonfile = jsonify(bf.data(tree))
	return jsonfile

@app.route('/')
def hello():
	"""
	hello()
	Return string with info about service homepage.
	"""
	return helloResponse

@app.route('/postxml', methods=['POST'])
def postxml():
	"""
	postxml()
	Receive xml and response with json
	"""
	xmlfile = request.get_data(as_text=True)
	resp = convert(xmlfile)
	return resp

if __name__ == '__main__':
	"""Start service if that module is the main program"""
	app.run(debug=False, host='0.0.0.0', port=80)
