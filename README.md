# PlutonicationServer
Flask version of Plutonication

# Automatically generate requirements.txt

```
pip install pipreqs
pipreqs . --force
```

# Docker

```
docker build --tag plutonication .

docker run plutonication
```

# Stress testing

Tests the `limit_socketio` capabilities.

- uses Node v16.17.1

```
cd stresstests

npm i

node index.js
```
