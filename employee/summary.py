import logging
import prettytable

from cliff.command import Command
from employee import main


employees = main.employees


class Summary(Command):
    """Show a list of employees.

    The name name and id are printed by default.
    """

    log = logging.getLogger(__name__)

    def take_action(self, parsed_args):
        if len(employees) is 0:
            self.log.info("No employees")
        else:
            output = prettytable.PrettyTable(['Name', 'ID'])
            for e in employees.values():
                output.add_row([e.name, e.id])
            print output