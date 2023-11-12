# PlutonicationServer

- Flask version of Plutonication Server.

Used for reliable connection between dApps and Wallets.

Passes payloads between Wallets and dApps.

# Low-level docs

In case you were interested in making your own Plutonication clients, consider reading these docs: https://plutonication-acnha.ondigitalocean.app/docs.

# In code docs

In code docs for each method are included.

<img width="760" alt="Screenshot 2023-11-10 at 22 34 23" src="https://github.com/RostislavLitovkin/PlutonicationServer/assets/77352013/0489922d-b27b-4a19-98c7-4a3e8af1a731">

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

# Unit testing

- tested on Node v16.17.1

To run unit tests and stresstests, run:
```
cd tests

npm i

npx playwright test
```

To run just unit tests, run:
```
npx playwright test events.spec.js
```

To run just stress tests, run:
```
npx playwright test stresstest.spec.js
```
