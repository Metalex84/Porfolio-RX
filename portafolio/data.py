import json
from typing import List

from pydantic import BaseModel


class Media(BaseModel):
    email: str = ""
    cv: str = ""
    github: str = ""
    likedin: str = ""


class Technology(BaseModel):
    icon: str = ""
    name: str = ""


class Info(BaseModel):
    icon: str = ""
    title: str = ""
    subtitle: str = ""
    description: str = ""
    date: str = ""
    certificate: str = ""
    technologies: List[Technology] = []
    image: str = ""
    url: str = ""
    github: str = ""


class Extra(BaseModel):
    image: str = ""
    title: str = ""
    description: str = ""
    url: str = ""


class Data(BaseModel):
    title: str = ""
    description: str = ""
    image: str = ""
    avatar: str = ""
    name: str = ""
    skill: str = ""
    location: str = ""
    media: Media = Media()
    about: str = ""
    technologies: List[Technology] = []
    experience: List[Info] = []
    projects: List[Info] = []
    training: List[Info] = []
    #extras: List[Extra] = []


with open("assets/data/data.json") as file:
    json_data = json.load(file)

data = Data(**json_data)
