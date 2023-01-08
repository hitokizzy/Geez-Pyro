FROM nikolaik/python-nodejs:python3.9-nodejs18
RUN apt-get update \
    && apt-get install -y --no-install-recommends ffmpeg \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

FROM hitokizzy/ibel:slim-buster
RUN git clone -b main https://github.com/hitokizzy/Geez-Pyro /home/geez/
WORKDIR /home/geez
RUN pip3 install --no-cache-dir --upgrade --requirement requirements.txt

CMD ["python3","-m","geez"]
