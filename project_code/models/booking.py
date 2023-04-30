class Booking:
    def __init__(self, member, session, id = None):
        self.id = id
        self.member = member #foreign key from member class
        self.session = session  #foreign key from session class