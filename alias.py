#!/usr/bin/env python

import interp

class Alias(object):
    '''
    Addition: alias needs a name and help function
    '''
    def __init__(self, hash, cmd):
        self.name = 'alias?'
        self.help = cmd
        self.hash = hash
        self.cmd = cmd.strip('"')
        self.shell = interp.Interpretor(self.hash.master)
    def process(self, argv):
        if argv[1:]:
            args = tuple(argv[1:])
        else:
            args = ''

        if args:
            try:
                cmd = self.cmd % args
            except Exception, e:
                print e
        else:
            cmd = self.cmd

        self.shell.send( '%s\n' % cmd )
