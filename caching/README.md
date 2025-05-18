# Python Caching Systems

This project implements basic caching strategies using Python OOP and dictionary-based storage. Each cache class inherits from a common `BaseCaching` class and applies a different eviction policy when the cache limit is reached.

##Files

- `base_caching.py` – Base class with common cache behavior and MAX_ITEMS limit
- `0-basic_cache.py` – No eviction policy
- `1-fifo_cache.py` – First-In First-Out (FIFO)
- `2-lifo_cache.py` – Last-In First-Out (LIFO)
- `3-lru_cache.py` – Least Recently Used (LRU)
- `4-mru_cache.py` – Most Recently Used (MRU)

Test scripts: `0-main.py` to `4-main.py`

##Usage

Run any of the test scripts:

```bash
python3 3-main.py  # Test LRU
python3 4-main.py  # Test MRU