import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

class Mail():
    """
    Class for sending email notifications.

    Attributes:
        email (str): The sender's email address.
        password (str): The sender's email password.
    """

    def __init__(self, email, password) -> None:
        """
        Initializes the Mail instance with sender's email and password.

        Args:
            email (str): The sender's email address.
            password (str): The sender's email password.
        """
        self.smtp = smtplib.SMTP('smtp.gmail.com', 587)
        self.email = email
        self.password = password

    def send(self, mail, msg) -> None:
        """
        Send an email notification.

        Args:
            mail (str): The recipient's email address.
            msg (str): The email message content.

        Returns:
            None
        """
        self.smtp = smtplib.SMTP('smtp.gmail.com', 587)
        self.smtp.starttls()
        self.smtp.login(self.email, self.password)
        self.mail = mail


        # The content to be mailed
        self.msg = MIMEMultipart()
        self.msg['Subject'] = f"Temperature Alert"
        self.msg.attach(MIMEText(msg, 'plain'))

        # Send the mail
        self.smtp.sendmail(self.email, self.mail, self.msg.as_string())
        self.smtp.quit()
