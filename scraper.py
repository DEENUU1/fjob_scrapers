from dataclasses import dataclass
from typing import List, Optional


@dataclass
class WorkType:
    name: Optional[str] = None


@dataclass
class EmploymentType:
    name: Optional[str] = None


@dataclass
class Experience:
    name: Optional[str] = None


@dataclass
class Salary:
    salary_from: Optional[float] = None
    salary_to: Optional[float] = None
    currency: Optional[str] = None
    schedule: Optional[str] = None


@dataclass
class Addresses:
    country: Optional[str] = None
    city: Optional[str] = None
    region: Optional[str] = None
    street: Optional[str] = None


@dataclass
class ParsedOffer:
    title: Optional[str] = None
    description: Optional[str] = None
    addresses: Optional[List[Addresses]] = None
    is_remote: Optional[bool] = False
    is_hybrid: Optional[bool] = False
    skills: Optional[str] = None
    salary: Optional[List[Salary]] = None
    experience: Optional[List[Experience]] = None
    work_type: Optional[List[WorkType]] = None
    employment_type: Optional[List[EmploymentType]] = None
    company_logo: Optional[str] = None
    url: Optional[str] = None
    company_name: Optional[str] = None

