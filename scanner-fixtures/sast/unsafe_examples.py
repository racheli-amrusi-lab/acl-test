"""Intentionally unsafe examples for static-analysis scanner testing only."""

import sqlite3


def find_user(username: str):
    # SAST fixture: unsafe SQL string interpolation.
    connection = sqlite3.connect(":memory:")
    query = "SELECT * FROM users WHERE name = '%s'" % username
    return connection.execute(query).fetchall()


def read_file(path: str):
    # SAST fixture: unvalidated user-controlled path.
    with open(path, "r", encoding="utf-8") as handle:
        return handle.read()
