from zope import schema
from zope.interface import Interface

from zope.app.container.constraints import contains
from zope.app.container.constraints import containers

from deliverance.contenttypes import contenttypesMessageFactory as _

class IBandlid(Interface):
    """Deliverance bandlid"""
    
    # -*- schema definition goes here -*-
