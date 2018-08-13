
from jumpscale import j



community = j.servers.digitalme.community

community.knowledge_learn("recipes")

m = community.coordinator_dna["zos_virtualbox"]

#now knowledge has been loaded

# for i in range(100):
#     assert (0, 11) == r2.action_ask("task1", 10)  # returns resultcode & result

# assert True == r2.monitor_running()
# assert True == r2.running()

# community.start()




import bpython; bpython.embed(locals(), banner='')


