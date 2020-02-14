FROM python:3.8.1
WORKDIR /app

COPY requirements.txt /app
RUN pip install --upgrade pip wheel setuptools && \
    pip install -r requirements.txt && \
    printf '%70s\n' | tr ' ' -

COPY . /app
COPY ./vendors/* /usr/local/bin/
RUN touch /tmp/myroute_lkh.sol && chmod 777 /tmp/myroute_lkh.sol && \
    touch /tmp/routes_cache && chmod -R 777 /tmp/

EXPOSE 8888

ENTRYPOINT ["jupyter",  "notebook", "--ip=0.0.0.0", "--port=8888", "--allow-root"]
