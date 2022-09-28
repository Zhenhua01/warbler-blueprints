from flask import Blueprint

from models import Follows

# Note that the capitalized Site and the lowercase site
# are two completely separate variables. Site is a model
# and site is a blueprint.

follows = Blueprint('follows', __name__)

@follows.url_value_preprocessor
def get_site(endpoint, values):
    query = Follows.query.filter_by(subdomain=values.pop('site_subdomain'))
    g.site = query.first_or_404()

# Import the views after site has been defined. The views
# module will need to import 'site' so we need to make
# sure that we import views after site has been defined.
from . import views