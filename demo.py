from simple_firebase_realtime_db import FirebaseRealtimeDB as DB
import time

DB.initialize(
    certificate_path='',
    database_url=''
)

path = 'desired/path'

print(
    'set',
    DB.set(
        {
            'test-key':'test-value'
        },
        path
    )
)

time.sleep(10)

import json
print(json.dumps(DB.get(path), indent=4))

time.sleep(10)

print('delete', DB.delete(path))