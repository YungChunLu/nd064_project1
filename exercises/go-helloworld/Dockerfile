FROM golang:alpine

WORKDIR /go/src/app

ADD . .

RUN go mod init
RUN go build -o helloworld

CMD ["./helloworld"]