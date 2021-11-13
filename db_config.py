import cx_Oracle
import sys
import os
import getpass

instant_client_dir = "/usr/lib/oracle/12.1/client64/lib"

if sys.platform.startswith("win"):
    instant_client_dir = r"c:\oracle\instantclient_19_10"

if sys.platform.startswith("darwin"):
    instant_client_dir = os.environ.get("HOME")+"/Downloads/instantclient_19_8"

if instant_client_dir is not None:
    cx_Oracle.init_oracle_client(lib_dir = instant_client_dir)

user = os.environ.get("PYTHON_USER")
if user is None:
    user = getpass.getpass("Enter user: ")

dsn = os.environ.get("PYTHON_CONNECT_STRING", "(DESCRIPTION=(ADDRESS=(PROTOCOL=TCP)(Host=oracle.scs.ryerson.ca)(Port=1521))(CONNECT_DATA=(SID=orcl)))")

pw = os.environ.get("PYTHON_PASSWORD")
if pw is None:
    pw = getpass.getpass("Enter password for %s: " % user)