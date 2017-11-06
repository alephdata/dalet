import re
from normality import stringify

from exactitude.common import ExactitudeType
from exactitude.domain import DomainType


class EmailType(ExactitudeType):
    EMAIL_REGEX = re.compile(r"[^@]+@[^@]+\.[^@]+")
    domains = DomainType()

    def validate(self, email, **kwargs):
        """Check to see if this is a valid email address."""
        email = stringify(email)
        if email is None:
            return
        if not self.EMAIL_REGEX.match(email):
            return False
        mailbox, domain = email.rsplit('@', 1)
        return self.domains.validate(domain, **kwargs)

    def clean_text(self, email, **kwargs):
        """Parse and normalize an email address.

        Returns None if this is not an email address.
        """
        if not self.EMAIL_REGEX.match(email):
            return None
        mailbox, domain = email.rsplit('@', 1)
        domain = self.domains.clean(domain, **kwargs)
        return '@'.join((mailbox, domain))

    def normalize(self, email, **kwargs):
        """Normalize for comparison."""
        emails = super(EmailType, self).normalize(email, **kwargs)
        return [e.lower() for e in emails]
