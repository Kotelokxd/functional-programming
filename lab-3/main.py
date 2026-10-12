from enum import Enum
from dataclasses import dataclass
from typing import Union


class LoadState(Enum):
    LOADING = "loading"
    SUCCESS = "success"
    ERROR = "error"


@dataclass(frozen=True)
class User:
    name: str
    age: int
    email: str


@dataclass(frozen=True)
class Success:
    value: list[User]


@dataclass(frozen=True)
class Failure:
    error: str


def load_users(users: list[User]) -> Union[Success, Failure]:
    return (
        Success(users)
        if users
        else Failure("Список пользователей пуст")
    )


print(load_users([
    User("Анна", 25, "anna@example.com"),
    User("Иван", 30, "ivan@example.com")
]))
