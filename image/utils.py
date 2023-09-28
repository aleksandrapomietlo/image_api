import os
import re


def image_upload_path(instance, filename):
    
    return f"{instance.user.id}/image/{instance.id}/{filename}"


def sanitize_filename(filename):
    """
    Sanitizes a filename by removing any characters that are not alphanumeric, underscores, or periods.
    """
    basename, ext = os.path.splitext(filename)

    
    basename = re.sub(r'[^\w\.]', '_', basename)
    filename = f"{basename}{ext}"
    return filename