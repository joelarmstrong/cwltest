# Stubs for galaxy.util.checkers (Python 3.4)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any, Optional

def check_html(file_path, chunk: Optional[Any] = ...): ...
def check_binary(name, file_path: bool = ...): ...
def check_gzip(file_path): ...
def check_bz2(file_path): ...
def check_zip(file_path): ...
def is_bz2(file_path): ...
def is_gzip(file_path): ...
def check_image(file_path): ...
