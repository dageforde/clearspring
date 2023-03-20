import psycopg2
import pandas as pd
from datetime import date

# Establish connection to db with psycopg and query for required data
conn = psycopg2.connect(dbname='',
                        user='', password='',
                        host='')
cur = conn.cursor()

query = '''SELECT MEDICAID_ID,MEMBER_FIRST_NAME,MEMBER_LAST_NAME,DOB,ELIGIBILITY_START_DATE,ELIGIBILITY_END_DATE
           FROM TABLE'''
cur.execute(query)

#store query results in a dataframe object
df = pd.DataFrame(cur.fetchall(), columns=['MEDICAID_ID','MEMBER_FIRST_NAME','MEMBER_LAST_NAME','DOB','ELIGIBILITY_START_DATE','ELIGIBILITY_END_DATE'])

#perform transformations on text fields
df[['MEDICAID_ID','MEMBER_FIRST_NAME','MEMBER_LAST_NAME']] = df[['MEDICAID_ID','MEMBER_FIRST_NAME','MEMBER_LAST_NAME']].str.upper()
df['MEDICAID_ID'] = '"' + df.MEDICAID_ID + '"'
df['MEMBER_FIRST_NAME'] = '"' + df.MEMBER_FIRST_NAME + '"'
df['MEMBER_LAST_NAME'] = '"' + df.MEMBER_LAST_NAME + '"'

# name file using today's date and write to file system
today = date.today()
filename = 'TEST_Request_'+today+'.csv'
df.to_csv(filename,index=False)