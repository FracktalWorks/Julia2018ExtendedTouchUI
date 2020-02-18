# coding=utf-8
from __future__ import absolute_import

import octoprint.plugin
# import time
# import subprocess
# from threading import Timer

# class RepeatedTimer(object):
# 	def __init__(self, interval, function, *args, **kwargs):
# 		self._timer = None
# 		self.interval = interval
# 		self.function = function
# 		self.args = args
# 		self.kwargs = kwargs
# 		self.is_running = False
#
# 	def _run(self):
# 		self.is_running = False
# 		self.start()
# 		self.function(*self.args, **self.kwargs)
#
# 	def start(self):
# 		if not self.is_running:
# 			self._timer = Timer(self.interval, self._run)
# 			self._timer.start()
# 			self.is_running = True
#
# 	def stop(self):
# 		if self.is_running:
# 			self._timer.cancel()
# 			self.is_running = False


class Julia2018ExtendedTouchUI(octoprint.plugin.StartupPlugin):
    def on_after_startup(self):
        # self.resetInetrval = int(self._settings.get(["resetInetrval"]))
        self._logger.info("TouchUI Plugin Started")
        # self._worker = RepeatedTimer(self.resetInetrval, self.worker)
        # self._worker.start()

    # def worker(self):
    # 	self._logger.info("Restarting Touch driver ...")
    # 	subprocess.call(["sudo", "modprobe", "-r", "ads7846"], shell=False)
    # 	time.sleep(0.1)
    # 	subprocess.call(["sudo", "modprobe", "ads7846"], shell=False)
    # 	self._logger.info("Touch driver restarted")
    #
    # def get_settings_defaults(self):
    # 	'''
    # 	initialises default parameters
    # 	:return:
    # 	'''
    # 	return dict(
    # 		resetInetrval=2
    # 		)

    def get_update_information(self):
        return dict(
            Julia2018ExtendedTouchUI=dict(
                displayName="Julia2018ExtendedTouchUI",
                displayVersion=self._plugin_version,
                # version check: github repository
                type="github_release",
                user="FracktalWorks",
                repo="Julia2018ExtendedTouchUI",
                current=self._plugin_version,

                # update method: pip
                pip="https://github.com/FracktalWorks/Julia2018ExtendedTouchUI/archive/{target_version}.zip"
            )
        )


__plugin_name__ = "Julia Extended Touch UI"
__plugin_version__ = "1.2.0"


def __plugin_load__():
    global __plugin_implementation__
    __plugin_implementation__ = Julia2018ExtendedTouchUI()

    global __plugin_hooks__
    __plugin_hooks__ = {
        "octoprint.plugin.softwareupdate.check_config": __plugin_implementation__.get_update_information
    }
