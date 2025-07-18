def is_context_manager(obj):
    if hasattr(obj, '__enter__') and hasattr(obj, '__exit__'):
        return True
    else:
        return False


print(is_context_manager(open('output.txt', mode='w')))