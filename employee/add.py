import cPickle as pickle
import random
import logging
import uuid

from cliff.command import Command
from datetime import date
from employee import main


employees = main.employees


class Add(Command):
    "Add an employee."

    log = logging.getLogger(__name__)
    names = ["Liuyi", "Chener", "Zhangsan", "Lisi", "Wangwu", "Zhaoliu",
             "Sunqi", "Zhouba", "Wujiu", "Zhengshi"]
    sexs = ["man", "woman"]
    edus = ["bachelor", "master", "doctor"]
    jobs = ["intern", "enginner", "senior enginner", "principle enginner",
            "product manager", "project manager", "designer", "staff"]

    def get_parser(self, prog_name):
        parser = super(Add, self).get_parser(prog_name)
        parser.add_argument('id', nargs='?', default=str(uuid.uuid4()))
        parser.add_argument('name', nargs='?',
            default=random.choice(self.names))
        parser.add_argument('sex', nargs='?',
            default=random.choice(self.sexs))
        parser.add_argument('birth', nargs='?', default=date.strftime(
            date.today(), '%Y.%m.%d'))
        parser.add_argument('edu', nargs='?',
            default=random.choice(self.edus))
        parser.add_argument('job', nargs='?',
            default=random.choice(self.jobs))
        parser.add_argument('tel', nargs='?', 
            default=random.randint(10000000, 99999999))
        parser.add_argument('addr', nargs='?', 
            default=random.randint(100000, 999999))
        return parser

    def take_action(self, parsed_args):
        if parsed_args.id is "?":
            parsed_args.id = str(uuid.uuid4())
        new_employee = main.Employee(id=parsed_args.id,
                                     name=parsed_args.name,
                                     sex=parsed_args.sex,
                                     birth=parsed_args.birth,
                                     edu=parsed_args.edu,
                                     job=parsed_args.job,
                                     tel=parsed_args.tel,
                                     addr=parsed_args.addr)
        new_employee.show()
        employees[parsed_args.id] = new_employee
        pickle.dump(employees, open("data.dat", "w"))
        self.log.info("New employee added, whose id is %s" % new_employee.id)