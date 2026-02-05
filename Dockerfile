FROM python:3.12-bookworm

ENV USER="user"
ENV PATH="/home/$USER/.local/bin:$PATH"

RUN groupadd --system "$USER"
RUN useradd --system --create-home --shell /bin/bash --gid "$USER" --uid 999 "$USER"

RUN apt-get update
RUN apt-get install -y git
RUN apt-get install -y man
RUN apt-get install -y vim

USER "$USER"
WORKDIR /home/"$USER"

RUN echo 'export PS1="$USER$ "' >> /home/$USER/.bashrc

CMD ["/bin/bash"]
