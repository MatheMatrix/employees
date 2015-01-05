import datetime
import logging

from cliff.command import Command
from employee import main
from employee import summary


employees = main.employees


class Update(Command):
    "Update an employee."

    log = logging.getLogger(__name__)

    def get_parser(self, prog_name):
        parser = super(Update, self).get_parser(prog_name)
        parser.add_argument('id', nargs="?")
        parser.add_argument('attr', nargs="?")
        parser.add_argument('value', nargs="?")
        return parser

    def take_action(self, parsed_args):
        employee = employees.get(parsed_args.id)
        if employee is None:
            print "No this employee"
            return
        elif parsed_args.attr not in employee.attrs:
            print "No such attr"
            return
        elif parsed_args.attr == "id":
            if parsed_args.value in employees.keys():
                print "ID already exists"
                return
            else:
                origin_id = employee.id
                setattr(employee, parsed_args.attr, parsed_args.value)
                employees[parsed_args.value] = employee
                employees.pop(origin_id)
        elif parsed_args.attr == "birth":
            birth = parsed_args.value.split('.')
            birth = datetime.date(*map(lambda x:int(x), birth))
            setattr(employee, parsed_args.attr, birth)
        else:
            setattr(employee, parsed_args.attr, parsed_args.value)

        print "Updated successfully"