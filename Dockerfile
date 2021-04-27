# FROM ubuntu:18.04

# WORKDIR /

# COPY requirements.txt .
# COPY . /beneath-stream

# RUN apt-get -y update

# # Install Python 3.7 and make it the default
# # This doesn't totally work
# RUN apt-get install -y python3.7
# # RUN echo "alias python3=python3.7" > .bashrc
# # RUN /bin/bash -c "source /usr/local/bin/virtualenvwrapper.sh"

# RUN curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
# RUN python3.7 get-pip.py --force-reinstall
# # RUN update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.7 1
# # RUN update-alternatives --config python3
# # RUN apt-get install python3-dev -y

# # Install pip and requirements
# # RUN apt-get install -y python3-pip
# # RUN python3.7 -m pip install pip
# RUN pip3 install -r requirements.txt

# CMD ["/bin/bash"]



FROM ubuntu:18.04

WORKDIR /

COPY requirements.txt .
COPY . /beneath-stream
COPY secret.txt /root/.beneath/secret.txt

# Upgrade installed packages
RUN apt-get update && apt-get upgrade -y && apt-get clean
RUN apt-get install vim -y

# Python package management and basic dependencies
RUN apt-get install -y curl python3.7 python3.7-dev python3.7-distutils

# Register the version in alternatives
RUN update-alternatives --install /usr/bin/python python /usr/bin/python3.7 1

# Set python 3 as the default python
RUN update-alternatives --set python /usr/bin/python3.7

# Upgrade pip to latest version
RUN curl -s https://bootstrap.pypa.io/get-pip.py -o get-pip.py && \
    python get-pip.py --force-reinstall && \
    rm get-pip.py

RUN pip3 install -r requirements.txt

CMD ["/bin/bash"]