from pandas import read_json
# import subprocess
import datetime

date = datetime.datetime.now().date()

ids = [1,7,8,9,10,11,12,13,14,15]

airborne_particles = ["NO2", "SO2", "CO", "PM2.5", "PM10","O3"]

types = ["dailystat", "dailyaqi"]

for id in ids:
#     subprocess.call("mkdir %s"%id, shell=True)
    for type in types:
        list_temp = []
#         subprocess.call("mkdir %s/%s"%(id, type), shell=True)
        for airborne_particle in airborne_particles:
            df_temp = read_json("http://moitruongthudo.vn/public/%s/%s?site_id=%s"%(type, airborne_particle, id))
            if len(df_temp) > 0:
                if type == "dailyaqi":
                    df_temp = df_temp.drop(columns="color")
                df_temp = df_temp.rename(columns={'value':airborne_particle})
                list_temp.append(df_temp)
        data = list_temp[0]
        for i in range(1,len(list_temp)):
            data = data.join(list_temp[i].set_index('time'), on='time', how='outer')
        data.to_csv("%s/%s/%s.csv"%(id, type, date),index=False)