docker run -d \
  --name oracle-23-ai \
  -p 1521:1521 \
  -v oracle_volume:/opt/oracle/oradata \
  container-registry.oracle.com/database/free:latest-lite