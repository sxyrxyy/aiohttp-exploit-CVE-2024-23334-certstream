import threading
import time
import certstream


def collect_domains(run_duration):
    print("[~] Getting Domains")
    stop_time = time.time() + run_duration
    collected_domains = []

    def print_callback(message, context):
        if time.time() > stop_time:
            return

        if message['message_type'] == "certificate_update":
            domains = message['data']['leaf_cert']['all_domains']
            for domain in domains:
                if "*" not in domain and len(domain) < 15:
#                    print(domain)
                    collected_domains.append(domain)

    def listener_task():
        certstream.listen_for_events(print_callback, url='wss://certstream.calidog.io/')

    listener_thread = threading.Thread(target=listener_task, daemon=True)
    listener_thread.start()

    while time.time() < stop_time:
        time.sleep(0.1)

    print(f'[~] Collected {len(collected_domains)} Domains')
    return collected_domains
