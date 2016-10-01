from app.properties.config import environment

class url_builder(object):
	
	protocol = "https://";
	base = "pagseguro.uol.com.br"
	webservice = "ws"
	static = "stc"
	session = "/v2/sessions";

	def __init__(self):
		super(url_builder, self).__init__()

	def build_base_url(self):	
		if self.__in_sandbox__() is True:
			return '{0}sandbox.{1}'.format(self.protocol, self.base)
		return '{0}{1}'.format(self.protocol, self.base)
		
	def build_ws_url(self):
		if self.__in_sandbox__() is True:
			return '{0}{1}.sandbox.{2}'.format(self.protocol, self.webservice, self.base)
		return '{0}{1}.{2}'.format(self.protocol, self.webservice, self.base)

	def build_static_url(self):
		if self.__in_sandbox__() is True:
			return '{0}{1}.sandbox.{2}'.format(self.protocol, self.static, self.base)
		return '{0}{1}.{2}'.format(self.protocol, self.static, self.base)

	def build_session_url(self):
		return '{0}{1}'.format(self.build_ws_url(), self.session)

	def __in_sandbox__(self):
		env = environment()
		if env.get_environment() == "sandbox":
			return True
		return False