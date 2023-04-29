class Booking:
    def __init__(self, id = None, member, session):
        self.id = id
        self.member = member #foreign key from member class
        self.session = session  #foreign key from session class