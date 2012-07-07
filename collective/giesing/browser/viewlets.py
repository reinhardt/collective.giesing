from five import grok
from Products.Five.browser.pagetemplatefile import ZopeTwoPageTemplateFile
from plone.app.layout.viewlets.interfaces import IPortalHeader
from zope.interface import Interface
from plone.app.layout.viewlets.interfaces import IBelowContent
from Products.CMFCore.utils import getToolByName

from collective.giesing.snippet import ISnippet
from collective.giesing.storyline import IStoryline

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

