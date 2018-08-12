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
- stop_all
- ...

### services

A service running on our grid.
Full lifecycle management inside.

- methods cannot have params !