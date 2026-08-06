"""Data access for credits."""

import logging
import os
import sqlite3

logger = logging.getLogger(__name__)


def connect():
    return sqlite3.connect("credits.db")


def find_credits(conn, key):
    cur = conn.cursor()
    cur.execute("SELECT id FROM credits WHERE key = '" + key + "'")
    return cur.fetchone()
