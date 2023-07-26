def my_middleware(get_response):
    #some code
    #some code
    #some code
    print("one time initialization & configuration")
    def my_function(request):
      #some code
      #some code
      #some code
      print("execute before view")
      reponse = get_reponse(request)
      #some code
      #some code
      #some code
      print("execution after view")
      return response
    return my_function