"""
Run an instance of the pyDEX App

author: officialcryptomaster@gmail.com
"""

from pydex_app import create_app

# You can start the service as a Docker image
# docker run -ti -p 8080:8080 -e JSON_RPC_URL=https://mainnet.infura.io -e NETWORK_ID=1 0xorg/order-watcher
# or build the source and run node lib/src/server.js.
# test with wscat -c ws://0.0.0.0:8080

if __name__ == "__main__":
    APP = create_app()
    APP.logger.info("starting pydex...")
    APP.run(host="0.0.0.0", port=3000, debug=True)
