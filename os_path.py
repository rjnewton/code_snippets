#!/usr/bin/python
# -*- coding:utf-8 -*-
import sys
import os

print (f"file: {__file__}");

rpath = os.path.realpath(__file__)
print (f"realpath of file: {rpath}")

ppath = os.path.dirname(os.path.realpath(__file__))
print (f"parent directory: {ppath}")

# Pic and lib dirs are one level up

picdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'pic')
print (f"picdir: {picdir}")

libdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'lib')
print (f"libdir: {libdir}")

#if os.path.exists(libdir):
#    sys.path.append(libdir)


