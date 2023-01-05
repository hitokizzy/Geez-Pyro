FROM hitokizzy/ibel:slim-buster

RUN git clone -b main https://github.com/hitokizzy/Geez-Pyro /home/geez/
WORKDIR /home/geez

CMD ["python3","-m","geez"]
