<!--
https://readme42.com
-->


[![](https://img.shields.io/pypi/v/kill.svg?maxAge=3600)](https://pypi.org/project/kill/)
[![](https://img.shields.io/badge/License-Unlicense-blue.svg?longCache=True)](https://unlicense.org/)
[![](https://github.com/andrewp-as-is/kill.py/workflows/tests42/badge.svg)](https://github.com/andrewp-as-is/kill.py/actions)

### Installation
```bash
$ [sudo] pip install kill
```

#### Examples
```python
>>> kill.kill(61024)
>>> kill.kill([61076])
```

errors
```python
>>> kill.kill(9999999)
kill: 999999: No such process

>>> kill.kill(1)
kill: (1) - Operation not permitted
```

<p align="center">
    <a href="https://readme42.com/">readme42.com</a>
</p>