print r"""
                   /
               A.A/
             ~~ ^ ^\_
 \\         ~~/    __V
  \\\      ~~/   /
    \\___>>>     /
    /             \
    \      ____/\\\\
     \ \ \ \    ////
     / / / /    u u
     \\  \\
      u   u
     """
print 'Hint: First Code Input: i'
import zlib
import marshal
import new
import sys
import base64
import time
import tty
import termios

a0_func = 'YwEAAAAJAAAABAAAAAMAAABzHAEAAGQBAH0BAHQAAGoAAIMAAH0CAHQBAGoCAGoDAIMAAH0DAHQEAGoFAHwDAIMBAH0EAHQGAGoHAHQBAGoCAGoDAIMAAIMBAAF0CAB0AQBqAgBqCQBkAgCDAQCDAQCJAAB0BABqCgB8AwB0BABqCwB8BACDAwABZAMAagwAdA0AhwAAZgEAZAQAhgAAfAAAgwIAgwEAfQUAdAAAagAAgwAAfQYAfAYAfAIAGGQFAGsEAHLVAGQDAGoMAHQNAIcAAGYBAGQGAIYAAHwAAIMCAIMBAH0FAG4AAHwFAGoOAHwBAIMBAH0HAHQPAHwHAIMBAGQCAGsCAHIKAWQHAH0IAHwHAGQIABl8CABmAgBTfAcAZAgAGXwHAGQCABlmAgBTKAkAAABOcwMAAAA6UjppAQAAAHQAAAAAYwEAAAABAAAAAwAAABMAAABzFAAAAHQAAHQBAHwAAIMBAIgAAEGDAQBTKAEAAABOKAIAAAB0AwAAAGNocnQDAAAAb3JkKAEAAAB0AQAAAHgoAQAAAHQKAAAAcGFzc3BocmFzZSgAAAAAcx4AAAAvdXNyL2xvY2FsL2Jpbi9ydXNzaWFuX2RvbGwucHl0CAAAADxsYW1iZGE+LAAAAHMAAAAAaQQAAABjAQAAAAEAAAAEAAAAEwAAAHMYAAAAdAAAdAEAfAAAgwEAiAAAZAEAF0GDAQBTKAIAAABOaQEAAAAoAgAAAFIBAAAAUgIAAAAoAQAAAFIDAAAAKAEAAABSBAAAACgAAAAAcx4AAAAvdXNyL2xvY2FsL2Jpbi9ydXNzaWFuX2RvbGwucHlSBQAAAC8AAABzAAAAAHQIAAAAZmluaXNoZWRpAAAAACgQAAAAdAQAAAB0aW1ldAMAAABzeXN0BQAAAHN0ZGludAYAAABmaWxlbm90BwAAAHRlcm1pb3N0CQAAAHRjZ2V0YXR0cnQDAAAAdHR5dAYAAABzZXRyYXdSAgAAAHQEAAAAcmVhZHQJAAAAdGNzZXRhdHRydAkAAABUQ1NBRFJBSU50BAAAAGpvaW50AwAAAG1hcHQFAAAAc3BsaXR0AwAAAGxlbigJAAAAdAcAAABtZXNzYWdldAwAAABzcGxpdF9zdHJpbmd0AgAAAHQwdAIAAABmZHQMAAAAb2xkX3NldHRpbmdzdAMAAAByZXN0AgAAAHQxUgMAAAB0AQAAAF8oAAAAACgBAAAAUgQAAABzHgAAAC91c3IvbG9jYWwvYmluL3J1c3NpYW5fZG9sbC5weXQKAAAAYXNrZGVjcnlwdCEAAABzIAAAAAABBgIMAQ8BDwEWARgCFgIhAQwBEAEkAQ8BEgEGAQ4B'

x = marshal.loads(base64.b64decode(a0_func))
x_func = new.function(x, {'ord':ord, 'sys':sys,
                          'map':map, 'chr':chr,
                          'time':time, 'tty':tty,
                          'termios':termios,
                          'len':len,
})

exec x