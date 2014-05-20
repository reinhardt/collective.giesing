from zc.relation.interfaces import ICatalog
from zope.component import getUtility
from z3c.relationfield.event import updateRelations
from z3c.relationfield.interfaces import IHasRelations

from Products.CMFCore.utils import getToolByName


def reindex_relations(context):
    rcatalog = getUtility(ICatalog)
    # Clear the relation catalog to fix issues with interfaces that don't exist
    #  anymore.
    rcatalog.clear()

    catalog = getToolByName(context, 'portal_catalog')
    brains = catalog.searchResults(
        object_provides=IHasRelations.__identifier__)
    for brain in brains:
        obj = brain.getObject()
        updateRelations(obj, None)
