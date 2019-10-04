from cliff.command import Command

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
            self.app.stdout.write(str(str(parsed_args.firstname).split()[0]))
        
        elif parsed_args.lastname:
            # last_name = sys.argv[4:\\]
            if ' ' in str(parsed_args.lastname):
                self.app.stdout.write(str(parsed_args.lastname).split()[-1])
            else:
                self.app.stdout.write(str(parsed_args.lastname)[:-2])
        elif parsed_args.fullname:
            self.app.stdout.write(str(parsed_args.fullname))

