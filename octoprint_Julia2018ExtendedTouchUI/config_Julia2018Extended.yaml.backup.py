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
  Julia3GFilamentSensor:
    extruderRunoutTime: '0.6'
    filamentRunoutTime: '15'
    minExtrudeTime: '10'
    sensorCount: '2'
  _disabled:
  - cura
  announcements:
    channels:
      _important:
        read_until: 1509547500
  discovery:
    model:
      description: Julia 2018 Extended 3D Printer from Fracktal Works
      name: Julia 2018 Extended
      number: 1
      serial: 00001815
      url: www.fracktal.in/julia2018
      vendor: Fracktal Works
      vendorUrl: www.fracktal.in
    publicPort: 80
    upnpUuid: 14fbb42f-66b1-471b-91dc-ca87e4bcbd5b
    zeroConf:
      port: 1234
  firmwareupdater:
    avrdude_path: /usr/bin/avrdude
    check_after_connect: false
  softwareupdate:
    _config_version: 5
    check_providers:
      Julia3GFilament: Julia3GFilament
      Julia3GFilamentSensor: Julia3GFilamentSensor
      Julia3GNeopixel: Julia3GNeopixel
      Julia3GPrintResurrection: Julia3GPrintResurrection
      Julia3GTouchUI: Julia3GTouchUI
      filemanager: filemanager
    checks:
      octoprint:
        checkout_folder: /home/pi/Julia2018ExtendedOctoprint
        prerelease: false

server:
  commands:
    serverRestartCommand: sudo service octoprint restart
    systemRestartCommand: sudo reboot now
    systemShutdownCommand: sudo shutdown now
  firstRun: true
  host: 127.0.0.1
  secretKey: WT1JA4JrYuRnA4Fpr1XFNYXReyDGEeFH
  seenWizards:
    corewizard: null
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
  snapshot: http://127.0.0.1:8080/?action=snapshot
  stream: /webcam/?action=stream






api:
  enabled: true
  key: B508534ED20348F090B4D0AD637D3660
  softwareupdate:
    _config_version: 6
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
  firmwareupdater:
    avrdude_path: /usr/bin/avrdude
    check_after_connect: false
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
    name: Default
    volume:
      custom_box: false
      depth: 250.0
      formFactor: rectangular
      height: 250.0
      origin: lowerleft
      width: 250.0
serial:
  baudrate: 115200
  port: /dev/ttyUSB0
server:
  commands:
    serverRestartCommand: sudo service octoprint restart
    systemRestartCommand: sudo reboot now
    systemShutdownCommand: sudo shutdown now
  firstRun: true
  pluginBlacklist:
    enabled: false
  secretKey: JiXVNP2AHYhOJKt9wv4CruEquOr4Yz78
  seenWizards:
    corewizard: 3
    cura: null
webcam:
  ffmpeg: /usr/bin/avconv
  snapshot: http://127.0.0.1:8080/?action=snapshot
  stream: /webcam/?action=stream
