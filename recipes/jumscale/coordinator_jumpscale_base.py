from jumpscale import j
JSBASE = j.servers.digitalme.community.coordinator_class_get()



class Coordinator(JSBASE):

    def init(self):
        #TODO, check min version is 9.5 of jumpscale
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