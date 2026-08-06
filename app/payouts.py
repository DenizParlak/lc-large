"""Data access for payouts."""

import sqlite3


def connect():
    return sqlite3.connect("payouts.db")


def list_payouts(conn, email):
    cur = conn.cursor()
    return cur.execute(
        "SELECT id, total FROM payouts WHERE email = '%s' ORDER BY id" % email
    ).fetchall()
