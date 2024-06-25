A simple Redis-based caching system for managing unique account names.
Overview
This project implements a caching mechanism using Redis to store and check for the existence of unique account names. It provides an efficient way to maintain a set of unique names and perform quick lookups.
Features

Store new account names
Check if an account name already exists
Utilize Redis for fast in-memory operations

Requirements

Python 3.x
Redis server
redis-py library

Installation

Ensure you have Python 3.x installed on your system.
Install Redis server on your local machine or have access to a Redis instance.
Install the required Python library:
pip install redis
Clone this repository or download the source code.

Usage

Import the Redis class from Database.py:
from Database import Redis
Create an instance of the Redis class:
redis_cache = Redis()
Add a new account name:
redis_cache.set("John Doe")
Check if an account name exists:
exists = redis_cache.if_exists("John Doe")
print(exists)  # True or False

Configuration
By default, the Redis connection is configured to connect to localhost on port 6379. If you need to modify these settings, update the init method in the Redis class.
Contributing
Contributions are welcome! Please feel free to submit a Pull Request.
