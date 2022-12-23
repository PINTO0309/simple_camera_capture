FROM ubuntu:20.04

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update \
    && apt-get install -y \
        python3-pip \
        python3-mock \
        libpython3-dev \
        python-is-python3 \
        libglib2.0-0 \
        libsm6 \
        libxrender1 \
        libfontconfig1 \
        libxext6 \
        sudo \
        v4l-utils \
    && apt clean \
    && rm -rf /var/lib/apt/lists/*

RUN pip install pip -U \
    && pip install opencv-python==4.1.2.30 \
    && pip install -U simpcamcap \
    && pip install -U simpcamcap \
    && python -m pip cache purge

ENV USERNAME=user
RUN echo "root:root" | chpasswd \
    && adduser --disabled-password --gecos "" "${USERNAME}" \
    && echo "${USERNAME}:${USERNAME}" | chpasswd \
    && echo "%${USERNAME}    ALL=(ALL)   NOPASSWD:    ALL" >> /etc/sudoers.d/${USERNAME} \
    && chmod 0440 /etc/sudoers.d/${USERNAME} \
    && usermod -a -G video ${USERNAME}
USER ${USERNAME}
ARG WKDIR=/workdir
WORKDIR ${WKDIR}
RUN sudo chown ${USERNAME}:${USERNAME} ${WKDIR}
