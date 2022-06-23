This is a FastAPI server to manage webhooks for the Slack App

# Running

    poetry install
    poetry run uvicorn slashtag_server.asgi:app --reload

# Install

    poetry config virtualenvs.in-project true
    cd slashtag_server/
    poetry add pre-commit-hooks
    cd ..
    pre-commit install --install-hooks
    # npm i -g gitmoji-cli
    gitmoji --init
