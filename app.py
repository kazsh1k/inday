import streamlit as st
from sqlalchemy import text, create_engine
import pandas as pd

list_doctor = ['', 'dr. Nurita', 'dr. Yogi', 'dr. Wibowo', 'dr. Ulama', 'dr. Ping']
list_symptom = ['', 'male', 'female']

DB_CONNECTION_STRING = 'postgresql://kashikogaming:p1BLaQZfwG0d@ep-orange-poetry-84084177.ap-southeast-1.aws.neon.tech/Milky%20Way'

engine = create_engine(DB_CONNECTION_STRING)

with engine.connect() as conn:
    conn.execute('CREATE TABLE IF NOT EXISTS SCHEDULE (id serial, doctor_name varchar, patient_name varchar, gender char(25), \
                                                       symptom text, handphone varchar, address text, waktu time, tanggal date);')

st.header('SIMPLE HOSPITAL DATA MANAGEMENT SYS')
page = st.sidebar.selectbox("Pilih Menu", ["View Data", "Edit Data"])

if page == "View Data":
    with engine.connect() as conn:
        data = pd.read_sql('SELECT * FROM schedule ORDER BY id;', conn)
        st.dataframe(data)

if page == "Edit Data":
    if st.button('Tambah Data'):
        with engine.connect() as conn:
            conn.execute('INSERT INTO schedule (doctor_name, patient_name, gender, symptom, handphone, address, waktu, tanggal) \
                          VALUES (%s, %s, %s, %s, %s, %s, %s, %s);', ('', '', '', '[]', '', '', None, None))
        st.experimental_rerun()

    with engine.connect() as conn:
        data = pd.read_sql('SELECT * FROM schedule ORDER BY id;', conn)

    for _, result in data.iterrows():
        # Remaining code for update and delete
        # Ensure the update and delete operations are handled properly
        # ...
