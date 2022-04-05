import atexit
import signal

from app.controllers.platform_controller import PlatformController

platform_controller = PlatformController()
platform_controller.start_threads()

atexit.register(platform_controller.cleanup)
signal.signal(signal.SIGTERM, platform_controller.cleanup)
