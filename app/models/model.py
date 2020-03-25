from datetime import datetime
from weakref import WeakValueDictionary
from sqlalchemy import inspect
from sqlalchemy.orm import aliased

from app import db


class MetaModel(db.Model.__class__):
    def __init__(self, *args):
        super().__init__(*args)
        self.aliases = WeakValueDictionary()

    def __getitem__(self, item):
        try:
            alias = self.aliases[item]
        except KeyError:
            alias = aliased(self)
            self.aliases[item] = alias

        return alias


class Model:
    exclude_print = ()
    exclude_to_json = ()

    def __repr__(self):
        """ Print Models, print_filter models will be excluded """
        return "%s(%s)" % (
            self.__class__.__name__,
            {
                column: value
                for column, value in self._to_dict().items()
                if column not in self.exclude_print
            },
        )

    @property
    def json(self):
        """ Jsonify Models, to_json_filter models will be excluded. """
        return {
            column: value
            if not isinstance(value, datetime)
            else value.strftime("%Y-%m-%d")
            for column, value in self._to_dict().items()
            if column not in self.exclude_to_json
        }

    def _to_dict(self):
        """ Allow to_json to be overwritten without impacting __repr__ (or vise versa)
                and adding the filter lists """
        return {
            column.key: getattr(self, column.key)
            for column in inspect(self.__class__).attrs
        }

    def save(self):
        db.session.add(self)
        db.session.commit()
        return self

    def delete(self):
        db.session.delete(self)
        db.session.commit()
