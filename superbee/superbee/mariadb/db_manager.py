import os

from dotenv import load_dotenv
from sqlalchemy import Column, Integer, String, Text, create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

Base = declarative_base()

class CareerlyPosts(Base):
    __tablename__ = 'careerly_posts'

    id = Column(Integer, primary_key=True)
    author = Column(String)
    workplace = Column(String)
    title = Column(String)
    text = Column(Text)
    url = Column(String)

load_dotenv(os.path.join(os.path.dirname(os.path.dirname(__file__)), '.env.development'))
engine = create_engine(f'mysql+pymysql://{os.getenv("MARIADB_USER_ID")}:{os.getenv("MARIADB_USER_PASSWORD")}@{os.getenv("MARIADB_DB_IP")}/{os.getenv("MARIADB_DB_NAME")}')
Session = sessionmaker(bind=engine)
