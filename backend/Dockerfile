FROM nginx/unit:1.25.0-python3.9
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

RUN mkdir /code
WORKDIR /code
COPY requirements.txt /code/
RUN export DEBIAN_FRONTEND=noninteractive \
    && export DEBCONF_NOWARNINGS=yes \
    && apt-get update \
    && apt-get install -y python3-pip \
    && pip3 install --disable-pip-version-check -r requirements.txt \
    && apt-get remove -y python3-pip \
    && apt-get autoremove --purge -y \
    && rm -rf /var/lib/apt/lists/* /etc/apt/sources.list.d/*.list
COPY . /code/
EXPOSE 8000
