# registry_py
Automatic class registry system for Python

## Development

* Install poetry [https://python-poetry.org/]
* Install pre-commit [https://pre-commit.com/]
* Install dependencies
  `poetry install`
* Install git hooks
  `pre-commit install`

## Usage

Define a registry by extending from `Registry` class. You must define class variable called `REGISTER_NAME` in the registry class.

```python
from registry_py import Registry


class ChannelRegistry(Registry):
    REGISTRY_NAME = "Channel-Registry"
```

Define the base class. It can be an abstract base class or a regular class depending on your use case. This class should extend from the `Registrable` class. It should point to the previously defined Registry class and also it should define a class variable called `REGISTRY_RECORD_ID` that would be the ID that will be used to register child classes. For example in the following code only child classes that has `CHANNEL_ID` will be registered in the registry.

```python
from registry_py import Registrable


class BaseChannel(Registrable, abc.ABC):
    REGISTRY = ChannelRegistry
    REGISTRY_RECORD_ID = "CHANNEL_ID"
```

Once a child class or the base class is imported all child classes will be automatically registered in the registry. Get a child class using it'd ID.

```python
class EmailChannel(BaseChannel):
    CHANNEL_ID = 1

    def send(self):
        print("emailing")


class SMSChannel(BaseChannel):
    CHANNEL_ID = 2

    def send(self):
        print("texting")


email_channel = BaseChannel.REGISTRY.get_by_id(1)
```

Get all child classes.

```python
all_channels = BaseChannel.REGISTRY.get_all_classes()
```
