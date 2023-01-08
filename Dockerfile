FROM hitokizzy/ibel:slim-buster
RUN apt-get update -y && apt-get upgrade -y \
    && apt-get install -y --no-install-recommends ffmpeg \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*
RUN git clone -b main https://github.com/hitokizzy/Geez-Pyro /home/geez/
WORKDIR /home/geez

CMD ["python3","-m","geez"]
