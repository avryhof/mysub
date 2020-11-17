import datetime

import pytz


def minutes(num_minutes):
    return num_minutes * 60


def make_utc_aware(timestamp):
    return timestamp.replace(tzinfo=pytz.utc)


def aware_utcnow():
    # Return a Timezone ware version of utc now.

    return make_utc_aware(datetime.datetime.utcnow())
