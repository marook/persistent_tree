
import datetime
from persistent_tree import manipulate, model
import unittest

class TreeInsertPerformanceTest(unittest.TestCase):

    def test(self):
        sample_sizes = [100, 1600, 25600]
        samples = self.measure_samples(sample_sizes)
        
        duration_increases = list(self.calc_size_duration_increase_ratio(samples))

        self.assertTrue(duration_increases[1] / duration_increases[0] > 0.5, 'insert ratios: %s' % (', '.join(['%s' % (duration_increase, ) for duration_increase in duration_increases]), ))
        
    def measure_samples(self, sample_sizes):
        samples = {}

        for sample_size in sample_sizes:
            duration = self.measure_build_tree(sample_size)

            samples[sample_size] = duration

        print '\n'.join(['%s items took %s' % (sample_size, duration) for sample_size, duration in sorted(samples.iteritems(), key=lambda item: item[0])])

        return samples

    def measure_build_tree(self, number_of_inserted_nodes):
        tree = manipulate.Tree()
        nodes = self.build_nodes_list(number_of_inserted_nodes)

        start_time = datetime.datetime.now()

        for node in nodes:
            tree.insert_node(node)

        end_time = datetime.datetime.now()

        return end_time - start_time

    def build_nodes_list(self, number_of_nodes):
        nodes = []

        for i in xrange(number_of_nodes):
            nodes.append(create_node_from_index(i))

        return nodes

    def calc_size_duration_increase_ratio(self, samples):
        sorted_sample_sizes = sorted(samples.iterkeys())

        last_inserts_per_time = self.calc_inserts_per_second(sorted_sample_sizes[0], samples[sorted_sample_sizes[0]])

        for sample_size in sorted_sample_sizes[1:]:
            current_inserts_per_time = self.calc_inserts_per_second(sample_size, samples[sample_size])

            yield current_inserts_per_time / last_inserts_per_time

            last_inserts_per_time = current_inserts_per_time

    def calc_inserts_per_second(self, sample_size, sample_duration):
        return float(sample_size) / sample_duration.total_seconds()

def create_node_from_index(i):
    i = switch_bits(i, 0, 5)
    i = switch_bits(i, 1, 7)
    i = switch_bits(i, 2, 4)
    i = switch_bits(i, 3, 8)
    i = switch_bits(i, 6, 9)
    i = switch_bits(i, 10, 11)

    return model.Node(i, None)

def switch_bits(i, b0, b1):
    v0 = (i & (1 << b0) >> b0)
    v1 = (i & (1 << b1) >> b1)

    if v0 == 0:
        i &= ~(1 << b1)
    else:
        i |= 1 << b1

    if v1 == 0:
        i &= ~(1 << b0)
    else:
        i |= 1 << b0

    return i
