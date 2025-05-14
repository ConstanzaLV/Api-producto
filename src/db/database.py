from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


# URL_DATABASE = 'postgresql://postgres:1234@127.0.0.1:5432/ferremas'
URL_DATABASE = 'postgresql://postgres.zdvremazneekzlxokyjd:teStKiioL8RqcsCk@aws-0-sa-east-1.pooler.supabase.com:6543/postgres'

engine = create_engine(URL_DATABASE)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


Base = declarative_base()
