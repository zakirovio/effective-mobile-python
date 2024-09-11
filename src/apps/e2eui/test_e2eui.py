from apps.e2eui.e2eui_main import E2EUI

def main():
    worker = E2EUI()
    worker.auth()
    worker.add_to_cart()
    worker.make_purchase()
