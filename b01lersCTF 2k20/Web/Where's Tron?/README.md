# SHOW TABLES #
# Tables ->     known_isomorphic_algorithms
#               programs
#               to_derezz
# SELECT * from known_isomorphic_algorithms # 
# SELECT * from programs # 
# SELECT * from to_derezz # 
# SELECT `COLUMN_NAME` FROM `INFORMATION_SCHEMA`.`COLUMNS` WHERE `TABLE_SCHEMA`='grid' AND `TABLE_NAME`='programs' #
# SELECT `COLUMN_NAME` FROM `INFORMATION_SCHEMA`.`COLUMNS` WHERE `TABLE_SCHEMA`='grid' AND `TABLE_NAME`='to_derezz' #
# SELECT `COLUMN_NAME` FROM `INFORMATION_SCHEMA`.`COLUMNS` WHERE `TABLE_SCHEMA`='grid' AND `TABLE_NAME`='known_isomorphic_algorithms' #
# programs -> id
#             name
#             status
#             location
# SELECT * FROM programs WHERE name LIKE BINARY '%Tron%' #