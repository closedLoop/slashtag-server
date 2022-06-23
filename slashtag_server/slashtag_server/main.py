from fastapi import Depends, FastAPI

from . import __version__
from .app import crud, models
from .app.db import SessionLocal, engine
from .app.routes.slack_endpoints import router as slack_router


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def get_app():

    # create the database tables on app startup or reload
    models.Base.metadata.create_all(bind=engine)

    app = FastAPI(
        title="SlashTag Server",
        debug=True,
        description="Managing Slack Integration and API endpoints",
        version=__version__,
    )

    app.include_router(slack_router, prefix="/slack", tags=["slack"])

    # define endpoint
    @app.get("/")
    def home():
        return {"Ahoy": "Captain"}

    # define endpoint
    @app.post("/create_friend")
    def create_friend(
        first_name: str, last_name: str, age: int, db: SessionLocal = Depends(get_db)
    ):
        friend = crud.create_friend(
            db=db, first_name=first_name, last_name=last_name, age=age
        )
        # return object created
        return {"friend": friend}

    return app
