from sqlalchemy.orm import Session
from ..connectors.database import DBSession


class DataBase:
    def __init__(self) -> None:
        self.session: Session = DBSession()

    def batch_insert(self, model, records) -> None:
        try:
            model_instances = [model(**record) for record in records]
            self.session.bulk_save_objects(objects=model_instances)
        except Exception as error:
            print(f"Error when inserting batch into bank:{str(error)}")
            self.session.rollback()
        else:
            self.session.commit()
        finally:
            self.session.close()
