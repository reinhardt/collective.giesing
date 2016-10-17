from five import grok
from zope.interface import Interface

from Products.Five.browser.pagetemplatefile import ZopeTwoPageTemplateFile
from plone.app.layout.viewlets.interfaces import IPortalHeader
from plone.app.layout.viewlets.interfaces import IBelowContent

from Products.CMFCore.utils import getToolByName
from zc.relation.interfaces import ICatalog
from zope.app.intid.interfaces import IIntIds
from zope.component import getUtility

from collective.giesing.snippet import ISnippet
from collective.giesing.storyline import IStoryline
from collective.giesing.location import ILocation

grok.templatedir('templates')

class TimeLineViewlet(grok.Viewlet):
    grok.context(ISnippet)
    grok.name('collective.giesing.TimeLineViewlet')
    grok.require('zope2.View')
    grok.viewletmanager(IBelowContent)

    def getTimeLine(self):
        cat = getToolByName(self.context, 'portal_catalog')
        query = dict(object_provides='collective.giesing.snippet.ISnippet',
            timetag=dict(query=[self.context.timetag, ], range='min'),
            sort_on='timetag',)
        future = [x for x in cat(query)]
        query['timetag']['range'] = 'max'
        past = [x for x in cat(query)]
        timeline = past[-3:-1] + future[:3]
        return timeline

class LocatineTimeLineViewlet(grok.Viewlet):
    grok.context(ILocation)
    grok.name('collective.giesing.LocationTimeLineViewlet')
    grok.require('zope2.View')
    grok.viewletmanager(IBelowContent)
    grok.template('timelineviewlet')

    def getTimeLine(self):
        intids = getUtility(IIntIds)
        relcatalog = getUtility(ICatalog)

        snippets = [intids.getObject(rv.from_id) for rv in relcatalog.findRelations({'to_id': intids.getId(self.context)})]
        timeline = [dict(Title=obj.Title(), 
                         getURL=obj.absolute_url(), 
                         storyline=obj.aq_parent.Title(), 
                         timetag=obj.timetag) \
                    for obj in snippets]
        timeline.sort(key=lambda x: x['timetag'])
        return timeline

class LocationViewlet(grok.Viewlet):
    grok.context(ISnippet)
    grok.name('collective.giesing.LocationViewlet')
    grok.require('zope2.View')
    grok.viewletmanager(IBelowContent)

    def getSnippets(self):
        intids = getUtility(IIntIds)
        relcatalog = getUtility(ICatalog)

        snippets = [intids.getObject(rv.from_id)
                    for rv in relcatalog.findRelations(
                        {'to_id': self.context.locationtag.to_id})]
        timeline = [dict(Title=obj.Title(),
                         getURL=obj.absolute_url(),
                         storyline=obj.aq_parent.Title(),
                         timetag=obj.timetag)
                    for obj in snippets]
        timeline.sort(key=lambda x: x['timetag'])
        return timeline
