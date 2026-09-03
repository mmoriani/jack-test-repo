"""Backend HTTP app.

Espone una pagina HTML di test e l'health-check pubblico ``GET /ping``.
"""

from datetime import datetime, timezone
from pathlib import Path

from fastapi import FastAPI
from fastapi.responses import FileResponse

APP_ROOT = Path(__file__).resolve().parent


def _read_version() -> str:
    """Legge la versione applicativa dal file VERSION accanto a questo modulo."""
    version_file = APP_ROOT / "VERSION"
    try:
        return version_file.read_text(encoding="utf-8").strip() or "unknown"
    except OSError:
        return "unknown"


VERSION = _read_version()

app = FastAPI(title="claude-test backend")


@app.get("/", response_class=FileResponse)
def home() -> FileResponse:
    """Serve la pagina usata per provare il browser integrato."""
    return FileResponse(APP_ROOT / "index.html")


@app.get("/ping")
def ping() -> dict:
    """Health-check pubblico: nessuna auth, nessun accesso al DB.

    Restituisce conferma di vita, versione applicativa e ora del server.
    """
    return {
        "pong": True,
        "version": VERSION,
        # ISO 8601 in UTC con suffisso "Z" (es. 2026-06-19T10:00:00Z)
        "time": datetime.now(timezone.utc)
        .replace(microsecond=0)
        .isoformat()
        .replace("+00:00", "Z"),
    }


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8080)
