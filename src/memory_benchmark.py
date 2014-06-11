
from persistent_tree import model

def main():
    warmup()

    run_benchmark(allocate_many_nodes)

def warmup():
    get_virtual_memory_size()

def run_benchmark(benchmark):
    start_usage = get_virtual_memory_size()

    memory_ref = benchmark()

    end_usage = get_virtual_memory_size()

    # this call makes sure that the python interpreter can't garbage
    # collect the memory which has been allocated in the benchmark
    hold_memory_ref(memory_ref)

    print_rusage_delta(benchmark.__name__, start_usage, end_usage)

def get_virtual_memory_size():
    virtual_memory_size = get_virtual_memory_size_via_resource()

    if not virtual_memory_size is None:
        return virtual_memory_size

    return get_virtual_memory_size_via_psutil()

def get_virtual_memory_size_via_resource():
    try:
        import resource

        return resource.getrusage(resource.RUSAGE_SELF).ixrss
    except ImportError:
        return None

def get_virtual_memory_size_via_psutil():
    import psutil

    return psutil.virtual_memory().used

def hold_memory_ref(memory_ref):
    pass

def print_rusage_delta(benchmark_name, memory_usage_0, memory_usage_1):
    delta_memory_usage = memory_usage_1 - memory_usage_0

    print 'Memory delta for %s is %s kB' % (benchmark_name, (delta_memory_usage / 1024))

def allocate_many_nodes():
    nodes = 10000 * [None,]

    for i in xrange(len(nodes)):
        nodes[i] = model.Node(None, None)

    return nodes

if __name__ == '__main__':
    main()
