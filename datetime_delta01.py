from datetime import datetime, timedelta
dt_today = datetime.now()
dt_today

delta = timedelta(days=1)
delta

dt_yesterday = dt_today - delta
dt_yesterday

dt_tomorrow = dt_today + delta
dt_tomorrow

month = timedelta(days=30)
dt_month = dt_today - month

date_string = 01/01/17 12:10:03.234567
date_dt = datetime. strftime(date_string '%m/%d/%y %H:%M:%f')
date_dt