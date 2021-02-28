#README

## pyhanlp-docker

To build a docker image with Python 3.7 、Zulu 11 、 pyhanlp and cocoNLP。Dockerfile is adapted from [docker-java-python](https://github.com/rappdw/docker-java-python "docker-java-python")  

```shell
docker build -t pyhanlp .
docker run -it -p 8765:8765 pyhanlp hanlp serve
```
