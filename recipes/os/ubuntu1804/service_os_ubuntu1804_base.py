from Jumpscale import j
import gevent
JSBASE = j.servers.digitalme.community.service_class_get()

SCHEMA = """
varpath = "/" (S)
"""

class Service(JSBASE):

    def init(self):
        self.data.state = "init" #init,new,start,stop, error,halted
        self.data_register()


    def action_start(self):
        if self.data.state in ["new"]:
            # TODO:*1 start
            ok = True
            if ok:
                self.data.state = "active"
                self.data.epoch_started = j.data.time.epoch
                print("started")
                self.data_register()
            else:
                self.delete()


    def action_delete(self):
        self.stop()
        if self.data.state in ["active", "error", "halted"]:
            print("delete")
            self.data.state = "deleted"
            self.data_register()


    def action_stop(self):
        if self.data.state in ["active"]:
            self.data.epoch_stopped = j.data.time.epoch
            print("stop")
            self.data.state = "halted"
            self.data_register()


    def monitor_main(self):
        print("monitor started")
        counter = 0
        while True:
            j.shell()
            k
            counter += 1
            print("monitor:%s:%s" % (self, counter))
            gevent.sleep(10)

