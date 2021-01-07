from abc import ABC, abstractmethod
from typing import List


class DataSourceAbstract(ABC):

    @abstractmethod
    def get(self, *args, **kwargs) -> List[list]:
        raise NotImplementedError
