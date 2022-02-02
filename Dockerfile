FROM python:3.7
COPY requirements.txt /

RUN apt-get install ca-certificates -y
RUN update-ca-certificates
ENV REQUEST_CA_BUNDLE=/usr/local/lib/python3.7/site-packages/certifi/cacert.pem
RUN pip install --upgrade pip
RUN pip install -r /requirements.txt
ENV TZ="America/Chicago"

RUN pip install gunicorn

COPY . /app
WORKDIR /app

RUN export PYTHONPATH=/app:$PYTHONPATH
RUN python setup.py install


CMD ["gunicorn", \
   "--threads", "3", \
    "--access-logfile", "-", \
    "--error-logfile", "-", \
    "--timeout", "600", \
    "--bind", "0.0.0.0:3000", \
    "--graceful-timeout", "500", \
    "swimmy.app:create_bot()"]