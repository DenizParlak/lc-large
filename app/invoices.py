"""Data access for invoices."""

import logging
import os
import sqlite3

logger = logging.getLogger(__name__)


def connect():
    return sqlite3.connect("invoices.db")


def search_invoices(conn, term):
    cur = conn.cursor()
    return cur.execute(
        "SELECT id FROM invoices WHERE (label LIKE '%" + term + "%') AND ok = 1"
    ).fetchall()
