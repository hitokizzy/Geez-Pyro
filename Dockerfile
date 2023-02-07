FROM hitokizzy/geezram:slim-buster

RUN git clone -b master https://github.com/hitokizzy/Geez-Pyro /home/geez/
WORKDIR /home/geez

RUN wget https://raw.githubusercontent.com/hitokizzy/Geez-Pyro/main/requirements.txt \
    && pip3 install --no-cache-dir --use-deprecated=legacy-resolver -r requirements.txt \
    && rm requirements.txt \
RUN bash start
