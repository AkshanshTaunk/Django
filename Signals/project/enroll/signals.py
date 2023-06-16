from django.contrib.auth.signals import user_logged_in,user_logged_out,user_login_failed
from django.db.models.signals import pre_init, pre_save, pre_delete, post_init,post_save,post_delete
from django.contrib.auth.models import User
from django.dispatch import receiver
# from django.core.signals import request_started, request_finished, got_request_exception


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


