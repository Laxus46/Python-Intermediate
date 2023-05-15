from sqlalchemy import create_engine

engine = create_engine('postgresql+psycopg2://postgres:postgres@host.docker.internal/postgres')

connection=engine.connect()