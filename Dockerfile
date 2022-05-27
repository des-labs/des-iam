FROM oraclelinux:7-slim as oracle

RUN  curl -o /etc/yum.repos.d/public-yum-ol7.repo https://yum.oracle.com/public-yum-ol7.repo && \
     yum-config-manager --enable ol7_oracle_instantclient && \
     yum -y install oracle-instantclient18.3-basic

FROM ubuntu:20.04

# ORACLE DB Client installation (https://oracle.github.io/odpi/doc/installation.html#oracle-instant-client-zip)
ENV PATH=$PATH:/usr/lib/oracle/18.3/client64/bin
ENV LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/usr/lib/oracle/18.3/client64/lib:/usr/lib
COPY --from=oracle /usr/lib/oracle/ /usr/lib/oracle
COPY --from=oracle /lib64/libaio.so.1 /usr/lib

RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y \
  python3-pip         \
  libaio1             \
  python-is-python3   \
  && rm -rf /var/lib/apt/lists/*


RUN useradd --create-home --shell /bin/bash worker --uid 1000
USER worker
WORKDIR /home/worker
ENV PATH="/home/worker/.local/bin:${PATH}"

COPY --chown=worker:worker requirements.txt requirements.txt
RUN pip install --user -r requirements.txt

COPY --chown=worker:worker ./ des_iam/
WORKDIR /home/worker/des_iam

USER root
RUN mkdir /static && chown 1000:1000 /static
USER worker


