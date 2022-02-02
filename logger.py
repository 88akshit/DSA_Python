class Logger():
    def __init__(self, limit, rate):
        self.data = {}
        self.limit = limit
        self.rate = rate

    def shouldPrintMessage(self, timestamp, message):

        if message in self.data:
            messageTimeout, numberOfRequestsLeft = self.data[message]

            if messageTimeout > timestamp and numberOfRequestsLeft > 0:
                self.data[message] = (messageTimeout, numberOfRequestsLeft - 1)
                return True
            if messageTimeout <= timestamp:
                self.data[message] = (self.limit + messageTimeout, self.rate - 1)
                return True                
            else:
                return False
        
        else:
            self.data[message] = (self.limit + timestamp, self.rate - 1)
            print(self.data)
            return True

logger = Logger(limit = 30, rate = 3)

print(logger.shouldPrintMessage(1, 'foo')) # True
print(logger.shouldPrintMessage(2, 'bar')) # True
print(logger.shouldPrintMessage(3, 'foo')) # True
print(logger.shouldPrintMessage(8, 'bar')) # True
print(logger.shouldPrintMessage(15, 'foo')) # True
print(logger.shouldPrintMessage(17, 'foo')) # False
print(logger.shouldPrintMessage(19, 'foo')) # False
print(logger.shouldPrintMessage(19, 'bar')) # True
print(logger.shouldPrintMessage(21, 'bar')) # False
print(logger.shouldPrintMessage(31, 'foo')) # True
print(logger.shouldPrintMessage(32, 'bar')) # True