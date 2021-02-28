# pyhanlp

To build a docker image with Python 3.7 、Zulu 11 、 pyhanlp and cocoNLP。

docker build -t pyhanlp .
docker run -it -p 8765:8765 pyhanlp hanlp serve
