from Jumpscale import j
import gevent
JSBASE = j.servers.digitalme.community.coordinator_class_get()



class Coordinator(JSBASE):

    def init(self):
        self.data.state = "init"
        self.data_register()


    def monitor_main(self):
        print("monitor started")
        counter = 0
        while True:
            counter+=1
            print("monitor:%s:%s"%(self,counter))
            gevent.sleep(10)

