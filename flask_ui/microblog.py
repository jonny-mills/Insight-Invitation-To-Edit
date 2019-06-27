#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
File to run the app
"""

from app import app

if __name__ == "__main__":
    app.run(port="80", host="0.0.0.0")
