# Minimal C wrapper

```
python3 setup.py build_ext --inplace
```

We don't need the `build` directory or the `pycmath.c` generated code. We only need the `ccmath.cpython...so` file.

From python:

```
import ccmath
```

should work.

## Caveats

Be very careful to clean up all auto-generated files, including `pycmath.c` after a botched compilation!
