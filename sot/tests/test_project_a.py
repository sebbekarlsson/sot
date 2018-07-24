import os
from read_and_close import read_and_close
from sot.Project import Project


path = os.path.abspath(os.path.dirname(__file__) + '/project_a')
project = Project(path)


def test_output():
    print(path)
    assert project.transpile(read_and_close(
        os.path.join(path, project.config['main']))) ==\
        'HELLO WORLD'
