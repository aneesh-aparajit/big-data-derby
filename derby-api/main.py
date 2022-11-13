import numpy as np
import pandas as pd
import sklearn as skl

from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI(title='Big Data Derby, 2022')


class Input(BaseModel):
    track_id: str
    race_number: int
    program_number: str
    trakus_index: int 
    latitude: float 
    longitude: float 
    distance_id: int 
    course_type: str
    race_type: str
    jockey: str
    day_of_race: str
    track_conditon: str
    run_up_distance: int 
    post_time: int 
    weight_carried: int 
    year: int 
    month: int 
    day: int 
    odds: int 


@app.get('/predict/', tags=['Prediction End Point'], response_model=Input)
def predict(inputs: Input):
    '''This method is the api end point for the prediction.'''
    return {
        'hellow': 'world'
    } 
    
