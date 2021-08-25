import ntplib
import time

def get_network_time(x):
    #start = time.time()
    c = ntplib.NTPClient()
    response = c.request(x)
    ts = response.tx_time
    return time.ctime(ts)

if __name__ == "__main__":
  print('Please enter an NTP server: ')
  x = input()
  print(x)

  # t en second car on l'utilise pour le time.sleep()
  t = 2
  # boucle à True pour faire une boucle infinie
  boucle = True

  while boucle:
      print(get_network_time(x))
      # time.sleep(t) permet de freeze le programme pendant une période t sec
      time.sleep(t)
