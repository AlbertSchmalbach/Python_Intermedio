import speedtest
from Clear import clearConsole

st = speedtest.Speedtest()

d_st = st.download()

u_st = st.upload()

clearConsole()

print('Tu velocidad de descarga es', round(d_st))
print('Tu velocidad de subida es', round(u_st))