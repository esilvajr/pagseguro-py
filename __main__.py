# -*- coding: latin -*-

from app.properties.config import configure
from app.services.session import session

""" how to use """
configure = configure()
session = session()
result  = session.create(configure.get_account_credentials())
print(result)