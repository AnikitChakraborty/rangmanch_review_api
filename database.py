from sqlmodel import SQLModel, Session, create_engine

DATABASE_URL = "sqlite:///./rangmanch_review.db"

engine = create_engine(DATABASE_URL, echo=True)

def create_tables():
    """CREATE ALL TABLES DEFINED BY SQLModel CLASSES IN THE DATABASE."""
    SQLModel.metadata.create_all(engine)

def get_session(): 
    """GET A NEW DATABASE SESSION."""
    with Session(engine) as session:
        yield session
