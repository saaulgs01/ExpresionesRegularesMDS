import re


texto = input()

patron = r"\d{4}-\d{2}-\d{2}\s+\d{2}:\d{2}:\d{2}.\d{3}\s+([A-Z]+).*\[(.+)\]\s+(.*\.)?(.+[^\.][^\s])\s+:\s+(.*)$"


results = re.findall(patron, texto)
for match in results:
    print("\"" + match[0] + "\",\"" + match[1] + "\",\"" + match[3] + "\",\"" + match[4]+"\"")

#2023-02-07 01:14:28.313 INFO 1174086 --- [main] drfp.Main : Starting Main v0.1-SNAPSHOT using Java 17.0.1 on raul2-ubuntu with PID 1174086 started by rmartin

#2023-02-07 01:14:29.428 INFO 1174086 --- [main] a.p.q.PostPCheck : Bean ’eventAsyncConfigurer’ of type [es.urjc.etsii.grafo.solver.services.events. EventAsyncConfigurer] is not eligible for getting processed by all BeanPostProcessors (for example: not eligible for auto-proxying)

#2022-02-07 01:14:29.428  INFO 1174086 --- [thread1] a.p.q.PostPCheck : Bean 'eventAsyncConfigurer' of type [es.urjc.etsii.grafo.solver.services.events.EventAsyncConfigurer] is not eligible for getting processed by all BeanPostProcessors (for example: not eligible for auto-proxying)
#"INFO","thread1","PostPCheck","Bean 'eventAsyncConfigurer' of type [es.urjc.etsii.grafo.solver.services.events.EventAsyncConfigurer] is not eligible for getting processed by all BeanPostProcessors (for example: not eligible for auto-proxying)"

#2022-02-07 01:14:28.313  INFO 1174086 --- [main] drfp.Main            : Starting Main v0.1-SNAPSHOT using Java 17.0.1 on raul2-ubuntu with PID 1174086 started by rmartin

#2023-02-07 01:14:29.806 INFO 1174086 --- [main] TomcatWebServer : Tomcatinitialized with port(s): 8080 (http)
# 2023-02-07 01:14:29.818 INFO 1174086 --- [main] o.a.c.c.StdSvc : Starting service [Tomcat]

#2023-02-07 01:14:29.806 CULO 1174086 --- [main] TomcatWebServer : Tomcatinitialized with port(s): 8080 (http)
