from collective.googleanalytics.viewlets.tracking import AnalyticsTrackingViewlet
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile

class AnalyticsViewlet(AnalyticsTrackingViewlet):
    """Override this one"""

    render = ViewPageTemplateFile('tracking.pt')

    def getTrackingWebProperty(self):
        """
        Returns the Google web property ID for the selected tracking profile,
        or an empty string if no tracking profile is selected.
        """
        return "UA-XXXXX-Y"

    def available(self):
        """
        Checks to see whether the viewlet should be rendered based on the role
        of the user and the selections for excluded roles in the configlet.
        """
        return True

