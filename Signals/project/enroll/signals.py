from django.contrib.auth.signals import user_logged_in,user_logged_out,user_login_failed
from django.db.models.signals import pre_init, pre_save, pre_delete, post_init,post_save,post_delete,post_migrate,pre_migrate
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.core.signals import request_started, request_finished, got_request_exception
from django.db.backends.signals import connection_created


@receiver(user_logged_in, sender=User)
def login_success(sender, request, user,**kwargs):
     print("-------------")
     print('logged_in signal.... Run intro..')
     print("sender: ",sender)
     print("request: ",request)
     print('user: ',user)
     print('user password: ',user.password)
     print(f"kwargs: {kwargs}")

# user_logged_in.connect(login_success, sender=User) 

@receiver(user_logged_out, sender=User)
def logout_success(sender, request, user,**kwargs):
     print("-------------")
     print('logged_out signal.... Run outro..')
     print("sender: ",sender)
     print("request: ",request)
     print('user: ',user)
     print(f"kwargs: {kwargs}")

# user_logged_out.connect(logout_success, sender=User)

@receiver(user_login_failed)
def login_failed(sender, credentials, request,**kwargs):
     print("-------------")
     print('logged_out signal.... Run outro..')
     print("sender: ",sender)
     print('credentials: ',credentials)
     print("request: ",request)
     print(f"kwargs: {kwargs}")

# user_login_failed.connect(login_failed, sender=User)

@receiver(pre_save, sender=User)
def at_beginning_save(sender, instance, **kwargs):
     print("-------------")
     print('pre_save signal....')
     print("sender: ",sender)
     print('instance: ',instance)
     print(f"kwargs: {kwargs}")

# pre_save.connect(at_beginning_save, sender=User)

@receiver(post_save, sender=User)
def at_ending_save(sender, instance, created, **kwargs):
   if created:
     print("-------------")
     print('post_save signal....')
     print('New Record')
     print("sender: ",sender)
     print('instance: ',instance)
     print('created: ',created)
     print(f"kwargs: {kwargs}")
   else:
     print("-------------")
     print('post_save signal....')
     print('update')
     print("sender: ",sender)
     print('instance: ',instance)
     print('created: ',created)
     print(f"kwargs: {kwargs}") 

# post_save.connect(at_ending_save, sender=User)

@receiver(pre_delete, sender=User)
def at_beginning_delete(sender, instance, **kwargs):
     print("-------------")
     print('pre_delete signal....')
     print("sender: ",sender)
     print('instance: ',instance)
     print(f"kwargs: {kwargs}")

# pre_delete.connect(at_beginning_delete, sender=User)

@receiver(post_delete, sender=User)
def at_ending_delete(sender, instance, **kwargs):
     print("-------------")
     print('post_delete signal....')
     print("sender: ",sender)
     print('instance: ',instance)
     print(f"kwargs: {kwargs}")

# post_delete.connect(at_ending_delete, sender=User)


@receiver(pre_init, sender=User)
def at_begining_init(sender, *args, **kwargs):
     print("-------------")
     print('pre_init signal....')
     print("sender: ",sender)
     print(f"args: {args}")
     print(f"kwargs: {kwargs}")

# pre_init.connect(at_begining_init, sender=User)

@receiver(post_init, sender=User)
def at_ending_init(sender, *args, **kwargs):
     print("-------------")
     print('post_init signal....')
     print("sender: ",sender)
     print(f"args: {args}")
     print(f"kwargs: {kwargs}")

# post_init.connect(at_ending_init, sender=User)

@receiver(request_started)
def at_begining_request(sender, environ, **kwargs):
    print('-----------------')
    print('at begining request')
    print('sender: ',sender)
    print('environ: ',environ)
    print(f'kwargs: {kwargs}')

# request_started.connect(at_begining_request)

@receiver(request_finished)
def at_ending_request(sender, **kwargs):
    print('-----------------')
    print('at ending request')
    print('sender: ',sender)
    print(f'kwargs: {kwargs}')

# request_finished.connect(at_ending_request)

@receiver(got_request_exception)
def at_request_exception(sender, request, **kwargs):
    print('-----------------')
    print('at exception request')
    print('sender: ',sender)
    print('request: ',request)
    print(f'kwargs: {kwargs}')

# got_request_exception.connect(at_request_exception)

@receiver(pre_migrate)
def before_install_app(sender, app_config, verbosity, interactive, using, plan, apps,**kwargs):
    print('-----------------')
    print('before install app')
    print('App_config: ',app_config)
    print('verbosity: ',verbosity)
    print("interaction: ",interactive)
    print('using: ',using)
    print('plan: ',plan)
    print("plan: ",plan)
    print(f'kwargs: {kwargs}')

#pre_migrate.connect(before_install_app)

@receiver(post_migrate)
def at_end_migrate_flush(sender, app_config, verbosity, interactive, using, plan, apps,**kwargs):
    print('-----------------')
    print('Migrate flush')
    print('App_config: ',app_config)
    print('verbosity: ',verbosity)
    print("interaction: ",interactive)
    print('using: ',using)
    print('plan: ',plan)
    print("plan: ",plan)
    print(f'kwargs: {kwargs}')

#post_migrate.connect(at_end_migrate_flush)

@receiver(connection_created)
def con_db(sender, connection, **kwargs):
    print('-----------------')
    print('initial connection to the database.....')
    print('sender: ',sender)
    print('connection: ',connection)
    print(f'kwargs: {kwargs}')

# connection_created.connect(con_db)