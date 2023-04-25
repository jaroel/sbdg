"""Definition of the Bandlid content type
"""

from zope.interface import implements

from Products.Archetypes import atapi
from Products.ATContentTypes.content import schemata
#from Products.ATContentTypes.content.document import ATDocument
from collective.folderishpage.content.folderishdocument import \
                                                            ATFolderishDocument

from deliverance.contenttypes.interfaces import IBandlid
from deliverance.contenttypes.config import PROJECTNAME

BandlidSchema = ATFolderishDocument.schema.copy() + atapi.Schema((

    # -*- Your Archetypes field definitions here ... -*-
    atapi.ImageField('foto',
        original_size=(800, 800),
        sizes={
            'mini': (80, 80),
            'normal': (240, 800),
            'big': (300, 800),
            'maxi': (500, 800),
        },
        required=True,
        searchable=False,
        storage=atapi.AttributeStorage(),
        max_size=(800, 800),
        widget=atapi.ImageWidget(
            label='Foto bandlid',
            description='',
            show_content_type=False,),
        validators=(),
   ),

    atapi.ImageField('fotoklein',
        original_size=(800, 800),
        sizes={'bandleden': (800, 152)},
        required=True,
        searchable=False,
        storage=atapi.AttributeStorage(),
        max_size=(800, 800),
        widget=atapi.ImageWidget(
            label='Foto bandlid bandledenoverzicht',
            description='',
            show_content_type=False,),
        validators=(),
   ),

))

# Set storage on fields copied from ATContentTypeSchema, making sure
# they work well with the python bridge properties.

BandlidSchema['title'].storage = atapi.AnnotationStorage()
BandlidSchema['description'].storage = atapi.AnnotationStorage()

schemata.finalizeATCTSchema(BandlidSchema, moveDiscussion=False)


class Bandlid(ATFolderishDocument):
    """Deliverance bandlid"""
    implements(IBandlid)

    meta_type = "Bandlid"
    schema = BandlidSchema

    title = atapi.ATFieldProperty('title')
    description = atapi.ATFieldProperty('description')

    # -*- Your ATSchema to Python Property Bridges Here ... -*-

atapi.registerType(Bandlid, PROJECTNAME)
