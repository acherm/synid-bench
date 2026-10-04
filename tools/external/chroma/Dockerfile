# Chroma (Go syntax highlighter used by Hugo; lexers.Match / lexers.Analyse as its CLI's "autodetect"), pinned
FROM golang:1.25.14 AS build
WORKDIR /src
COPY go.mod go.sum main.go ./
RUN go mod download && CGO_ENABLED=0 go build -mod=readonly -o /chroma-identify .
FROM gcr.io/distroless/static-debian12
COPY --from=build /chroma-identify /chroma-identify
ENTRYPOINT ["/chroma-identify"]
