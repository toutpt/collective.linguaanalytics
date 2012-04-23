from Products.Five.browser import BrowserView
from plone.browserlayer import utils

class LayersView(BrowserView):
    """View all existing layers"""
    
    def layers(self):
        layers = utils.registered_layers()
        import pdb;pdb.set_trace()
        return [layer.__identifier__ for layer in layers]