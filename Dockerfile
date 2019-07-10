FROM python:3.7-slim

RUN apt-get update -yqq \
      && apt-get install -yqq chromium chromium-driver \
      && apt-get install -yqq fonts-ipafont-gothic fonts-ipafont-mincho \
      && apt-get install -yqq cron \
      && pip install selenium \
      && pip install requests

RUN echo '30 7   * * *  root   /bin/bash -l /usr/src/cron.sh > /usr/src/cron.log 2>&1' >> /etc/crontab \
     && echo '40 7   * * *  root   /bin/bash -l /usr/src/cron.sh > /usr/src/cron.log 2>&1' >> /etc/crontab \
     && echo '50 7   * * *  root   /bin/bash -l /usr/src/cron.sh > /usr/src/cron.log 2>&1' >> /etc/crontab \
     && env >.env

WORKDIR /usr/src

COPY crawl.py /usr/src/
COPY cron.sh /usr/src/
COPY execcron.sh /usr/src/

CMD ["/bin/sh", "/usr/src/execcron.sh"]