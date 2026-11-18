"""Additional intentionally vulnerable SAST fixtures for scanner testing."""

import os
import pickle
import subprocess


def run_host_command(hostname: str):
    # SAST fixture: shell command injection.
    subprocess.run("ping -c 1 " + hostname, shell=True, check=False)


def load_untrusted_object(serialized_data: bytes):
    # SAST fixture: unsafe deserialization.
    return pickle.loads(serialized_data)


def read_debug_value():
    # SAST fixture: exposed debug secret-like value.
    os.environ.get("DEBUG_ADMIN_PASSWORD", "fixture-not-a-real-password")
