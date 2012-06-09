from five import grok
from zope import schema

from plone.directives import form, dexterity

from plone.app.textfield import RichText

from collective.giesing import GiesingMessageFactory as _

class ILocation(form.Schema):
    """ A location is a real or fictional place where a snippet can be set. A 
        guideline for the size of a location is "as far as the eye can see".
        Examples are a flat, a bar, a forest clearing etc.
    """

    title = schema.TextLine(
            title=_(u"Location Name"),
        )

    description = schema.Text(
            title=_(u"Description"),
            required=False,
        )

    coordinates = schema.Tuple(
            title=_("Coordinates"),
            required=False,
            min_length=2,
            max_length=2,
            value_type=schema.Float(title=_("Coordinate")),
        )
