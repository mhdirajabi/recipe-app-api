# pull official base image
FROM python:3.7-alpine

# set working directory
RUN mkdir /app
WORKDIR /app
COPY ./app /app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install psycopg2 dependencies
RUN apk add --no-cache postgresql14-dev=~14.2-r0 gcc=~10.3.1_git20211027-r0 \
    python3-dev=~3.9.7-r4 musl-dev=~1.2.2-r7 \
# install dependencies
    && pip install --upgrade --no-cache-dir pip==22.0.4
COPY ./requirements.txt /requirements.txt
RUN pip install --no-cache-dir -r /requirements.txt

# copy entrypoint.sh
COPY ./entrypoint.sh /entrypoint.sh
RUN sed -i 's/\r$//g' /entrypoint.sh \
    && chmod +x /entrypoint.sh

# run entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]