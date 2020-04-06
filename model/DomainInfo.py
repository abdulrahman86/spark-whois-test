from datetime import datetime
import whois

class DomainInfo:
    def __init__(self, domain):
        self.whois_info = whois.query(domain)


    def get_domain_age_in_days(self):
        if (self.whois_info is not None):
            today = datetime.today()
            return (today - self.whois_info.creation_date).days
        else:
            return -1

    def get_domain_registrar(self):
        if (self.whois_info is not None):
            return self.whois_info.registrar
        else:
            return None

    def get_domain_expiration(self):
        if (self.whois_info is not None):
            return self.whois_info.expiration_date.strftime("%m/%d/%Y, %H:%M:%S")
        else:
            return None

