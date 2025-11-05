FROM python:3.12-bookworm

ENV USER="user"
ENV PATH="/home/$USER/.local/bin:$PATH"

RUN groupadd --system "$USER"
RUN useradd --system --create-home --gid "$USER" --uid 999 "$USER"

RUN apt-get update
RUN apt-get upgrade
RUN apt-get autoremove
RUN apt-get autoclean

RUN apt-get install -y git
RUN apt-get install -y man
RUN apt-get install -y vim

USER "$USER"
WORKDIR /home/"$USER"
