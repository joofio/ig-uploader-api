import re

data = """
08:00:05.716 [main] INFO dk.jkiddo.EmberApplication -- STARTING EMBER

  .   ____          _            __ _ _
 /\\ / ___'_ __ _ _(_)_ __  __ _ \ \ \ \
( ( )\___ | '_ | '_| | '_ \/ _` | \ \ \ \
 \\/  ___)| |_)| | | | | || (_| |  ) ) ) )
  '  |____| .__|_| |_|_| |_\__, | / / / /
 =========|_|==============|___/=/_/_/_/
 :: Spring Boot ::                (v3.2.2)

2024-04-16T08:00:06.091Z  INFO 1 --- [           main] dk.jkiddo.EmberApplication               : Starting EmberApplication v0.7.0-SNAPSHOT using Java 17.0.10 with PID 1 (/app/main.jar started by nonroot in /app)
2024-04-16T08:00:06.094Z  INFO 1 --- [           main] dk.jkiddo.EmberApplication               : No active profile set, falling back to 1 default profile: "default"
2024-04-16T08:00:06.930Z  INFO 1 --- [           main] org.quartz.impl.StdSchedulerFactory      : Using default implementation for ThreadExecutor
2024-04-16T08:00:06.936Z  INFO 1 --- [           main] org.quartz.core.SchedulerSignalerImpl    : Initialized Scheduler Signaller of type: class org.quartz.core.SchedulerSignalerImpl
2024-04-16T08:00:06.936Z  INFO 1 --- [           main] org.quartz.core.QuartzScheduler          : Quartz Scheduler v.2.3.2 created.
2024-04-16T08:00:06.936Z  INFO 1 --- [           main] org.quartz.simpl.RAMJobStore             : RAMJobStore initialized.
2024-04-16T08:00:06.936Z  INFO 1 --- [           main] org.quartz.core.QuartzScheduler          : Scheduler meta-data: Quartz Scheduler (v2.3.2) 'quartzScheduler' with instanceId 'NON_CLUSTERED'
  Scheduler class: 'org.quartz.core.QuartzScheduler' - running locally.
  NOT STARTED.
  Currently in standby mode.
  Number of jobs executed: 0
  Using thread pool 'org.quartz.simpl.SimpleThreadPool' - with 10 threads.
  Using job-store 'org.quartz.simpl.RAMJobStore' - which does not support persistence. and is not clustered.

2024-04-16T08:00:06.936Z  INFO 1 --- [           main] org.quartz.impl.StdSchedulerFactory      : Quartz scheduler 'quartzScheduler' initialized from an externally provided properties instance.
2024-04-16T08:00:06.936Z  INFO 1 --- [           main] org.quartz.impl.StdSchedulerFactory      : Quartz scheduler version: 2.3.2
2024-04-16T08:00:06.936Z  INFO 1 --- [           main] org.quartz.core.QuartzScheduler          : JobFactory set to: org.springframework.scheduling.quartz.SpringBeanJobFactory@6f4ade6e
2024-04-16T08:00:06.948Z  WARN 1 --- [           main] ion$DefaultTemplateResolverConfiguration : Cannot find template location: classpath:/templates/ (please add some templates, check your Thymeleaf configuration, or set spring.thymeleaf.check-template-location=false)
2024-04-16T08:00:06.980Z  INFO 1 --- [           main] o.s.s.quartz.SchedulerFactoryBean        : Starting Quartz Scheduler now
2024-04-16T08:00:06.981Z  INFO 1 --- [           main] org.quartz.core.QuartzScheduler          : Scheduler quartzScheduler_$_NON_CLUSTERED started.
2024-04-16T08:00:06.989Z  INFO 1 --- [           main] dk.jkiddo.EmberApplication               : Started EmberApplication in 1.196 seconds (process running for 1.584)
Error fetching https://packages.fhir.org/hl7.fhir.eu.extension: Invalid HTTP response 404 from https://packages.fhir.org/hl7.fhir.eu.extension (Not Found) (content in /tmp/http-log/fhir-http-2.log)
2024-04-16T08:00:08.729Z  INFO 1 --- [           main] o.h.f.u.n.FilesystemPackageCacheManager  : Failed to determine latest version of package hl7.fhir.eu.extension from server: https://packages.fhir.org
2024-04-16T08:00:10.816Z  INFO 1 --- [           main] o.h.f.u.n.FilesystemPackageCacheManager  : Failed to determine latest version of package hl7.fhir.eu.extension from server: https://packages2.fhir.org/packages
2024-04-16T08:00:13.369Z  INFO 1 --- [           main] o.h.f.u.n.FilesystemPackageCacheManager  : Failed to determine latest version of package hl7.fhir.eu.extension from server: build.fhir.org
Installing hl7.fhir.eu.extension#? to the package cache
  Fetching:
Error fetching https://packages.fhir.org/hl7.fhir.eu.extension: Invalid HTTP response 404 from https://packages.fhir.org/hl7.fhir.eu.extension (Not Found) (content in /tmp/http-log/fhir-http-3.log)
2024-04-16T08:00:13.423Z  INFO 1 --- [           main] o.h.f.u.npm.BasePackageCacheManager      : Failed to resolve package hl7.fhir.eu.extension#null from server: https://packages.fhir.org (Package not found: hl7.fhir.eu.extension)
2024-04-16T08:00:13.568Z  INFO 1 --- [           main] o.h.f.u.npm.BasePackageCacheManager      : Failed to resolve package hl7.fhir.eu.extension#null from server: https://packages2.fhir.org/packages (Package not found: hl7.fhir.eu.extension)
Error fetching https://packages.fhir.org/hl7.fhir.eu.extension: Invalid HTTP response 404 from https://packages.fhir.org/hl7.fhir.eu.extension (Not Found) (content in /tmp/http-log/fhir-http-4.log)
2024-04-16T08:00:13.631Z  INFO 1 --- [           main] o.h.f.u.npm.BasePackageCacheManager      : Failed to resolve package hl7.fhir.eu.extension#null.x from server: https://packages.fhir.org (Package not found: hl7.fhir.eu.extension)
2024-04-16T08:00:14.573Z  INFO 1 --- [           main] o.h.f.u.npm.BasePackageCacheManager      : Failed to resolve package hl7.fhir.eu.extension#null.x from server: https://packages2.fhir.org/packages (Package not found: hl7.fhir.eu.extension)
2024-04-16T08:00:14.588Z  INFO 1 --- [           main] .s.b.a.l.ConditionEvaluationReportLogger : 

Error starting ApplicationContext. To display the condition evaluation report re-run your application with 'debug' enabled.
2024-04-16T08:00:14.614Z ERROR 1 --- [           main] o.s.boot.SpringApplication               : Application run failed

org.hl7.fhir.exceptions.FHIRException: Unable to resolve package id hl7.fhir.eu.extension#null
        at org.hl7.fhir.utilities.npm.FilesystemPackageCacheManager.fetchTheOldWay(FilesystemPackageCacheManager.java:827) ~[org.hl7.fhir.utilities-6.1.2.2.jar!/:na]
        at org.hl7.fhir.utilities.npm.FilesystemPackageCacheManager.loadFromPackageServer(FilesystemPackageCacheManager.java:309) ~[org.hl7.fhir.utilities-6.1.2.2.jar!/:na]
        at org.hl7.fhir.utilities.npm.FilesystemPackageCacheManager.loadPackage(FilesystemPackageCacheManager.java:615) ~[org.hl7.fhir.utilities-6.1.2.2.jar!/:na]
        at org.hl7.fhir.utilities.npm.BasePackageCacheManager.loadPackage(BasePackageCacheManager.java:183) ~[org.hl7.fhir.utilities-6.1.2.2.jar!/:na]
        at dk.jkiddo.EmberApplication.loadResourcesFromNPM(EmberApplication.java:133) ~[!/:0.7.0-SNAPSHOT]
        at dk.jkiddo.EmberApplication.run(EmberApplication.java:90) ~[!/:0.7.0-SNAPSHOT]
        at org.springframework.boot.SpringApplication.lambda$callRunner$4(SpringApplication.java:786) ~[spring-boot-3.2.2.jar!/:3.2.2]
        at org.springframework.util.function.ThrowingConsumer$1.acceptWithException(ThrowingConsumer.java:83) ~[spring-core-6.1.3.jar!/:6.1.3]
        at org.springframework.util.function.ThrowingConsumer.accept(ThrowingConsumer.java:60) ~[spring-core-6.1.3.jar!/:6.1.3]
        at org.springframework.util.function.ThrowingConsumer$1.accept(ThrowingConsumer.java:88) ~[spring-core-6.1.3.jar!/:6.1.3]
        at org.springframework.boot.SpringApplication.callRunner(SpringApplication.java:798) ~[spring-boot-3.2.2.jar!/:3.2.2]
        at org.springframework.boot.SpringApplication.callRunner(SpringApplication.java:786) ~[spring-boot-3.2.2.jar!/:3.2.2]
        at org.springframework.boot.SpringApplication.lambda$callRunners$3(SpringApplication.java:774) ~[spring-boot-3.2.2.jar!/:3.2.2]
        at java.base/java.util.stream.ForEachOps$ForEachOp$OfRef.accept(ForEachOps.java:183) ~[na:na]
        at java.base/java.util.stream.SortedOps$SizedRefSortingSink.end(SortedOps.java:357) ~[na:na]
        at java.base/java.util.stream.AbstractPipeline.copyInto(AbstractPipeline.java:510) ~[na:na]
        at java.base/java.util.stream.AbstractPipeline.wrapAndCopyInto(AbstractPipeline.java:499) ~[na:na]
        at java.base/java.util.stream.ForEachOps$ForEachOp.evaluateSequential(ForEachOps.java:150) ~[na:na]
        at java.base/java.util.stream.ForEachOps$ForEachOp$OfRef.evaluateSequential(ForEachOps.java:173) ~[na:na]
        at java.base/java.util.stream.AbstractPipeline.evaluate(AbstractPipeline.java:234) ~[na:na]
        at java.base/java.util.stream.ReferencePipeline.forEach(ReferencePipeline.java:596) ~[na:na]
        at org.springframework.boot.SpringApplication.callRunners(SpringApplication.java:774) ~[spring-boot-3.2.2.jar!/:3.2.2]
        at org.springframework.boot.SpringApplication.run(SpringApplication.java:341) ~[spring-boot-3.2.2.jar!/:3.2.2]
        at org.springframework.boot.SpringApplication.run(SpringApplication.java:1354) ~[spring-boot-3.2.2.jar!/:3.2.2]
        at org.springframework.boot.SpringApplication.run(SpringApplication.java:1343) ~[spring-boot-3.2.2.jar!/:3.2.2]
        at dk.jkiddo.EmberApplication.main(EmberApplication.java:78) ~[!/:0.7.0-SNAPSHOT]
        at java.base/jdk.internal.reflect.NativeMethodAccessorImpl.invoke0(Native Method) ~[na:na]
        at java.base/jdk.internal.reflect.NativeMethodAccessorImpl.invoke(NativeMethodAccessorImpl.java:77) ~[na:na]
        at java.base/jdk.internal.reflect.DelegatingMethodAccessorImpl.invoke(DelegatingMethodAccessorImpl.java:43) ~[na:na]
        at java.base/java.lang.reflect.Method.invoke(Method.java:568) ~[na:na]
        at org.springframework.boot.loader.launch.Launcher.launch(Launcher.java:91) ~[main.jar:0.7.0-SNAPSHOT]
        at org.springframework.boot.loader.launch.Launcher.launch(Launcher.java:53) ~[main.jar:0.7.0-SNAPSHOT]
        at org.springframework.boot.loader.launch.JarLauncher.main(JarLauncher.java:58) ~[main.jar:0.7.0-SNAPSHOT]

2024-04-16T08:00:14.619Z  INFO 1 --- [           main] org.quartz.core.QuartzScheduler          : Scheduler quartzScheduler_$_NON_CLUSTERED paused.
2024-04-16T08:00:14.619Z  INFO 1 --- [           main] o.s.s.quartz.SchedulerFactoryBean        : Shutting down Quartz Scheduler
2024-04-16T08:00:14.620Z  INFO 1 --- [           main] org.quartz.core.QuartzScheduler          : Scheduler quartzScheduler_$_NON_CLUSTERED shutting down.
2024-04-16T08:00:14.620Z  INFO 1 --- [           main] org.quartz.core.QuartzScheduler          : Scheduler quartzScheduler_$_NON_CLUSTERED paused.
2024-04-16T08:00:14.620Z  INFO 1 --- [           main] org.quartz.core.QuartzScheduler          : Scheduler quartzScheduler_$_NON_CLUSTERED shutdown complete.
"""

pattern = "\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\.\d{3}Z"

dd = re.split(pattern, data)

final_data = []

# Regex pattern to match the start of each log entry
log_pattern = r"""(INFO|WARN|ERROR)                              # Log Level
\s+
(\d+)                                          # Process ID
\s+---\s+
\[\s*([^\]]+)\s*\]                             # Thread
\s+
([\w\.\$]+)                                    # Logger Name
\s+:\s+
(.+)                                           # Message
"""


for d in dd[1:]:
    print(d)
    print(re.search(log_pattern, d, re.VERBOSE | re.DOTALL).groups())
    print("..." * 100)
