cat name.py 
import logging
import sys
from cliff.command import Command


#class Name(Command):
 #   "A simple command that prints a message."

  #  log = logging.getLogger(__name__)

   # def take_action(self, parsed_args):
       # self.log.info('suraj patil')
       # self.log.debug('debugging')
        #self.app.stdout.write('hi!\n')

# class First(Command):
#     "A simple command that prints a message."

#     log = logging.getLogger(__name__)

#     def take_action(self, parsed_args):
#         self.log.info('suraj')
#         #name = input("What's your name? ")
#         #print(name)
#         self.log.debug('debugging')
#         #self.app.stdout.write('hi!\n')

# class Last(Command):
#     "A simple command that prints a message."

#     log = logging.getLogger(__name__)

#     def take_action(self, parsed_args):
#         self.log.info('patil')
#         self.log.debug('debugging')
#         #self.app.stdout.write('hi!\n')



class Name(Command):

    def get_parser(self, parsed_args):
        parser = super(Name, self).get_parser(parsed_args)
        group = parser.add_mutually_exclusive_group()

        group.add_argument(
            '--firstname',
            help = 'print first name',
        )

        group.add_argument(
            '--lastname',
            help = 'print last name',
        )

        group.add_argument(
            '--fullname',
            help = 'print name',
        )

        return parser

    def take_action(self, parsed_args):
         
            if parsed_args.firstname:
                if ' ' in sys.argv[3]:
                    raise Exception('No space in first name please') 
                self.app.stdout.write(sys.argv[3])
            
            elif parsed_args.lastname:
                if ' ' in sys.argv[3]:
                    last_name = sys.argv[3]
                    print(last_name.split()[1])
                else:
                    self.app.stdout.write(sys.argv[3].split()[0])
            elif parsed_args.fullname:
                self.app.stdout.write(sys.argv[3])

