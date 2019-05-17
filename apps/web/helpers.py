"""
This module servers as a behavior to create usefull functions
that can be used in many views.
"""

from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string


def send_email(subject, from_email, to_email, text_path, html_path, context, is_admin):
    """
    This function will be used to send an smtp message to email server.
    The email server will delivery the message with its html and text content.
    """

    message_context = {
        "name": context["name"],
        "email": context["email"],
        "subject": context["subject"],
        "description": context["description"],
        "is_admin": is_admin,
    }

    text_content = render_to_string(text_path, message_context)
    html_content = render_to_string(html_path, message_context)

    print(to_email)

    email_message = EmailMultiAlternatives(
        subject, text_content, from_email, [to_email]
    )
    email_message.attach_alternative(html_content, "text/html")
    email_message.content_subtype = "html"

    return email_message.send()


def group_directors(directors):
    """
    This function will group all directors by year.
    It will be used inside the about View to create a history.
    """
    history = []
    for director in directors:
        if history == []:
            history.append({"year": director.started_at.year, "directors": [director]})
            check = False
            continue

        for value in history:
            if value["year"] == director.started_at.year:
                value["directors"].append(director)
                check = True
            else:
                check = False

        if not check:
            history.append({"year": director.started_at.year, "directors": [director]})

    return history
