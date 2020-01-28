class EmailService:
    def __init__(self):
        self.email_list = ['yymgu@edu.uwaterloo.ca']
        self.subject = 'TRIGGER ALERT'

    @classmethod
    def get_email_subject(cls, summary):
        return summary

    @classmethod
    def get_html_content(cls, summary):
        return summary
