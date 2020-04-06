from datetime import datetime
import whois

class DomainInfo:
    def __init__(self, domain):
        self.w = whois.query(domain)

    def get_domain_age_in_days(self):
        if (self.w is not None):
            today = datetime.today()
            return (today - self.w.creation_date).days
        else:
            return -1