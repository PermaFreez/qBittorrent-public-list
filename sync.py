import qbittorrentapi

qbt_client = qbittorrentapi.Client(
    host='127.0.0.1',
    port=8080,
    username='admin',
    password='adminadmin'
)

html_file = open("torrents.html", "w") 

html_file.write("<html>\n")
html_file.write("  <head>\n")
html_file.write("    <style>\n      table {\n        margin-left: auto; \n        margin-right: auto;\n      }\n      table, th {\n        border: 2px solid black; \n        border-collapse: collapse; \n      }\n      table.noborder, th.noborder {\n        border: 0;\n      }\n    </style>\n")
html_file.write("    <title>My Torrents</title>\n")
html_file.write("  </head>\n")

html_file.write("  <body>\n")
html_file.write('    <table class="noborder">\n      <tr><th class="noborder"><h2><b>My torrents from newest to oldest</b></h2></th></tr>\n      <tr><th class="noborder"><h3>Number of my torrents: ' + str(len(qbt_client.torrents.info())) + '</h3></th></tr>\n    </table>\n')
html_file.write('    <table>\n')
for torrent in qbt_client.torrents.info(sort="added_on", reverse=True):
  html_file.write("      <tr>\n")
  html_file.write("        <th>" + torrent.name + "</th>\n")
  html_file.write("        <th><a href='" + torrent.magnet_uri + "'>Magnet</a></th>\n")
  html_file.write("        <th>" + str(round(torrent.progress * 100, 2)) + "%</th>\n")
  html_file.write("      </tr>\n")

html_file.write("    </table>\n")
html_file.write("  </body>\n")
html_file.write("</html>\n")

html_file.close()
