# pylint: disable=E1101

from src.infra.config import DBConnectionHandler
from src.infra.entities import Users


class FakerRepo:
    """A simple repo"""

    @classmethod
    def insert_user(cls):
        """insert user"""

        with DBConnectionHandler() as db_connection:
            try:
                new_user = Users(name="DAN", password="teste123")
                db_connection.session.add(new_user)
                db_connection.session.commit()
            except:
                db_connection.session.rollback()
                raise
            finally:
                db_connection.session.close()
