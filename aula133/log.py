#Abstração 
#Herança - é um (ex: LogFileMix é um Log)
from pathlib import Path

LOG_FILE = Path(__file__).parent / 'log.txt'


class Log:
    def _log(self, msg):
        raise NotImplementedError('Implemente o método log')
    
    def log_error(self, msg):
        return self._log(f'Error: {msg}')
    
    def log_success(self, msg):
        return self._log(f'Success: {msg}')
    
class LogFileMixin(Log):
    def _log(self, msg):
        msg_formatada = f'{msg} ({self.__class__.__name__})' 
        print('Salvando no log...', msg_formatada)
        with open(LOG_FILE, 'a') as arquivo:
            arquivo.write(msg_formatada)
            arquivo.write('\n')
    
class LogPrintMixin(Log):
    def _log(self, msg):
        print(f'{msg} ({self.__class__.__name__}) ')
    
    
if __name__ == '__main__':
    lp = LogPrintMixin()
    lp._log('Qualquer Coisa')
    lp.log_error('avae')
    lp.log_success('Que legal')
    
    lf = LogFileMixin()
    lf._log('Qualquer Coisa')
    lf.log_error('avae')
    lf.log_success('Que legal')

    
    
