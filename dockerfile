# set the base image

FROM python:2.7

LABEL version="0.1"

LABEL description="MAC program with Dockerfile."

#RUN mkdir -p /Demo

ADD mac.py .

# ADD macaddress_io.apikey /Demo/.

#RUN pip install requests

RUN if [ $(pip list | grep requests) ]; then echo "Python package already installed"; else echo "Python packages not installed. Installing...."; pip install requests; fi

CMD [ "python", "mac.py" ]

