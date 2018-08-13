# principles


# defs

### coordinator

Manages 1 or more services.
If more than 1 service will instanciate services and remember about them.

- methods can have params

the base coordinator

- just hold X services and allows you to manage the find the required services.

default methods

- services_list
- service_get
- service_delete
- errors
- services_stop()
- services_start()
- services_export()  #export all services to capnp structs in msgpack list
- services_import()
- ...


the data objects are stored in BCDB with name $coordinatorname if for the coordinator itself 

### services

A service running on our grid.
Full lifecycle management inside.

- methods cannot have params !

the data objects are stored in BCDB with name $coordinatorname__$servicename


### dna

is like DNA of a person, is the module which makes up the service or coordinator.
Loaded as module in the community.

### community

Is running set of coordinators.
In the community we can find the dna of services & coordinators
but also the services/coordinators which are actually running.

# rules

THE ONLY DATA is in the BCDB and per coordinator or per service


