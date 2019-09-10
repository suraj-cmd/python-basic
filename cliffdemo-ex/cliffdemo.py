import logging
import sys
from cliff.command import Command


class Name(Command):
    "A simple command that prints a message."

    log = logging.getLogger(__name__)

     def take_action(self, parsed_args):
        self.log.info('suraj patil')
        self.log.debug('debugging')
        #self.app.stdout.write('hi!\n')

class First(Command):
     "A simple command that prints a message."

     log = logging.getLogger(__name__)

     def take_action(self, parsed_args):
         self.log.info('suraj')
         #name = input("What's your name? ")
         #print(name)
         self.log.debug('debugging')
#         #self.app.stdout.write('hi!\n')

 class Last(Command):
     "A simple command that prints a message."

     log = logging.getLogger(__name__)

     def take_action(self, parsed_args):
         self.log.info('patil')
         self.log.debug('debugging')
#         #self.app.stdout.write('hi!\n')
