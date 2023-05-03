class Session:
    def __init__(self, name, duration, premium_session, what_day, what_time, id = None):
        self.name = name
        self.duration = duration
        self.premium_session = premium_session
        self.what_day = what_day
        self.what_time = what_time
        self.id = id
