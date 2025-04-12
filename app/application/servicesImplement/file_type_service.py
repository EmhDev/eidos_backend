import mimetypes

class FileTypeService:
    def analyze(self, file_path: str) -> dict:
        file_type, _ = mimetypes.guess_type(file_path)
        return {"type": file_type or "unknown"}
