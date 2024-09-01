def getStatsForRequest(m,database,request):

    url_map={}
    for db in database:
        id,short_url,long_url=db.split()
        key=id+short_url
        url_map[key]=long_url

    request_count={}


data=["0 ggl google.com","1 gg google.com","0 fb fb.com"]
req=['gg','fb','ggl']
m=2

"""
output:
 google.com 

"""
getStatsForRequest(m,data,req)