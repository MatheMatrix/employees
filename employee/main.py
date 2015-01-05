import cPickle as pickle
import datetime
import logging
import prettytable
import sys

from cliff.app import App
from cliff.commandmanager import CommandManager


global employees
employees = {}


class Employee(object):
    """Data structure for employee

    Data: id, name, sex, birth, education, job, tel, addr
    """

    attrs = ["id", "name", "sex", "birth", "edu", "job", "tel", "addr"]

    def __init__(self, *args, **kwargs):
        for attr in self.attrs:
            if attr is "birth":
                birth = kwargs.get("birth").split('.')
                self.birth = datetime.date(*map(lambda x:int(x), birth))
            else:
                setattr(self, attr, kwargs.get(attr))
        
    def show(self):
        output = prettytable.PrettyTable(['attr', 'value'])
        for attr in self.attrs:
            output.add_row([attr, getattr(self, attr)])
        print output

class Manager(App):

    log = logging.getLogger(__name__)

    def __init__(self):
        super(Manager, self).__init__(
            description='simple employee system for course design',
            version='0.1',
            command_manager=CommandManager('employee.manager'),
            )

    def initialize_app(self, argv):
        self.log.debug('initialize_app')
        try:
            employees.update(pickle.load(open("data.dat", "r")))
        except IOError:
            self.log.info("It seems you use this app the first time, welcome!")
        print("If you want to add a birthday, please input like "
                "%Y.%m.%d (eg. 1994.10.5)")

    def prepare_to_run_command(self, cmd):
        self.log.debug('prepare_to_run_command %s', cmd.__class__.__name__)

    def clean_up(self, cmd, result, err):
        self.log.debug('clean_up %s', cmd.__class__.__name__)
        pickle.dump(employees, open("data.dat", "w"))


def main(argv=sys.argv[1:]):
    app = Manager()
    return app.run(argv)


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
