from zope import component

from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from plone.registry.interfaces import IRegistry

from collective.googleanalytics.viewlets import tracking
from collective.linguaanalytics import interfaces

class AnalyticsTrackingViewlet(tracking.AnalyticsTrackingViewlet):
    """Override this one"""

    def __init__(self, context, request, view, manager):
        super(AnalyticsTrackingViewlet, self).__init__(context,request,view,
                                                       manager)
        self._settings = None
        self._code = None
        self._navigation_root_url = None

    def getTrackingWebProperty(self):
        """
        Returns the Google web property ID for the selected tracking profile,
        or an empty string if no tracking profile is selected.
        """
        if self._code is None:
            mapping = self.mapping
            url = self.navigation_root_url()
            self.code = mapping.get(url)
        return self.code

    def available(self):
        """
        Checks to see whether the viewlet should be rendered based on the role
        of the user and the selections for excluded roles in the configlet.
        """
        if not self.settings:
            return False

        return self.settings.activated and self.getTrackingWebProperty()

    @property
    def settings(self):
        if not self._settings:
            registry = component.getUtility(IRegistry)
            self._settings = registry.forInterface(interfaces.ISettingsSchema,
                                                   check=False)
        return self._settings

    def navigation_root_url(self):

        if not self._navigation_root_url:
            portal_state = component.getMultiAdapter((self.context,
                                                      self.request),
                                                     name="plone_portal_state")
            self._navigation_root_url = portal_state.navigation_root_url()

        return self._navigation_root_url

    @property
    def mapping(self):
        mapping = {}
        url_codes = self.settings.mapping
        for url_code in url_codes:
            url, code = url_code.split('|')
            mapping[url] = code
        return mapping
