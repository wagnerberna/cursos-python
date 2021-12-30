try:
    from mysql import connector  # noqa
except ModuleNotFoundError:
    print("MySQL Connector não instalado!")
else:
    print("MySQL Connector instalado e pronto para ser usado!")
