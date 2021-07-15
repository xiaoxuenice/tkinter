# -*- mode: python ; coding: utf-8 -*-
import SSH
def shell(exec,Ip):
    return SSH.sssh(exec,Ip)
def active(Ip):
    return SSH.active(Ip)
