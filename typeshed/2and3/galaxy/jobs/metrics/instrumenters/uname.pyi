# Stubs for galaxy.jobs.metrics.instrumenters.uname (Python 3.4)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any
import formatting
from ..instrumenters import InstrumentPlugin

class UnameFormatter(formatting.JobMetricFormatter):
    def format(self, key, value): ...

class UnamePlugin(InstrumentPlugin):
    plugin_type = ...  # type: str
    formatter = ...  # type: Any
    uname_args = ...  # type: Any
    def __init__(self, **kwargs) -> None: ...
    def pre_execute_instrument(self, job_directory): ...
    def job_properties(self, job_id, job_directory): ...