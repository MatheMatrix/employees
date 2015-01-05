import logging

from cliff.command import Command
from employee import main
from employee import summary


employees = main.employees


class Query(Command):
    "Query an employee."

    log = logging.getLogger(__name__)

    def get_parser(self, prog_name):
        parser = super(Query, self).get_parser(prog_name)
        parser.add_argument('attr', nargs="?")
        parser.add_argument('value', nargs="?")
        return parser

    def take_action(self, parsed_args):
        query_result = []
        if parsed_args.attr not in main.Employee.attrs:
            print "No such attr"
            return
        for e in employees.values():
            if parsed_args.value in str(getattr(e, parsed_args.attr)):
                query_result.append(e)
        print "query result:"
        for e in query_result:
            e.show()