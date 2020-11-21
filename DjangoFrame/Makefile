NAME=DjangoFrame

BUILD_ARG=--build-arg http_proxy=http://172.16.6.67:3128 --build-arg https_proxy=http://172.16.6.67:3128

base:
    echo build ${NAME}:base
    cp build/docker/base/Dockerfile .
    docker build -t ${NAME}:base . ${BUILD_ARG}
    rm Dockerfile
    # docker push ${NAME}:base

dev:
    cp build/docker-compose.yml .
    docker-compose up -d
    rm docker-compose.yml

down:
    cp build/docker-compose.yml .
    docker-compose down
    rm docker-compose.yml

update:
    cp build/docker-compose.yml .
    docker-compose restart
    rm docker-compose.yml
