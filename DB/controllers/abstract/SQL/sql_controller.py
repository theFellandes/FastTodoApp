import sqlalchemy.ext.declarative

from functools import wraps
from sqlalchemy import and_, or_
from sqlalchemy.orm import sessionmaker
from sqlalchemy import select
from pydantic import BaseModel, Extra

from DB.connectors.abstract.SQL.sql_connector import SQLConnector


class SQLController(BaseModel):
    class Config:
        extra = Extra.forbid

    sql_connector: SQLConnector
    base: sqlalchemy.ext.declarative.declarative_base
    engine: sqlalchemy.engine = None
    Session: sqlalchemy.orm.sessionmaker = None
    session: Session = None

    def sql_base_exception(self, func):
        """ Catches any exceptions and rolls back the session """
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except Exception as e:
                print(e)
                self.session.rollback()

    @sql_base_exception
    def search_table(self, select_values: tuple, filter_values: tuple,
                     filter_by: str = 'and', number_of_results: int = -1):
        """
        Returns a list of results from a table based on a filter clause of and

        Arguments:
            select_values {tuple} -- The column to select from the table
            filter_values {tuple} -- The column to filter by
            filter_by {str} -- The filter clause to use (and/or) default is and
            number_of_results {int} -- The number of results to return, default is -1 which returns all

        Raises:
            Exception: If the filter_by is not and, or

        Returns:
            list -- A list of results from the table
        """
        if filter_by == 'and' or filter_by == '&' or filter_by == '&&':
            # SELECT select_column FROM table WHERE filter1 == value1 AND filter2 == value2
            results = self.session.execute(select(*select_values).filter(and_(*filter_values)))
        else:
            # SELECT select_column FROM table WHERE filter1 == value1 AND filter2 == value2
            results = self.session.execute(select(*select_values).filter(or_(*filter_values)))

        if number_of_results != -1:
            return results[:number_of_results]
        return results

    def add(self, entity: BaseModel):
        """ Adds an entity to the database """
        self.session.add(entity)
        self.session.commit()

    def add_many(self, list_of_items: list):
        """ Adds a list of items to the database """
        self.session.add_all(list_of_items)
        self.session.commit()
