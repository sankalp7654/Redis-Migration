################### YOUR INPUT HERE #######################
REDIS_DUMP_JSON_DATA = "PUT_THE_JSON_DATA_AS_IT_IS"
TARGET_REDIS_HMSET_NAME = "MY_AWESOME_NAME"
TARGET_OUTPUT_REDIS_QUERY_FILE_NAME = "redis_query"
################### YOUR INPUT HERE #######################


########################## LOGIC ##########################
hm_dict = REDIS_DUMP_JSON_DATA[list(REDIS_DUMP_JSON_DATA.keys())[0]]['value']
outputFile = open("query", "w")

for key, value in hm_dict.items():
  query = "HMSET {TARGET_REDIS_HMSET_NAME} '{key}' '{value}'\n".format(key=key, value=value, TARGET_REDIS_HMSET_NAME=TARGET_REDIS_HMSET_NAME)
  outputFile.write(query)

outputFile.close()
