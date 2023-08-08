# API Healthcheck

A small script to check the health of APIs.

## Installation

```bash
git clone https://github.com/NazarNintendo/api-healthcheck.git
```

## Modify the config file

`data.json` contains the configuration for the script. It is a list of
dictionaries, each dictionary represents an API and contains the following keys:

```json
{
  "id": "api-id",
  "url": "https://api.example.com/healthcheck",
  "freq": 60,
  "integration": "telegram",
  "args": [
    "https://api.telegram.org/.../sendMessage",
    "-928336126"
  ]
}
```

- `id`: a unique identifier for the API
- `url`: the URL to check
- `freq`: the frequency of the checks in seconds
- `integration`: the integration to use to send the notifications
- `args`: the arguments to pass to the integration



## Build the image

```bash
docker build -t api-healthcheck .
```

## Run the container

```bash
docker run -d --name api-healthcheck api-healthcheck
```

## Development

Read the [CONTRIBUTING.md](CONTRIBUTING.md) file.