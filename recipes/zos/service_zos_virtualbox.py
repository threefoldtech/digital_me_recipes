from Jumpscale import j
import gevent
JSBASE = j.servers.digitalme.community.service_class_get()

SCHEMA = """
name = "" (S)    # name as used in virtualbox sal
redis_addr = "" (S)  #for the client to connect to
redis_port = 0 (I)
epoch_started = 0 (D)
epoch_stopped = 0 (D)
description = ""
state = "new,active,error,halted,deleted" (S)  #needs to become enumeration, so no mistakes can be made, now string
"""

class Service(JSBASE):

    # def __init__(self,community,name,instance):
    #     JSBASE.__init__(self,community=community,name=name,instance=instance)

    def init(self):
        #nothing to do, no dependencies
        self.data.state = "init"
        self.save()


    def start(self):
        if self.data.state in ["new"]:
            #TODO:*1 start
            ok=True
            if ok:
                self.data.state = "active"
                self.data.epoch_started =  j.data.time.epoch
                self.save()
            else:
                self.delete()
            
    def delete(self):
        self.stop()
        if self.data.state in ["active","error","halted"]:
            self.data.state = "deleted"
            self.save()        

    def stop(self):
        if self.data.state in ["active"]:
            self.data.epoch_stopped =  j.data.time.epoch
            self.data.state = "halted"
            self.save()                    

    def monitor_main(self):
        print("monitor started")
        counter = 0
        while True:
            gevent.sleep(1)
            counter+=5
            print("monitor:%s:%s"%(self,counter))

    def ok(self):
        pass