import os

import reflex as rx

# URL of the deployed Reflex backend (the long-running Python/WebSocket
# server). Set BACKEND_URL in the build environment to the public https URL
# of your backend host (e.g. https://porfolio-rx.up.railway.app).
# The frontend uses this to open its WebSocket at wss://<backend>/_event.
backend_url = os.environ.get("BACKEND_URL", "http://localhost:8000")

config = rx.Config(
    app_name="portafolio",
    # Where the frontend connects for /_event (state sync / event handlers).
    api_url=backend_url,
    # Public URL of the deployed frontend.
    deploy_url=os.environ.get("FRONTEND_URL", "http://localhost:3000"),
)
