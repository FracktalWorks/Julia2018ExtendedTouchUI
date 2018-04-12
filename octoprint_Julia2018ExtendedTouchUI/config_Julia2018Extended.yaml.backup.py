api:
  enabled: true
  key: B508534ED20348F090B4D0AD637D3660
appearance:
  name: Fracktal Works Julia 2018 Extended
devel:
  cache:
    enabled: true
    preemptive: true
  stylesheet: css
  virtualPrinter:
    brokenM29: true
    commandBuffer: 4
    echoOnM117: true
    enabled: true
    extendedSdFileList: false
    forceChecksum: false
    hasBed: true
    includeCurrentToolInTemps: true
    includeFilenameInOpened: true
    movementSpeed:
      e: 300
      x: 6000
      y: 6000
      z: 200
    numExtruders: 2
    okAfterResend: false
    okWithLinenumber: false
    repetierStyleResends: false
    repetierStyleTargetTemperature: false
    rxBuffer: 64
    sendWait: false
    smoothieTemperatureReporting: false
    supportM112: true
    throttle: 0.01
    waitInterval: 1
  webassets:
    bundle: true
    clean_on_startup: true
    minify: true
feature:
  sdSupport: false
pluginmanager:
  repository: http://plugins.octoprint.org/plugins.json
plugins:
  _disabled:
  - cura
  announcements:
    _blog: null
    _important: null
    _octopi: null
    _plugins: null
    _releases: null
    channels: null
    read_until: 1523285400
  firmwareupdater:
    avrdude_avrmcu: m2560
    avrdude_baudrate: '115200'
    avrdude_path: /usr/bin/avrdude
    avrdude_programmer: wiring
    check_after_connect: false
    flash_method: avrdude
  softwareupdate:
    _config_version: 6
    check_providers:
      Julia2018ExtendedTouchUI: Julia2018ExtendedTouchUI
      firmwareupdater: firmwareupdater
printerProfiles:
  defaultProfile:
    axes:
      e:
        inverted: false
        speed: 300
      x:
        inverted: false
        speed: 6000
      y:
        inverted: false
        speed: 6000
      z:
        inverted: false
        speed: 200
    color: default
    extruder:
      count: 1
      nozzleDiameter: 0.4
    heatedBed: true
    id: _default
    model: Generic RepRap Printer
    name: Julia 2018 Extended
    volume:
      custom_box: false
      depth: 250.0
      formFactor: rectangular
      height: 250.0
      origin: lowerleft
      width: 300.0
serial:
  autoconnect: true
  baudrate: 115200
  port: /dev/ttyUSB0
server:
  commands:
    serverRestartCommand: sudo service octoprint restart
    systemRestartCommand: sudo reboot now
    systemShutdownCommand: sudo shutdown now
  firstRun: true
  host: 127.0.0.1
  pluginBlacklist:
    enabled: false
  secretKey: 1QM9QG2FnNY6AvLbTZWZ8k6N5L1qKzqk
  seenWizards:
    corewizard: 3
    cura: null
    softwareupdate: null
system:
  actions:
  - action: streamon
    command: /home/pi/scripts/webcam start
    confirm: false
    name: Start video stream
  - action: streamoff
    command: /home/pi/scripts/webcam stop
    confirm: false
    name: Stop video stream
webcam:
  ffmpeg: /usr/bin/avconv
  snapshot: ''
  stream: ''
