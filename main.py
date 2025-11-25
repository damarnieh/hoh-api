from fastapi import FastAPI, HTTPException
import pandas as pd
import psycopg2

# create FastAPI object
app = FastAPI()


def getConnection():
    # create connection
    conn = psycopg2.connect(
        dbname="neondb", user="neondb_owner", password="npg_sLfVg8iW4EwO",
        host="ep-steep-water-a102fmjl-pooler.ap-southeast-1.aws.neon.tech",
    )

    return conn


# @app.get('/')
# async def getWelcome():
#     return {
#         "msg": "sample-fastapi-pg"
#     }


@app.get('/')
def narutoMakan():
    return{
        "msg" : "naruto-makan-ramen"
    }

# endpoint untuk menampilkan data dari csv
@app.get('/sasuke')
def sasukeKentut():
        # membaca data csv
        df = pd.read_csv('data.csv')

        # response
        return df.to_dict(orient="records")


@app.get('/sasuke/{lokasi}')
def sasukeKentut(lokasi: str):
        # membaca data csv
        df = pd.read_csv('data.csv')

        #filter
        hachu = df.loc[df.lokasi == lokasi]

        # jika data kosong -> result 404
        if hachu.shape[0] == 0:
               raise HTTPException(status_code=404, detail="Emak lo METAL dari lahir!")

        # response
        return hachu.to_dict(orient="records")

@app.get("/profile")
async def getProfiles():
    # get connection to db
    connection = getConnection()
    
    dadang = pd.read_sql("SELECT * FROM PROFILES;", connection)
    
    return dadang.to_dict(orient="records")

# @app.get(...)
# async def g# get connection to db):

# getConnection(ofileById():
#     pass


# @app.post(...)
# async def c# get connection to db):

# getConnection(eProfile():
#     pass


# @app.patch(...)
# async def u# get connection to db):

# getConnection(eProfile():
#     pass


# @app.delete(...)
# async def d# get connection to db):

# getConnection(eProfile():
#     pass
