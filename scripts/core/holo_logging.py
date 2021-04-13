class holo_logging:

    def log_debug(message, system=False): #Only log these messages when Debug Mode is enabled

        print(message)#Temporary solution only

    def log_info(message, system=False): #Log messages for successful or ordinary events

        print(message)#Temporary solution only

    def log_warning(message, system=False): #Log messages for problems that can be ignored without affecting the program functionality (e.g. disk space low)

        print(message)#Temporary solution only

    def log_error(message, system=False): #Log messages for problems that hinder the program from functioning normally but that do not result in a crash

        print(message)#Temporary solution only

    def log_critical(message, system=False): #Log messages for critical problems that stop the program from continuing to run

        print(message)#Temporary solution only
