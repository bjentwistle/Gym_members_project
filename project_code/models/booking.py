class Booking:
    def __init__(self, member, session, id = None):
        self.member = member #foreign key from member class will be member.id
        self.session = session  #foreign key from session class will be session.id
        self.id = id


# Alex suggesting changes 
# class BookingResult(self, booking_id, first_name, last_name, session_name):
