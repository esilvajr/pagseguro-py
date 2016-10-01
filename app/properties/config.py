class configuration(object):
    """ docstring environment """
    environment = "sandbox"
    """ docstring account credentials """
    email = "edison.junior@s2it.com.br"
    token_production = "your_production_token"
    token_sandbox = "256422BF9E66458CA3FE41189AD1C94A"
    """ docstring application credentials """
    app_id_production = "your_production_application_id"
    app_id_sandbox = "your_sandbox_application_id"
    app_key_production = "your_production_application_key"
    app_key_sandbox = "your_sandbox_application_key"
    """ docstring charset """
    charset = "UTF-8"
    """ docstring log """
    log_active = None
    log_location = ""

class environment(object):

    env = None

    """docstring for environment"""
    def __init__(self):
        super(environment, self).__init__()
        self.env = configuration.environment

    def get_environment(self):
        return self.env

    def set_environment(self, environment):
        self.env = environment
        

class account_credentials(object):
    
    email = None
    token = None

    """docstring for Configure"""
    def __init__(self):
        self.email = configuration.email
        self.token = configuration.token_production if environment.get_environment == "sandbox" else configuration.token_sandbox

    """Get credentials"""
    def get_credentials(self):
        return {
            'email' : self.email,
            'token' : self.token
        }

    """Set credentials"""
    def set_credentials(self, email, token):
        self.email = email
        self.token = token

    """Get token"""
    def get_token(self):
        return self.token

    """Set token""" 
    def set_token(self, token):
        self.token = token

    """Get e-mail"""
    def get_email(self):
        return self.email 

    """Set e-mail"""
    def set_email(self, email):
        self.email = email

class configure(object):

    """docstring for Configure"""
    def __init__(self):
        super(configure, self).__init__()

    """Get account credentials"""
    def get_account_credentials(self):
        account = account_credentials()
        return account.get_credentials()

    def set_account_credential(self, email, token):
        account_credentials(email, token)

    """Get environment"""
    def get_credentials(self):
        environment = environment()
        return environment.get_environment()

    def set_credentials(self, environment):
        environment(environment)

        