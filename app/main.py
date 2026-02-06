class Person:
    people = dict()

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    result = [
        Person(person.get("name"), person.get("age"))
        for person in people
    ]
    for i in range(len(result)):
        if people[i].get("husband") is not None:
            result[i].husband = result[i].people.get(people[i].get("husband"))
        if people[i].get("wife") is not None:
            result[i].wife = result[i].people.get(people[i].get("wife"))
    return result
