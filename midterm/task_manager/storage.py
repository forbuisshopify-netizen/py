"""JSON ფაილის წაკითხვა და უსაფრთხოდ ჩანაცვლება."""
import json
from pathlib import Path
from tempfile import NamedTemporaryFile


def load(path, default):
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError:
        return default


def save(path, data):
    # ძველი ფაილი მხოლოდ ახალი ასლის სრულად ჩაწერის შემდეგ იცვლება.
    with NamedTemporaryFile(dir=path.parent, delete=False, mode="w",
                            encoding="utf-8") as stream:
        temporary = Path(stream.name)
        try:
            json.dump(data, stream, ensure_ascii=False, indent=2)
            stream.flush()
        except BaseException:
            stream.close()
            temporary.unlink(missing_ok=True)
            raise
    try:
        temporary.replace(path)
    finally:
        temporary.unlink(missing_ok=True)
