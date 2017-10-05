# Heavy-weight docker file for development on OmniC
FROM python:3.6.2-stretch
MAINTAINER michaelb <michaelpb@gmail.com>

ENV PYTHONUNBUFFERED 1

# Terrible way to add sources for node
RUN curl -sL http://deb.nodesource.com/setup_6.x | bash -


# TODO: nodejs is not venison locked, can't be because of the above issue, need
# to incorporate a proper node version that actually builds from source down to
# a patch number

# Pull in system reqs
RUN apt-get update && apt-get install -y \
    imagemagick=8:6.9.7.4+dfsg-11+deb9u1 \
    inkscape=0.92.1-1 \
    meshlab=1.3.2+dfsg1-3 \
    nodejs \
    openbabel=2.3.2+dfsg-3 \
    unoconv=0.7-1.1

# Punting on JS compilation and jsc3d stuff
RUN npm install -g jsc3d

#RUN npm install -g \
#    babel-cli@6.24.1 \
#    babel-preset-es2015@6.24.1 \
#    browserify@14.4.0 \
#    jsc3d@0.1.8 \
#    uglify-js@3.0.20

# Setup python reqs
COPY ./requirements.txt /requirements.txt
RUN pip install --no-cache-dir -r /requirements.txt \
    && rm /requirements.txt

# Setup code directory
ADD . /app
WORKDIR /app

EXPOSE 80

CMD omnic runserver
