import imaplib
import email
import re


IMAP_SERVER = "outlook.office365.com"
IMAP_PORT = 993

class Emailutils:
    @staticmethod
    def getreset_password_link(email_host,email_user,email_pass):
        try:
            mail = imaplib.IMAP4_SSL(email_host, IMAP_PORT)
            mail.login(email_user,email_pass)
            mail.select("inbox")


            result, data = mail.search(None, 'FROM "noreply@infotime.com" SUBJECT "Reset Password"')
            mail_ids = data[0].split()

            if mail_ids:
                latest_email_id = mail_ids[-1]
                result, email_data = mail.fetch(latest_email_id, "(RFC822)")

                for response_part in email_data:
                    if isinstance(response_part,tuple):
                        msg = email.message_from_bytes(response_part[1])
                        if msg.is_multipart():
                            for part in msg.walk():
                                content_type = part.get_content_type()
                                if content_type == "text/plain":
                                    email_body = part.get_payload(decode=True).decode(errors="ignore")
                                    break

                    else:
                        email_body = msg.get_payload(decode = True).decode(errors="ignore")

                    reset_link_pattern = r"https://infotimeqa.azurewebsites.net/resetpassword/MTM/ckuqtq-cbaf0a6c2ae54d73b5bf72377542e986"
                    reset_link = re.search(reset_link_pattern, email_body)

                    #reset_link = re.search("https://infotimeqa.azurewebsites.net/resetpassword/MTM/ckg611-110739338b0e0f94f66bf0f29321dcfe",email_body)

                    if reset_link:
                        return reset_link.group(0)


        except Exception as e:
            print(f"Error fetching reset link: {e}")

        finally:
            mail.logout()

        return None