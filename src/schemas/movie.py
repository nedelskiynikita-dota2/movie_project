from datetime import date

from pydantic import BaseModel, Field, ConfigDict, field_validator


class MovieBase(BaseModel):
    title: str = Field(min_length=2, max_length=200)
    genre: str = Field(min_length=2, max_length=100)
    rating: float = Field(ge=0, le=10)
    year: int

    @field_validator("year")
    @classmethod
    def if_year_in_range(cls, year: int) -> int:
        if not (1888 <= year <= date.today().year):
            raise ValueError(
                f"Год должен быть между 1888 и {date.today().year}"
            )
        return year


class MovieCreate(MovieBase):
    pass


class MovieUpdate(BaseModel):
    title: str | None = Field(default=None, min_length=2, max_length=200)
    genre: str | None = Field(default=None, min_length=2, max_length=100)
    rating: float | None = Field(default=None, ge=0, le=10)
    year: int | None = None

    @field_validator("year")
    @classmethod
    def if_year_in_range(cls, year: int | None) -> int | None:
        if year is None:
            raise ValueError("Год не может быть пустым")
        if not (1888 <= year <= date.today().year):
            raise ValueError(
                f"Год должен быть между 1888 и {date.today().year}"
            )
        return year


class MovieOut(MovieBase):
    id: int
    model_config = ConfigDict(from_attributes=True)
