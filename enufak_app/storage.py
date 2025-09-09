import unicodedata
from django.core.files.storage import FileSystemStorage

class NormalizedFileSystemStorage(FileSystemStorage):
    def get_available_name(self, name, max_length=None):
        name = unicodedata.normalize('NFKD', name).encode('ascii', 'ignore').decode('ascii')
        return super().get_available_name(name, max_length)
