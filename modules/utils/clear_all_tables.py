from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker
from ..connectors.database import engine, DBSession

def clear_all_tables():
    metadata = MetaData(bind=engine)
    metadata.reflect(bind=engine)
    session = DBSession()
    for table in reversed(metadata.sorted_tables):
        try:
            print(f"Clearing table {table.name}")
            session.execute(table.delete())
            session.commit()
        except Exception as error:
            print(f"Error on clear table {table.name}: {str(error)}")
            session.rollback()
    session.close()
