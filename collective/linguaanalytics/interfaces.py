from zope import interface
from collective.googleanalytics.interfaces.browserlayer import IAnalyticsLayer

class ILayer(interface.Interface, IAnalyticsLayer):
    """Marker interface that defines a Zope 3 browser layer."""
