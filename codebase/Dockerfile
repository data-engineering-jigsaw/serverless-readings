FROM public.ecr.aws/lambda/python:3.9-arm64

COPY ./src/requirements.txt ./
RUN pip3 install -r requirements.txt
COPY ./src/main.py ./

CMD ["main.lambda_handler"]
