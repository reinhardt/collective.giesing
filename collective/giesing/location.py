from five import grok
from zope import schema
from zope.interface import Interface

from plone.directives import form, dexterity

from plone.app.textfield import RichText

from collective.giesing import GiesingMessageFactory as _

from collective.geo.behaviour.behaviour import ICoordinates
from collective.geo.mapwidget.interfaces import (
    IMapLayer,
    IMapWidget as IMapWidget_geo,
)
from collective.geo.mapwidget.maplayers import MapLayer
from collective.z3cform.mapwidget.widget import IMapWidget
from collective.z3cform.mapwidget.maplayers import ShapeMapDisplayWidget

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

    text = RichText(
            title=_(u"Text"),
            required=False,
        )


class LocationShapeMapDisplayWidget(grok.MultiAdapter, ShapeMapDisplayWidget):
    grok.adapts(IMapWidget, Interface, ILocation)
    grok.provides(IMapWidget_geo)
    grok.implements(IMapWidget_geo)
    grok.name('geoshapedisplaymap')

    _layers = ['shapedisplay', 'all_locations']


class AllLocations(grok.MultiAdapter, MapLayer):
    grok.adapts(Interface, Interface, ILocation, Interface)
    grok.provides(IMapLayer)
    grok.implements(IMapLayer)
    grok.name('all_locations')

    @property
    def jsfactory(self):
        coords = []
        for obj in self.context.aq_parent.objectValues():
            if not obj == self.context \
               and obj.portal_type == 'collective.giesing.location':
                c = ICoordinates(obj).coordinates
                if c:
                    coords.append(c)
        if len(coords) == 0:
            return ""
        return """
    function() { return (function(cgmap) {
        cg_default_options = cgmap.createDefaultOptions();
        var wkt = new OpenLayers.Format.WKT({
            internalProjection: cg_default_options.projection,
            externalProjection: cg_default_options.displayProjection
        });
        var features = wkt.read('GEOMETRYCOLLECTION(%(coords)s)') || [];
        wkt.destroy();
        if(features.constructor != Array) {
            features = [features];
        }
        var layer = new OpenLayers.Layer.Vector('All Locations');
        layer.addFeatures(features);
        return layer;
    })(cgmap);
    }
""" % { 'coords': ','.join(coords)}

