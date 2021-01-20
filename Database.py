import pandas as pd

### Check if database exists ###
def checkdb():
# If database Exists, Open and convert to Pandas DataFrame
    try:
        _forgopassdf = pd.read_csv('database.csv')
        #_forgopassdf = pd.DataFrame()
        print(_forgopassdf)
        return _forgopassdf

    # If database doesn't exist, create new dataframe to be saved later
    except FileNotFoundError:
        # Setup database
        _data = {'Website':[],
                'Username':[],
                'Password':[]}
        _forgopassdf = pd.DataFrame(_data)
        _forgopassdf.to_csv('database.csv', index=False)

### Appending new information to database ###
def appenddb(domain,username,password):
    # Get Dataframe
    _forgopassdf = checkdb()

    # Add new domain,user,pass to dataframe
    _new = {'Website':domain,'Username':username,'Password':password}
    _forgopassdf = _forgopassdf.append(_new, ignore_index=True)
    # Save updated dataframe to csv file
    _forgopassdf.to_csv('database.csv', index=False)
    


