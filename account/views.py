# views.py

from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from .forms import ApplicantForm

def applicant_form(request):
    if request.method == 'POST':
        # FIX: Added request.FILES to handle the uploaded file data
        form = ApplicantForm(request.POST, request.FILES)
        
        if form.is_valid():
            # We save the form so the resume is saved to your server,
            # but we cannot attach it to the email with send_mail.
            form.save()

            # Extract data
            name = form.cleaned_data['name']
            mobile = form.cleaned_data['mobile']
            user_email = form.cleaned_data['email']
            feedback = form.cleaned_data['feedback']
            



            # Compose email
            subject = f"📬 New Form Submission from {name}"
            message = f"""
A new user has filled the form.

Name: {name}
Mobile: {mobile}
Email: {user_email}
Feedback/Demand: {feedback}

"""
            try:
                # Use the send_mail function
                send_mail(
                    subject=subject,
                    message=message,
                    from_email=settings.EMAIL_HOST_USER,  # Best practice: Use email from settings.py
                    recipient_list=['saranshsahu532@gmail.com'], # Must be a list or tuple
                   
                )
                print("✅ Email sent successfully!")
            except Exception as e:
                print(f"❌ Email sending failed: {e}")

            return render(request, 'success.html', {'name': name})
    else:
        form = ApplicantForm()

    return render(request, 'mainbox.html', {'form': form, 'title': "gixtechnology"})