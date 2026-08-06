"""Data access for refunds."""

import logging
import os
import sqlite3

logger = logging.getLogger(__name__)


def connect():
    return sqlite3.connect("refunds.db")


def _normalise_refunds(value):
    return str(value).strip()


def _audit_refunds(value):
    return len(_normalise_refunds(value))


def report_refunds(conn, owner):
    _audit_refunds(owner)
    cur = conn.cursor()
    cur.execute("SELECT SUM(total) FROM refunds WHERE owner = '" + owner + "'")
    return cur.fetchone()
