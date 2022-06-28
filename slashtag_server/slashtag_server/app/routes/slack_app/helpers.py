import os
import tempfile
from pathlib import Path

import requests
from requests.structures import CaseInsensitiveDict


def make_local_filename(url, temp_dir: str = None, prefix: str = None):
    local_filename = url.split("/")[-1]
    temp_dir = temp_dir or os.environ.get("LOCAL_STORAGE_DIR")
    temp_dir = Path(tempfile.mkdtemp() if temp_dir is None else temp_dir) / (
        prefix or "_annon"
    )
    # make directory if it doesn't exist
    temp_dir.mkdir(parents=True, exist_ok=True)

    return temp_dir / local_filename


def download_file(
    url, temp_dir: str = None, chunk_size=8192, token: str = None, prefix: str = None
) -> str:
    assert token is not None, "authentication token is required"

    filename = make_local_filename(url, temp_dir, prefix)

    headers = CaseInsensitiveDict()
    headers["User-Agent"] = "Slashtag App v1.0"
    headers["Authorization"] = f"Bearer {token}"

    with requests.get(
        url,
        headers=headers,
        stream=True,
    ) as r:
        r.raise_for_status()
        with open(filename, "wb") as f:
            for chunk in r.iter_content(chunk_size=chunk_size):
                f.write(chunk)

    return filename
