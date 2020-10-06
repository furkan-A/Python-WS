from speedtest import Speedtest

st = Speedtest()

dwl = st.download()/1000000
upl = st.upload()/1000000

print("Download : ", "{:2f}".format(dwl), " Mbps")
print("Upload :", "{:2f}".format(upl), " Mbps")