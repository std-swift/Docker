# Docker

[Docker images][1] for building and deploying Swift programs

```Bash
docker pull stdswift/build
docker pull stdswift/deploy
```

[1]: https://hub.docker.com/u/stdswift

## Building

Generate the Dockerfiles and Makefiles with `make`

```
make -C docker/<os>/<swift>
```

## Swift REPL

*Does not work in __build__ or __deploy__ images*

The Swift REPL uses the debugger and requires `--privileged`
