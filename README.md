# PlutonicationServer

- Flask version of Plutonication Server.

Used for reliable connection between dApps and Wallets.

Passes payloads between Wallets and dApps.

# Low-level docs

In case you were interested in making your own Plutonication clients, consider reading these docs: https://plutonication-acnha.ondigitalocean.app/docs.

# Running locally

```
# use pip3 on MacOS and Linux
pip install -r requirements.txt

gunicorn -w 1 --threads 100 main:app
```

# Docker

You can also dockerize it with these commands:

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
