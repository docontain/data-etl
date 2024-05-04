import mysql.connector
import pandas as pd
from sqlalchemy import create_engine


def extract():
    conn = mysql.connector.connect(
        host="db", user="root", password="password", database="source_db"
    )
    query = "SELECT * FROM source_table"
    df = pd.read_sql(query, conn)
    conn.close()
    return df


def transform(df):
    df["new_column"] = df["existing_column"] * 2
    return df


def load(df):
    engine = create_engine("postgresql://postgres:password@db:5432/target_db")
    df.to_sql("target_table", engine, if_exists="replace", index=False)


if __name__ == "__main__":
    data = extract()
    transformed_data = transform(data)
    load(transformed_data)
