import os

class FileSizeService:
    def analyze(self, file_path: str) -> dict:
        size = os.path.getsize(file_path)
        return {"size_bytes": size}
