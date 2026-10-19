from enum import Enum
from dataclasses import dataclass


class PetrovLoadState(Enum):
    LOADING = "loading"
    SUCCESS = "success"
    ERROR = "error"


@dataclass(frozen=True)
class User:
    name: str
    age: int
    email: str


@dataclass(frozen=True)
class Success[T]:
    value: T


@dataclass(frozen=True)
class Failure[E]:
    error: E


type Result[T, E] = Success[T] | Failure[E]


def petrov_load_users(users: list[User]) -> Result[list[User], str]:
    return {
        True: lambda: Success(users),
        False: lambda: Failure("Список пользователей пуст"),
    }[bool(users)]()


print(petrov_load_users([
    User("Анна", 25, "anna@example.com"),
    User("Иван", 30, "ivan@example.com")
]))
