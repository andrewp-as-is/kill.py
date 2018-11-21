#!/usr/bin/env python
import kill

err = kill.kill(1)
print(err)

err = kill.kill(9999999)
print(err)
