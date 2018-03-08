# zfs-prometheus-collector

This collects analytics from an Oracle ZFS Appliance. It uses requests to scrape the API for measurements, and parses them into Prometheus metrics classes.

The metrics classes are stored in metrics classes.
the urls are store in urls.py. They can be customized to add additional analytics. 

There are three types of metrics:
Single guage - for use with 1 simple item, such as %CPU utilization.

A bi directional metric, such as HDD Utilization with read, write, and total or network with in/ out/ total

a buckets metric such as NFS bytes per host name, or per accessed share.

All measurements need to be turned on in the appliances analytics worksheet page.

To create a new URL it needs to be bundled according to the urls.py. Add the URL with {}.format for hostname, add the metric class, and the in and out name for bidirectional measurements. if applicable

User credentials are stored in secrets.py. Create and secure this file, chmod 600.


To start run with the hostname of the oracle server, and the local port for the app to listen on for prometheus scraper. 
json-prometheus.py {hostname} {listen port}
