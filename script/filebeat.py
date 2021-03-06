import os
from fastdog.maintain.filebeat.dfilebeat import DFileBeat,multi_tail_file,django_process_parsers,elastice_search,nginx_log_parser,\
     elasticesearch_process
from fastdog.maintain.fast_log import set_log

from functools import partial
from concurrent.futures import ThreadPoolExecutor,as_completed
base_dir = os.path.dirname(  os.path.dirname( os.path.abspath(__file__) )  )
log_path = os.path.join( base_dir,'log/filebeat.log')
set_log(log_path)

#p_django = DFileBeat(harvest= partial(multi_tail_file,
                                      #[
                                       #'/pypro/easyjob/log/process.log',
                                       #'/pypro/voiceplatform/log/django.log'
                                       #]),
                     #parsers =django_process_parsers,
                  #outputs = [
                      #partial(elasticesearch_process,'liu.enjoyst.com:9200','elastic','he27375089','voice-django')
                  #] )

p_nginx = DFileBeat(harvest= partial(multi_tail_file,['/var/log/nginx/easyjob.log']),
                    parsers =nginx_log_parser,
                  outputs = [
                      partial(elastice_search,'z.enjoyst.com:9200','elastic','he27375089','easyjob-nginx')
                  ] )
p_nginx.run()
#executor =  ThreadPoolExecutor(max_workers = 2)
#batch_items = [ p_django.run,p_nginx.run]
#futures = [executor.submit(item) for item in batch_items]
#for future in as_completed(futures):
    #print(future.result() )