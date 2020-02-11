# docker-helloworld-tcp-server
Simple docker image implemented in python

## Running

```
docker run -p 8080:8080 benjjefferies/docker-helloworld-tcp-server
```

# Usage

```
{ echo "hello"; sleep 1; }  | telnet localhost 8080      
Trying ::1...
Connected to localhost.
Escape character is '^]'.
world
Connection closed by foreign host.
```