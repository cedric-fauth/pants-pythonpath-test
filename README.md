# Problem using PYTHONPATH in pants run goal


```bash
PYTHONPATH=/workspaces/pants-pythonpath-test hello=123 pants run src:script
```

Output should be the same as running the python3 command:

`PYTHONPATH=/workspaces/pants-pythonpath-test hello=123 python3 src/script.py`:

```
123
/workspaces/pants-pythonpath-test
Now we call the lib
This is from the lib
```

