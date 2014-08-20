from tornado.web import authenticated

from amgut.util import AG_DATA_ACCESS
from amgut.handlers.base_handlers import BaseHandler


class ResultsPortalHandler(BaseHandler):
    @authenticated
    def get(self):
        results = AG_DATA_ACCESS.get_barcode_results(self.current_user)
        self.render('results_portal.html', skid=self.current_user,
                    results=results)