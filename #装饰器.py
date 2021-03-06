#装饰器
import functools
import time
def metric(fn):
    @functools.wraps(fn)
    def wraper(*args, **kargs):
        start=time.time()
        f=fn(*args, **kargs)
        end=time.time()-start
        print('%s executed in %s ms' % (fn.__name__, end))
        return f
    return wraper
# 测试
@metric
def fast(x, y):
    time.sleep(0.0012)
    return x + y;

@metric
def slow(x, y, z):
    time.sleep(0.1234)
    return x * y * z;

f = fast(11, 22)
s = slow(11, 22, 33)
if f != 33:
    print('测试失败!')
elif s != 7986:
    print('测试失败!')