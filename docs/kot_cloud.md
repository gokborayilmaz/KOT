---
layout: default
title: KOT CLOUD
nav_order: 23
has_children: True
---

# KOT Cloud | [![Cloud Test Every - 15 Minute](https://github.com/KOT/KOT/actions/workflows/cloud_test.yml/badge.svg)](https://github.com/KOT/KOT/actions/workflows/cloud_test.yml)
KOT Cloud: the ultimate, free cloud database for all Python developers. Experience reliability, efficiency, and top-notch security in one powerful solution. Start your seamless development journey with KOT Cloud today!

“Save your Python Things to the Cloud: Code Unrestricted, Scale Limitless with KOT Cloud!”



## Enable the cloud connection in your Python
```console
KOT cloud_key
```

> cloud-HWP0iUIvUlFd18acOgrNa6UmLx6yua

```python
from kot import KOT_Cloud

cloud = KOT_Cloud("YOUR_CLOUD_KEY")
```

## Sending


```python
#FUNCTION
@cloud.active
def remove_lines(string):
    return string.replace("\n","")

#CLASS
@cloud.active
class human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

#VARIABLE
price = 15.2
cloud.set("price", price)
```


## Getting

```python
#FUNCTION
cloud.get("remove_lines")("Hi,\nhow are you")

#CLASS
cloud.get("human")("Onur", 100)

#VARIABLE
cloud.get("price")
```





# Cloud Pro | [![Cloud Pro Test Every - 15 Minute](https://github.com/KOT/KOT/actions/workflows/cloud_pro_test.yml/badge.svg)](https://github.com/KOT/KOT/actions/workflows/cloud_pro_test.yml)
In Cloud Pro you can create databases with name, for this use:

```console
KOT cloud_pro_key <YOUR_DATABASE_NAME>
```

Its will give like this:

> cloud-6xvX7p0jKlYpV6GpKjGR0xujXTfbpn-YOUR_DATABASE_NAME

and now you can use your access key.

```python
from kot import KOT_Cloud_Pro

cloud = KOT_Cloud_Pro("YOUR_CLOUD_PRO_KEY", "YOUR_ACCESS_KEY")
```


# Cloud Dedicated
When you got the dedicated cloud you will get admin and user password and dedicated key.

For admin account (set and delete operations):
```python
from kot import KOT_Cloud_Dedicated

cloud = KOT_Cloud_Dedicated("YOUR_DATABASE_NAME", "YOUR_ADMIN_PASSWORD", "YOUR_DEDICATED_KEY")
```

For user account (get operations):
```python
from kot import KOT_Cloud_Dedicated

cloud = KOT_Cloud_Dedicated("YOUR_DATABASE_NAME", "YOUR_USER_PASSWORD", "YOUR_DEDICATED_KEY")
```


# Encryption
You can give `encryption_key` to all functions, this will encrypt your things in your computer and after its send the encrypted version to KOT cloud.

```python
@cloud.active(encryption_key="")
...

cloud.set(..., encryption_key="")

cloud.get(..., encryption_key="")

```

or you can use global encryption

```python
cloud.force_encrypt = ""
```

You can use every string as an encryption key but also you can generate a verry strong encryption key in [here](https://docs.kot.co/features/encryption.html#fernet-key-generation)
