FROM python:3

WORKDIR /TRABALHO_FINAL

COPY . .

CMD [ "python", "TRABALHO_FINAL/Agendador.py"]
