import logging
import prettytable

from cliff.command import Command
from employee import main
from employee import summary


employees = main.employees


class Sort(Command):
    "Sort employees by an attr."

    log = logging.getLogger(__name__)

    def get_parser(self, prog_name):
        parser = super(Sort, self).get_parser(prog_name)
        parser.add_argument('attr', nargs="?")
        return parser

    def take_action(self, parsed_args):
        if parsed_args.attr not in main.Employee.attrs:
            print "No such attr"
            return
        result = sorted(employees.values(),
            key=lambda e:getattr(e, parsed_args.attr))
        
        if parsed_args.attr in ['name', 'id']:
            output = prettytable.PrettyTable(['Name', 'ID'])
            for e in result:
                output.add_row([e.name, e.id])
        else:
            output = prettytable.PrettyTable(['Name', 'ID',
                '%s' % parsed_args.attr])
            for e in result:
                output.add_row([e.name, e.id, getattr(e, parsed_args.attr)])
        print output