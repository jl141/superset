from typing import Any

from flask_babel import lazy_gettext as _
from sqlalchemy import and_, or_
from sqlalchemy.orm import aliased
from sqlalchemy.orm.query import Query

from superset.utils.core import get_user_id
from superset.utils.filters import get_dataset_access_filters
from superset.views.base import BaseFilter

class NotDeletedUserFilter(BaseFilter):
    #Filter out deleted users when getting all users
    name = "Filter non-deleted users"

    def apply(self, query, value):
        return query.filter(self.model.deleted.is_(False))
