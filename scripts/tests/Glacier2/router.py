# -*- coding: utf-8 -*-
# **********************************************************************
#
# Copyright (c) 2003-2017 ZeroC, Inc. All rights reserved.
#
# This copy of Ice is licensed to you under the terms described in the
# ICE_LICENSE file included in this distribution.
#
# **********************************************************************

passwords = {
    "userid": "abc123",
    "userid-0": "abc123",
    "userid-1": "abc123",
    "userid-2": "abc123",
    "userid-3": "abc123",
    "userid-4": "abc123"
}

routerProps = {
   "Ice.Warn.Dispatch" : "0",
   "Ice.Warn.Connections" : "0",
   "Glacier2.Filter.Category.Accept" : "c1 c2",
   "Glacier2.Filter.Category.AcceptUser" : "2",
   "Glacier2.SessionTimeout" : "30",
}

def buffered(enabled):
    return { "Glacier2.Client.Buffered": enabled, "Glacier2.Server.Buffered": enabled }

Glacier2TestSuite(__name__, routerProps, [
                  ClientServerTestCase(name="client/server with router in unbuffered mode",
                                       servers=[Glacier2Router(passwords=passwords, props=buffered(False)), Server()],
                                       client=Client(args=["--shutdown"])),
                  ClientServerTestCase(name="client/server with router in buffered mode",
                                       servers=[Glacier2Router(passwords=passwords, props=buffered(True)), Server()],
                                       clients=[Client(), Client(args=["--shutdown"])])])

