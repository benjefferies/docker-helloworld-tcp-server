FROM python:3.7-slim-stretch AS base

COPY run.py /bin

CMD ["run.py"]