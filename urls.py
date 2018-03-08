from metrics_classes import SingleValueGauge, BiDirGauge, BucketsGauge
import sys
#from json-prometheus import host

host = sys.argv[1]

collected1 = 'https://{}:215/api/analytics/v1/datasets/cpu.utilization/data?seconds=1'.format(host)
collected2 = 'https://{}:215/api/analytics/v1/datasets/io.ops[op]/data?seconds=1'.format(host)
collected3 = 'https://{}:215/api/analytics/v1/datasets/nic.kilobytes[direction]/data?seconds=1'.format(host)
collected4 = 'https://{}:215/api/analytics/v1/datasets/ip.bytes[hostname]/data?seconds=1'.format(host)
collected5 = 'https://{}:215/api/analytics/v1/datasets/arc.size[component]/data?seconds=1'.format(host)
collected6 = 'https://{}:215/api/analytics/v1/datasets/io.bytes[op]/data?seconds=1'.format(host)
collected7 = 'https://{}:215/api/analytics/v1/datasets/arc.accesses[hit/miss]/data?seconds=1'.format(host)
collected8 = 'https://{}:215/api/analytics/v1/datasets/arc.hitratio/data?seconds=1'.format(host)
collected9 = 'https://{}:215/api/analytics/v1/datasets/arc.l2_accesses[hit/miss]/data?seconds=1'.format(host)
collected10 = 'https://{}:215/api/analytics/v1/datasets/arc.l2_size/data?seconds=1'.format(host)
collected11 = 'https://{}:215/api/analytics/v1/datasets/dnlc.accesses[hit/miss]/data?seconds=1'.format(host)
collected12 = 'https://{}:215/api/analytics/v1/datasets/arc.l2_accesses[share]/data?seconds=1'.format(host)
collected13 = 'https://{}:215/api/analytics/v1/datasets/arc.accesses[share]/data?seconds=1'.format(host)
collected14 = 'https://{}:215/api/analytics/v1/datasets/nfs3.bytes[share]/data?seconds=1'.format(host)
collected15 = 'https://{}:215/api/analytics/v1/datasets/nfs3.bytes[client]/data?seconds=1'.format(host)
collected16 = 'https://{}:215/api/analytics/v1/datasets/mem.heap[application]/data?seconds=1'.format(host)
collected17 = 'https://{}:215/api/analytics/v1/datasets/nfs3.ops[share]/data?seconds=1'.format(host)
collected18 = 'https://{}:215/api/analytics/v1/datasets/nfs3.ops[client]/data?seconds=1'.format(host)

bundles = []

bundles.append((SingleValueGauge, (collected1, 'cpu_utilization', host)))
bundles.append((BiDirGauge, (collected2, 'io_ops', host, 'write', 'read')))
bundles.append((BiDirGauge, (collected3, 'nic_direction', host, 'out', 'in')))
bundles.append((BucketsGauge, (collected4, 'ip_bytes_by_hostname', host)))
bundles.append((BucketsGauge, (collected5, 'arc_size_by_component', host)))
bundles.append((BiDirGauge, (collected6, 'hdd_direction', host, 'write', 'read')))
bundles.append((BiDirGauge, (collected7, 'ARC_accesses', host, 'metadata_hits', 'metadata_misses')))
bundles.append((BucketsGauge, (collected8, 'arc_hit_ratio', host)))
bundles.append((BiDirGauge, (collected9, 'L2ARC_accesses', host, 'hits', 'misses')))
bundles.append((BucketsGauge, (collected10, 'L2ARC_size', host)))
bundles.append((BiDirGauge, (collected11, 'DNLC_access', host, 'hits', 'misses')))
bundles.append((BucketsGauge, (collected12, 'L2ARC_accesses_by_share', host)))
bundles.append((BucketsGauge, (collected13, 'ARC_accesses_by_share', host)))
bundles.append((BucketsGauge, (collected14, 'nfs3_bytes_by_share', host)))
bundles.append((BucketsGauge, (collected15, 'nfs3_bytes_by_client', host)))
bundles.append((BucketsGauge, (collected16, 'mem_heap_by_application', host)))
bundles.append((BucketsGauge, (collected17, 'nfs3_ops_by_share', host)))
bundles.append((BucketsGauge, (collected18, 'nfs3_ops_by_client', host)))
