import logging

from cliff.command import Command
from employee import main
from employee import summary


employees = main.employees


class Delete(Command):
    "Delete an employee."

    log = logging.getLogger(__name__)

    def get_parser(self, prog_name):
        parser = super(Delete, self).get_parser(prog_name)
        parser.add_argument('id', nargs="?")
        return parser

    def take_action(self, parsed_args):
        employee = employees.get(parsed_args.id)
        if employee is None:
            print "No this employee"
        else:
            employees.pop(parsed_args.id)
            print "Deleted successfully"