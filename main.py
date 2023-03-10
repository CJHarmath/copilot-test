# GitHub CoPilot generated code based on the below comments:
#
#
# write a command line tool which has an option to add students and asks for name and age
# and then prints the name and age of the student
# also allows selecting students and edit or delete them
# as well as filtering students by age
# and finally printing all students

import click
import json

@click.group()
def cli():
    pass

@cli.command()
@click.option('--name', prompt='Name', help='The name of the student.')
@click.option('--age', prompt='Age', help='The age of the student.')
def add(name, age):
    with open('students.json', 'r') as f:
        students = json.load(f)
        students.append({'name': name, 'age': age})
    with open('students.json', 'w') as f:
        json.dump(students, f)

@cli.command()
def list():
    with open('students.json', 'r') as f:
        students = json.load(f)
        for student in students:
            print(student)

@cli.command()
@click.option('--name', prompt='Name', help='The name of the student.')
def select(name):
    with open('students.json', 'r') as f:
        students = json.load(f)
        for student in students:
            if student['name'] == name:
                print(student)
                
@cli.command()
@click.option('--name', prompt='Name', help='The name of the student.')
@click.option('--age', prompt='Age', help='The age of the student.')
def edit(name, age):
    with open('students.json', 'r') as f:
        students = json.load(f)
        for student in students:
            if student['name'] == name:
                student['age'] = age
    with open('students.json', 'w') as f:
        json.dump(students, f)

@cli.command()
@click.option('--name', prompt='Name', help='The name of the student.')
def delete(name):
    with open('students.json', 'r') as f:
        students = json.load(f)
        for student in students:
            if student['name'] == name:
                students.remove(student)
    with open('students.json', 'w') as f:
        json.dump(students, f)

@cli.command()
@click.option('--age', prompt='Age', help='The age of the student.')
def filter(age):
    with open('students.json', 'r') as f:
        students = json.load(f)
        for student in students:
            if student['age'] == age:
                print(student)

if __name__ == '__main__':
    cli()

