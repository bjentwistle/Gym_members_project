class Booking:
    def __init__(self, member_id, session_id, id = None):
        self.member_id = member_id #foreign key from member class
        self.session_id = session_id  #foreign key from session class
        self.id = id