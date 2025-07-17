# export_votes.py

import pandas as pd
from sqlalchemy import create_engine

from app.core.config import settings


def main():
    DATABASE_URL = settings.get_database_url
    # 1) Conecta con la DB
    engine = create_engine(DATABASE_URL)

    # 2) Lee la tabla completa en un DataFrame
    df = pd.read_sql_table('burger_battle_votes_2025', con=engine)

    # 3) Guarda a CSV y/o a Excel
    df.to_csv('burger_battle_votes_2025.csv', index=False)
    print("CSV guardado como burger_battle_votes_2025.csv")

if __name__ == '__main__':
    main()
