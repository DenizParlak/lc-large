"""Data access for invoices."""

import sqlite3


def connect():
    return sqlite3.connect("invoices.db")


def search_invoices(conn, term):
    cur = conn.cursor()
    return cur.execute(
        "SELECT id FROM invoices WHERE (label LIKE '%" + term + "%') AND ok = 1"
    ).fetchall()
