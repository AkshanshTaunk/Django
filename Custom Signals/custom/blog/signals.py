from django.dispatch import signals, receiver

#creating signals
notification = signals(providing_args=["request","user"])

#receiver function
@receiver (notification)
def show_notification(sender, **kwargs):
    print(sender)
    print(f'{**kwargs}')
    print("notification")#just for checking before code