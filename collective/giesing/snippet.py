from five import grok
from zope import schema

from plone.directives import form, dexterity

from plone.app.textfield import RichText
from z3c.relationfield.schema import RelationChoice
from plone.formwidget.contenttree import ObjPathSourceBinder
from plone.indexer.decorator import indexer

from collective.giesing import GiesingMessageFactory as _
from collective.giesing.location import ILocation

class ISnippet(form.Schema):
    """ A snippet is a short (a few paragraphs) prose text, usually part of a storyline
    """

    title = schema.TextLine(
            title=_(u"Title"),
        )
    
    description = schema.Text(
            title=_(u"Description"),
            required=False,
        )

    text = RichText(
            title=_(u"Text"),
            required=False,
        )

    timetag = schema.Datetime(
            title=_(u"Timetag"),
            description=_("The approximate time at which the events that this "
                          "snippet describes take place"),
            required=False,
        )

    locationtag = RelationChoice(
            title=_(u"Locationtag"),
            source=ObjPathSourceBinder(object_provides=ILocation.__identifier__),
            required=False,
        )

@indexer(ISnippet)
def storyline(obj):
    return obj.aq_parent.Title()
