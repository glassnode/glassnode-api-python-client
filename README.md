# glassnode-api-python-client
The official Python client library for Glassnode's API – https://docs.glassnode.com

## Quick Start

### API Key

You can get your API from your [Glassnode account](https://studio.glassnode.com/settings/api).

You can add you API key your environment variables by running:

`export GLASSNODE_API_KEY=<YOUR-KEY>`

### Example Usage

Instantiate the Glassnode client:

```
from glassnode import GlassnodeClient

gn = GlassnodeClient(api_key='YOUR-KEY')
```

If you added the API key to your environment variables you can leave the `api_key` argument empty.

#### Fetching a Metric

To fetch a metric run the client's `get` method:
```
sopr = gn.get(
    'https://api.glassnode.com/v1/metrics/indicators/sopr',
    a='BTC',
    s='2020-01-01',
    i='24h'
)
```

For a complete list of all available metric endpoints endpoints and query parameters please visit [docs.glassnode.com](https://docs.glassnode.com).

## Further Information

* [API documentation](https://docs.glassnode.com/)
* [Overview of metrics and restrictions](https://glassnode.com/metrics)
