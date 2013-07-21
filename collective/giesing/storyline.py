from five import grok
from zope import schema

from plone.directives import form, dexterity
from Products.CMFCore.utils import getToolByName

from collective.giesing import GiesingMessageFactory as _
from collective.giesing.location import ILocation
from collective.giesing.interfaces import IGiesingLayer

grok.templatedir('templates')

class IStoryline(form.Schema):
    """ A storyline is a set of logically connected snippets """

    title = schema.TextLine(
            title=_(u"Title"),
        )
    
    description = schema.Text(
            title=_(u"Description"),
            required=False,
        )

class View(grok.View):
    """Present the contents of the storyline."""
    grok.context(IStoryline)
    grok.layer(IGiesingLayer)
    grok.require('zope2.View')
    grok.template('storyline_view')


class RSS(grok.View):
    """ A storyline specific RSS view """
    grok.context(IStoryline)
    grok.layer(IGiesingLayer)
    grok.template('storyline_rss')

    def update(self):
        catalog = getToolByName(self.context, 'portal_catalog')
        self.object_list = catalog(path='/'.join(self.context.getPhysicalPath()),
                                   portal_type='collective.giesing.snippet',
                                   sort_on='modified',
                                   sort_order='reverse',
                                   b_start=0,
                                   b_size=10,
                                   )
