from typing import Callable, Dict
from keybind import KeyBinder
from functools import partial
import subprocess
from pathlib import Path


def run(cmd: str) -> None:
    args = cmd.split(" ")
    subprocess.run(args)


class Binder:
    def __init__(self) -> None:
        self.bindings: Dict[str, Callable] = {}

    def parse_bindings(self) -> None:
        bindings_dir = Path("bindings")
        lines = []
        for bindings_path in bindings_dir.glob("*.txt"):
            with open(bindings_path) as f:
                lines.extend([line.strip() for line in f.readlines()])

        for line in lines:
            k, cmd = line.split("#")
            self.bindings[k] = partial(run, cmd)

    def bind(self) -> None:
        KeyBinder.activate(self.bindings)
