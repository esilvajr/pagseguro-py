# -*- coding: latin -*-

from urllib.parse import urlencode
from urllib.request import Request, urlopen
from app.properties.resources import url_builder
import xml.etree.ElementTree as xml_parser

class session(object):
	"""docstring for Session"""
	def __init__(self):
		super(session, self).__init__()

	def create(self, credentials):
		request = Request(self.__url__(), urlencode(credentials).encode())
		response = urlopen(request).read().decode()
		xml = xml_parser.fromstring(response)
		return xml.find('id').text

	def __url__(self):
		builder = url_builder()
		return builder.build_session_url()