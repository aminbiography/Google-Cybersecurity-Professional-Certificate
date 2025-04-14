"""
Google Cybersecurity Professional Certificate
=============================================

View Certificate Badge:
-----------------------
https://www.credly.com/badges/YOUR_BADGE_ID

<img src="https://images.credly.com/size/680x680/images/0bf0f2da-a699-4c82-82e2-56dcf1f2e1c7/image.png" 
     alt="Google Cybersecurity Certificate on Coursera" width="300"/>

Live Project Page:
------------------
https://aminbiography.github.io/Google-Cybersecurity-Professional-Certificate/

License
-------
MIT License

Copyright (c) 2024 Mohammad Aminul Islam

This repository contains personal notes and official certificates from the
Google Cybersecurity Professional Certificate on Coursera.

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Materials"), to deal
in the Materials without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Materials, and to permit persons to whom the Materials are
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Materials.

THE MATERIALS ARE PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES, OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE MATERIALS OR THE USE OR OTHER DEALINGS IN
THE MATERIALS.
"""

# List of Coursera Certificates (Courses 1-8)
certificates = [
    {
        "title": "Course 1: Foundations of Cybersecurity",
        "url": "https://www.coursera.org/account/accomplishments/certificate/21J47YRQG8P5",
        "image": "https://s3.amazonaws.com/coursera_assets/meta_images/generated/CERTIFICATE_LANDING_PAGE/CERTIFICATE_LANDING_PAGE~21J47YRQG8P5.jpeg"
    },
    {
        "title": "Course 2: Play It Safe: Manage Security Risks",
        "url": "https://www.coursera.org/account/accomplishments/certificate/OA7G8JR2H7Z9",
        "image": "https://s3.amazonaws.com/coursera_assets/meta_images/generated/CERTIFICATE_LANDING_PAGE/CERTIFICATE_LANDING_PAGE~OA7G8JR2H7Z9.jpeg"
    },
    {
        "title": "Course 3: Connect and Protect: Networks and Network Security",
        "url": "https://www.coursera.org/account/accomplishments/certificate/IAC5IIN9W8WQ",
        "image": "https://s3.amazonaws.com/coursera_assets/meta_images/generated/CERTIFICATE_LANDING_PAGE/CERTIFICATE_LANDING_PAGE~IAC5IIN9W8WQ.jpeg"
    },
    {
        "title": "Course 4: Tools of the Trade: Linux and SQL",
        "url": "https://www.coursera.org/account/accomplishments/certificate/CPA899ZQOXHC",
        "image": "https://s3.amazonaws.com/coursera_assets/meta_images/generated/CERTIFICATE_LANDING_PAGE/CERTIFICATE_LANDING_PAGE~CPA899ZQOXHC.jpeg"
    },
    {
        "title": "Course 5: Assets, Threats, and Vulnerabilities",
        "url": "https://www.coursera.org/account/accomplishments/certificate/77U1JUDD0QKY",
        "image": "https://s3.amazonaws.com/coursera_assets/meta_images/generated/CERTIFICATE_LANDING_PAGE/CERTIFICATE_LANDING_PAGE~77U1JUDD0QKY.jpeg"
    },
    {
        "title": "Course 6: Sound the Alarm: Detection and Response",
        "url": "https://www.coursera.org/account/accomplishments/certificate/HYVE1Z9ZT2LV",
        "image": "https://s3.amazonaws.com/coursera_assets/meta_images/generated/CERTIFICATE_LANDING_PAGE/CERTIFICATE_LANDING_PAGE~HYVE1Z9ZT2LV.jpeg"
    },
    {
        "title": "Course 7: Automate Cybersecurity Tasks with Python",
        "url": "https://www.coursera.org/account/accomplishments/verify/CIUW7RTZ0CA0",
        "image": "https://s3.amazonaws.com/coursera_assets/meta_images/generated/CERTIFICATE_LANDING_PAGE/CERTIFICATE_LANDING_PAGE~CIUW7RTZ0CA0.jpeg"
    },
    {
        "title": "Course 8: Put It to Work: Prepare for Cybersecurity Jobs (Final Course)",
        "url": "https://www.coursera.org/account/accomplishments/certificate/2GLRWLH1Y7SK",
        "image": "https://coursera-certificate-images.s3.amazonaws.com/2GLRWLH1Y7SK"
    }
]

# Function to display certificates
def display_certificates(certs):
    for cert in certs:
        print(f" {cert['title']}")
        print(f" {cert['url']}")
        print(f" {cert['image']}")
        print("-" * 80)


# Run display
if __name__ == "__main__":
    display_certificates(certificates)
