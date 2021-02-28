FROM python:3.7

ENV LANG=C.UTF-8 LC_ALL=C.UTF-8

RUN sed -i 's/deb.debian.org/mirrors.ustc.edu.cn/g' /etc/apt/sources.list && \
    sed -i 's|security.debian.org/debian-security|mirrors.ustc.edu.cn/debian-security|g' /etc/apt/sources.list

ENV APT_KEY_DONT_WARN_ON_DANGEROUS_USAGE=DontWarn

RUN set -e; \
    apt-get update; \
    apt-get install -y --no-install-recommends \
        software-properties-common \
    ; \
    apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys 0xB1998361219BD9C9; \
    apt-add-repository 'deb http://repos.azulsystems.com/debian stable main'; \
    apt-get update; \
    apt-get install -y --no-install-recommends \
        zulu-11 \
    ; \
    apt-get clean; \
    rm -rf /var/tmp/* /tmp/* /var/lib/apt/lists/*

RUN mkdir -p /usr/local/lib/python3.7/site-packages/pyhanlp/static/ && \
    wget https://file.hankcs.com/hanlp/hanlp-1.8.0-release.zip -O /usr/local/lib/python3.7/site-packages/pyhanlp/static/hanlp-1.8.0-release.zip && \
    wget https://file.hankcs.com/hanlp/data-for-1.7.5.zip -O /usr/local/lib/python3.7/site-packages/pyhanlp/static/data-for-1.8.0.zip && \
    pip install pyhanlp -i  https://mirrors.aliyun.com/pypi/simple/ 

RUN pip install -v cocoNLP==0.0.13 -i https://mirrors.aliyun.com/pypi/simple/  
