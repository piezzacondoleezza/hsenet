FROM python:3.8

WORKDIR /dir
COPY . .

RUN apt-get update && apt-get install -y iputils-ping
RUN pip3 install argparse
CMD ["./script.py", "--host=ya.ru"]
