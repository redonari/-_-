#лаб 3 и 5 184ae3c30bb74bb49c067c415202b8e24e9ce8831cf7d5ac0d8de7c8656c0176

from dataclasses import dataclass
from enum import Enum
from typing import Callable, Generic, TypeVar, Union

T = TypeVar("T")
E = TypeVar("E")


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
class Success(Generic[T]):
    value: T


@dataclass(frozen=True)
class Failure(Generic[E]):
    error: E


Result = Union[Success[T], Failure[E]]


def user_source() -> list[User]:
    return [
        User("Egor", 21, "Egor@cos.ru"),
        User("Lada", 20, "Lada@sin.ru"),
    ]


def load_users(error_message: str) -> Callable[
    [Callable[[], list[User]]], Callable[[], Result[list[User], str]]
]:
    def with_source(
        source: Callable[[], list[User]],
    ) -> Callable[[], Result[list[User], str]]:
        def run() -> Result[list[User], str]:
            users = source()
            return Success(users) if users else Failure(error_message)

        return run

    return with_source


if __name__ == "__main__":
    prepare_load = load_users("Список пользователей пуст")
    task = prepare_load(user_source)
    result = task()

    match result:
        case Success(value):
            print("Пользователи:", value)
        case Failure(error):
            print("Ошибка:", error)
