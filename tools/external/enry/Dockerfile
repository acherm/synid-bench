# go-enry (Go port of Linguist, used by StarCoder2's data pipeline), pinned
FROM golang:1.23 AS build
WORKDIR /src
COPY go.mod go.sum main.go ./
RUN go mod download && CGO_ENABLED=0 go build -mod=readonly -o /enry-identify .
FROM gcr.io/distroless/static-debian12
COPY --from=build /enry-identify /enry-identify
ENTRYPOINT ["/enry-identify"]
