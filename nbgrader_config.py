c = get_config()

import os.path
c.CourseDirectory.root = os.path.join(os.path.expanduser('~'),'course01')

c.Exchange.root = '/tmp/exchange'

