from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from redis_om import get_redis_connection ,HashModel



app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['http://localhost:3000'],
    allow_methods=['*'],
    allow_headers=['*'],

)

#THIS WILL BE DIFFERENT FOR EVERY MICEOSERVICES
redis=get_redis_connection(
    host="redis-12990.c293.eu-central-1-1.ec2.cloud.redislabs.com",
    port=12990,
    password="hSVysForn2HVS0pUYWlciRZwrZjl8AhM",
    decode_responses=True
)
