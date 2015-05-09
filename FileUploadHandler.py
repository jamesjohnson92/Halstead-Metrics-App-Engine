from google.appengine.ext.webapp import blobstore_handlers
from gaesessions import get_current_session


class FileUploadHandler(blobstore_handlers.BlobstoreUploadHandler):
    def post(self):
        uploads = self.get_uploads()[0]
        session = get_current_session()
        session['key'] = uploads.key()
        self.redirect('/view')


