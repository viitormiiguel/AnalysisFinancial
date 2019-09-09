import javabridge

cpython = javabridge.JClassWrapper('org.cellprofiler.javabridge.CPython')()
d = javabridge.JClassWrapper('java.util.Hashtable')()
result = javabridge.JClassWrapper('java.util.ArrayList')()
d.put("result", result)
cpython.execute(
    'import javabridge\n'
    'x = { "foo":"bar"}\n'
    'ref_id = javabridge.create_and_lock_jref(x)\n'
    'javabridge.JWrapper(result).add(ref_id)', d, d)
cpython.execute(
    'import javabridge\n'
    'ref_id = javabridge.to_string(javabridge.JWrapper(result).get(0))\n'
    'assert javabridge.redeem_jref(ref_id)["foo"] == "bar"\n'
    'javabridge.unlock_jref(ref_id)', d, d)

    