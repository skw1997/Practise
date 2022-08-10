from sqlalchemy import create_engine, func, distinct
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, LargeBinary, DateTime, Integer, BigInteger, Boolean, UniqueConstraint, DECIMAL, \
    ARRAY, ForeignKey, DATE, Sequence, Float
from datetime import datetime
import os
Base = declarative_base()
def generate_datetime():
    return datetime.utcnow()
class App(Base):
    __tablename__ = 'fc_app'

    id = Column(String(255), primary_key=True, nullable=False)
    user_id = Column(String, nullable=False)
    app_name = Column(String(255), nullable=False)
    app_version = Column(Integer, nullable=False)
    rafiki_app_name = Column(String(255), nullable=False)
    rafiki_app_version = Column(Integer, nullable=False)
    ai_user_id = Column(String(255), nullable=False)
    project_id = Column(Integer, nullable=True)
    folder_id = Column(BigInteger, nullable=True)
    train_job_id = Column(String(255), nullable=True)
    predictor_host = Column(String(255), nullable=False)
    app_type = Column(Integer, nullable=False)
    create_date = Column(DateTime, nullable=False, default=generate_datetime)
    modify_date = Column(DateTime, nullable=False, default=generate_datetime)
    status = Column(Integer, nullable=False, default=1)
    description = Column(String(2500), nullable=False, default='')
    operator = Column(String(255), nullable=False)
    __table_args__ = (UniqueConstraint('app_name', 'app_version', 'train_job_id'),)

class DbStore():
    def __init__(self):
        host = '192.168.100.202'
        port = '5433'
        user = 'singa_auto'
        database = 'singa_auto'
        password = 'singa_auto'

        db_connection_url = self._make_connection_url(
            host=host,
            port=port,
            database=database,
            user=user,
            password=password
        )

        self._engine = create_engine(db_connection_url)
        self._sessionmaker = sessionmaker(bind=self._engine)
        self._session = None

    def get_train_job_user_id(self, train_job_id):
        sql = '''
            SELECT
                train_job.user_id AS ai_user_id
            FROM
                train_job
            WHERE
                 train_job.id = '{}' 
        '''.format(train_job_id)
        result = self._session.execute(sql)
        if result.rowcount > 0:
            return [dict(row) for row in result][0]
        return []

    def get_train_job_can_test(self, train_job_id):
        sql = '''
            SELECT
                grants.user_id,
                grants.folder_id,
                grants.is_can_test_app
            FROM
                fc_trainjob_dataset_folder_grant_bind  bind
                LEFT JOIN fc_dataset_folder_grant grants on  bind.grant_id = grants.grant_id
            WHERE
                 bind.trainjob_id = '{}' and bind.folder_id = grants.folder_id 
        '''.format(train_job_id)
        result = self._session.execute(sql)
        if result.rowcount > 0:
            return [dict(row) for row in result][0]
        return []

    def get_dataset_folder_test_app(self, app_name, app_version, app_id, ai_user_id, status, type):
        app = self._session.query(App)\
            .filter(App.app_name == app_name,
                    App.app_version == app_version,
                    App.id == app_id,
                    App.ai_user_id == ai_user_id,
                    App.status == status,
                    App.app_type == type).first()
        return app

    def get_train_job_app_list(self, train_job_id):
        list = self._session.query(App).filter(App.train_job_id == train_job_id).all()
        return list

    def _make_connection_url(self, host, port, database, user, password):
        return 'postgresql://{}:{}@{}:{}/{}'.format(
            user, password, host, port, database
        )
    def __enter__(self):
        self.connect()

    def connect(self):
        self._session = self._sessionmaker()

    def __exit__(self, exception_type, exception_value, traceback):
        self.disconnect()

    def disconnect(self):
        if self._session is not None:
            self._session.commit()
            self._session.close()
            self._session = None

if __name__ == '__main__':
    db = DbStore()
    with db:
        result = db.get_dataset_folder_test_app(app_name='ai-test_app', app_version=1, app_id="f59b4f80-a100-41f4-87d9-b6b11a1e786a", ai_user_id='c5d6f021-9dcc-4d82-a022-92d54cf435f2', status=1, type=1)
        print(not result)