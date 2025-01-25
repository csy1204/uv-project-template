import os

from common_example.services.io.s3_manager import S3Manager


def get_file_list(path, ext=None):
    """
    Get the list of files in the directory with the specified extension.

    Args:
        path (str): Path to the directory.
        ext (str): Extension of the files to be listed.

    Returns:
        list: List of files in the directory.
    """
    if not os.path.exists(path):
        raise FileNotFoundError(f"Directory '{path}' does not exist.")
    if ext is None:
        return [os.path.join(path, f) for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]
    return [
        os.path.join(path, f) for f in os.listdir(path) if os.path.isfile(os.path.join(path, f)) and f.endswith(ext)
    ]


def get():
    manager = S3Manager()
    print(manager)
