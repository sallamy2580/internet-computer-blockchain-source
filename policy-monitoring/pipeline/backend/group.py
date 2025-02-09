from typing import Iterable
from typing import Optional

from pipeline.global_infra import GlobalInfra


class Group:
    def __init__(
        self,
        gid: str,
        logs: Iterable = [],
        url: Optional[str] = None,
        global_infra: Optional[GlobalInfra] = None,
    ):
        self.logs = logs
        self.gid = gid
        self.url = url
        self.global_infra = global_infra

    def __str__(self) -> str:
        """Logging-friendly representation"""
        return f"<Group gid={self.gid}>"
