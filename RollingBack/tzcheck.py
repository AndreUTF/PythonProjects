import pytz
import pickle
import sqlite3

db = sqlite3.connect("accounts.sqlite", detect_types=sqlite3.PARSE_DECLTYPES)

# for row in db.execute("SELECT strftime('%Y-%m-%d %H:%M:%f', history.time, 'localtime') AS localtime,"
#                       "history.account, history.amount FROM history ORDER BY history.time"):
for row in db.execute("SELECT * FROM history"):
    utc_time = row[0]
    # pickled_zone = row[3]
    # zone = pickle.loads(pickled_zone)
    zone = pytz.timezone("CET")
    local_time = pytz.utc.localize(utc_time).astimezone()
    print("{}\t{}\t{}".format(utc_time, local_time, local_time.tzinfo))

db.close()