from collective.googleanalytics.viewlets.tracking import AnalyticsTrackingViewlet

class AnalyticsViewlet(AnalyticsTrackingViewlet):
    """Override this one"""
    
    def getTrackingWebProperty(self):
        """
        Returns the Google web property ID for the selected tracking profile,
        or an empty string if no tracking profile is selected.
        """
        import pdb;pdb.set_trace()
        return getattr(self.analytics_tool, 'tracking_web_property', None)
