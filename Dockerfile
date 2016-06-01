FROM fedora:23
MAINTAINER Tomas Tomecek <ttomecek@redhat.com>

COPY ./results/xmind-3.6.1-1.fc23.x86_64.rpm /data/
RUN dnf install -y /data/xmind-3.6.1-1.fc23.x86_64.rpm

ARG USER_ID=1000
RUN useradd -o -u ${USER_ID} -G video xmind
USER xmind
ENV HOME /home/xmind
CMD ["/usr/bin/xmind"]
