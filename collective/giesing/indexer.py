from plone.indexer import indexer
from plone.dexterity.interfaces import IDexterityContent
from plone.uuid.interfaces import IUUID


@indexer(IDexterityContent)
def UID(obj):
    return IUUID(obj)
