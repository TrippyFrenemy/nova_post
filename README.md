# Nova\_Post

A Python wrapper for the Nova Poshta API, providing an easy-to-use interface for interacting with Nova Poshta's logistics and tracking services.

## Features

- Address management: create, update, delete addresses, and retrieve city, warehouse, and street directories.
- Counterparty management: manage sender/receiver contacts and related information.
- Internet document (waybill) management: create, update, delete, and track shipments.
- Common API methods: retrieve time intervals, cargo types, packaging options, and service types.
- Shipment tracking: track parcels via document numbers and phone numbers.

## Installation

You can install **Nova\_Post** via pip:

```sh
pip install nova-post
```

## Usage

### Initialization

```python
from nova_post.api import NovaPostApi

api = NovaPostApi(api_key="your_api_key")
```

> **Note:** You can obtain your API key from your business account at [Nova Poshta Business Cabinet](https://new.novaposhta.ua/).

### Address API

```python
from nova_post.models.address import GetCitiesRequest

request_data = GetCitiesRequest(FindByString="Київ", Limit=5)
cities = api.address.get_cities(request_data)
print(cities)
```

### Shipment Tracking

```python
from nova_post.models.tracking import TrackingRequest

tracking_request = TrackingRequest(DocumentNumber="20400048799000")
tracking_info = api.tracking.track_parcel(tracking_request)
print(tracking_info)
```

### Creating a Waybill (Internet Document)

```python
from nova_post.models.internet_document import SaveInternetDocumentRequest

request = SaveInternetDocumentRequest(
    PayerType="Sender",
    PaymentMethod="Cash",
    DateTime="2025-03-18",
    CargoType="Cargo",
    Weight=5.0,
    ServiceType="WarehouseWarehouse",
    SeatsAmount=1,
    Description="Test Cargo",
    Cost=500,
    CitySender="sender_city_ref",
    Sender="sender_ref",
    SenderAddress="sender_address_ref",
    ContactSender="contact_sender_ref",
    SendersPhone="contact_sender_phone",
    CityRecipient="recipient_city_ref",
    Recipient="recipient_ref",
    RecipientAddress="recipient_address_ref",
    ContactRecipient="contact_recipient_ref",
    RecipientsPhone="contact_recipient_phone"
)

document = api.internet_document.save_internet_document(request)
print(document)
```

> **Note:** To determine `Sender`, `Recipient`, and their parameters (`ref`, `address`, etc.), use the `counterparty` adapter.

> **Documentation:** All adapters follow the official Nova Poshta API documentation: [Nova Poshta API Documentation](https://developers.novaposhta.ua/documentation).

> **Issues:** Report bugs or suggest features at [GitHub Issues](https://github.com/TrippyFrenemy/nova_post/issues).

## Error Handling

Nova\_Post raises `NovaPostApiError` when the API returns an error or when a request fails due to timeouts or invalid responses. Example:

```python
from nova_post.exceptions import NovaPostApiError

try:
    tracking_info = api.tracking.track_parcel(tracking_request)
    print(tracking_info)
except NovaPostApiError as e:
    print(f"API error occurred: {e}")
```

## Logging

Nova\_Post includes logging for API requests and responses. By default, logs are sent to the standard output. You can configure logging in `logger.py` to redirect logs to a file or another logging service:

```python
import logging
from nova_post.logger import logger

logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler("nova_post.log")
logger.addHandler(file_handler)
```

## Configuration

Nova\_Post supports optional configurations such as request timeouts and retries. These settings can be adjusted within the `NovaPostApi` class:

```python
api = NovaPostApi(api_key="your_api_key")
api.DEFAULT_TIMEOUT = 15  # Increase timeout to 15 seconds
```

## Supported Python Versions

Nova\_Post is compatible with Python 3.9 and above.

## Running Tests

To run unit and integration tests, use:

```sh
pytest tests/
```

## Environment Variables

The library uses an API key, which should be set as an environment variable:

```sh
export NOVA_POST_API_KEY="your_api_key"
```



## Planned Performance Improvements

To enhance performance, caching mechanisms will be introduced to store frequently used API responses (e.g., city directories and service lists). This will reduce redundant API calls and improve response times. Additional optimizations include connection pooling for HTTP requests.



## Contributing

1. Fork the repository.
2. Create a feature branch (`git checkout -b feature-name`).
3. Commit your changes (`git commit -m 'Add new feature'`).
4. Push to the branch (`git push origin feature-name`).
5. Open a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

