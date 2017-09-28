from plone.app.contenttypes.browser.folder import FolderView
from Products.Five.browser import BrowserView


class GalleryView(FolderView, BrowserView):
    """
    Gallery view
    """


class GalleryModal(BrowserView):
    """
    Gallery modal helper method for slick carousel
    """

    contents = []
    itemIndex = -1

    def getContents(self):
        self.contents = self.context.listFolderContents(
                            contentFilter={"portal_type": "Image"}
                        )
        return self.contents

    def getIndex(self):
        self.itemIndex = [x.UID() for x in self.contents].index(
                            self.request.form['image']
                         )
        return self.itemIndex
