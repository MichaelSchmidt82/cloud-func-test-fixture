FROM python:3

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

#* install latest googleapiclient and google storage libraries.
RUN python -m pip install git+https://github.com/googleapis/google-api-python-client.git
RUN python -m pip install git+https://github.com/googleapis/python-storage.git

ENV GOOGLE_APPLICATION_CREDENTIALS="credentials.json"

#* Specify the cloud function URL
ENV FUNCTION_URL="https://*.cloudfunctions.net/"

ENV PROJECT_ID=""
ENV LOCATION=""
ENV DATASET_ID=""

ENV SERVICE_NAME=""
ENV API_VERSION="v1beta1"

COPY . .
CMD [ "python", "./entrypoint.py" ]
