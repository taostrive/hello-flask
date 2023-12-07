FROM python:3.9-slim

ARG APPDIR=/project

# Create runtime user and group but not using root
RUN groupadd --gid 3000 flask \
    && useradd -u 3000 -g flask -s /bin/bash -m -d ${APPDIR} myflask 

RUN chown 3000:3000 ${APPDIR}

WORKDIR ${APPDIR}

USER 3000

#RUN pip install pipenv
#RUN export PATH="$PATH:"${APPDIR}/.local/bin; echo $PATH
#RUN pipenv install --deploy

COPY . .

RUN pip install -r requirements.txt

EXPOSE 5001

CMD ["python", "app.py"]