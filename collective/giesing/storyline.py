from five import grok
from zope import schema

from plone.directives import form, dexterity

from collective.giesing import GiesingMessageFactory as _
from collective.giesing.location import ILocation

class IStoryline(form.Schema):
    """ A storyline is a set of logically connected snippets """

    title = schema.TextLine(
            title=_(u"Title"),
        )
    
    description = schema.Text(
            title=_(u"Description"),
            required=False,
        )

