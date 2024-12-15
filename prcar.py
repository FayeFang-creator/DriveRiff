speed_cur = 0
speed_pre = 0

# Change the address below to yours
address = 'http://127.0.0.1:9981'

io = socketio.Client()


@io.on('connect')
def on_connect():
    print('[SOCKERIO] Connected to server')
    io.emit('ppBridgeApp', {'name': 'python'})


@io.on('ppMessage')
def on_message(data):
    messageId = data['messageId']
    value = data['value'] if 'value' in data else None
    print('[SOCKERIO] Receive a Message from connect', data)
    if (messageId == "PLAY_MUSIC"):
        play_music()
    if (messageId == "STOP_MUSIC"):
        stop_music()
    if (messageId == "SPEED"):
        update_music(value)


io.connect(address)

# PCars = collections.namedtuple('PCars',
#                                'buildVersionNumber packetType gameSessionState viewedParticipantIndex numParticipants unfilteredThrottle unfilteredBrake unfilteredSteering unfilteredClutch raceStateFlags lapsInEvent bestLapTime lastLapTime currentTime splitTimeAhead splitTimeBehind splitTime eventTimeRemaining personalFastestLapTime worldFastestLapTime currentSector1Time currentSector2Time currentSector3Time fastestSector1Time fastestSector2Time fastestSector3Time personalFastestSector1Time personalFastestSector2Time personalFastestSector3Time worldFastestSector1Time worldFastestSector2Time worldFastestSector3Time joyPad highestFlag pitModeSchedule oilTempCelsius oilPressureKPa waterTempCelsius waterPressureKpa fuelPressureKpa carFlags fuelCapacity brake throttle clutch steering fuelLevel speed rpm maxRpm gearNumGears boostAmount enforcedPitStopLap crashState odometerKM orientation localVelocity worldVelocity angularVelocity localAcceleration worldAcceleration extentsCentre tyreFlags terrain tyreY tyreRPS tyreSlipSpeed tyreTemp tyreGrip tyreHeightAboveGround tyreLateralStiffness tyreWear brakeDamage suspensionDamage brakeTempCelsius tyreTreadTemp tyreLayerTemp tyreCarcassTemp tyreRimTemp tyreInternalAirTemp wheelLocalPositionY rideHeight suspensionTravel suspensionVelocity airPressure engineSpeed engineTorque aeroDamage engineDamage ambientTemperature trackTemperature rainDensity windSpeed windDirectionX windDirectionY trackLength wings dPad')

# s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# s.bind(("0.0.0.0", 5606))

pygame.mixer.init()
bass = pygame.mixer.Sound('bass_long.MP3')
melody = pygame.mixer.Sound('melody_soft_long.MP3')
drum = pygame.mixer.Sound('drum-long.MP3')
channel1 = pygame.mixer.Channel(0)
channel2 = pygame.mixer.Channel(1)
channel3 = pygame.mixer.Channel(2)


def play_music():
    # Starting the mixer
    channel1.set_volume(0.5)
    channel2.set_volume(0)
    channel3.set_volume(0)
    channel1.play(bass, loops=-1)
    channel2.play(melody, loops=-1)
    channel3.play(drum, loops=-1)


def update_music(speed):
    # speed = int(speed)
    channel3.set_volume(speed / 260)
    if (0 < speed <= 30):
        channel1.set_volume(0.5)
        channel2.set_volume(0)
    if (30 < speed <= 100):
        channel1.set_volume(0.5)
        channel2.set_volume(0.6)
    if (100 < speed <= 150):
        channel1.set_volume(1)
        channel2.set_volume(1)


def stop_music():
    pygame.mixer.stop()

while True:
    dat, adr = s.recvfrom(2048)
    # pcars = PCars(*struct.unpack('HBBbbBBbBBBfffffffffffffffffffffHBBhHhHHBBBBBbffHHBBbBffffffffBBfffBBffBBBhHHHHHffffHffBBbbBbbbfBB', dat[0:250]))
    # # print(pcars)
    # speed_cur = pcars.speed*3.6/1.6 # comes in m/s, multiply to convert to metric (km/h)
    acc = (speed_cur - speed_pre)/0.2 # actually fake
    if (acc > 30 ):
        acc = 30
    if (acc < -30 ):
        acc = -30

    print("speed = " ,speed_cur)
    print("acc = ", acc)
    print("-----------------")

    update_music(speed_cur)

    io.emit('ppMessage', {'messageId':"SPEED", 'value':speed_cur})
    io.emit('ppMessage', {'messageId':"ACC", 'value':acc})
    speed_pre = speed_cur


# while True:
#     dat, adr = s.recvfrom(2048)
#     pcars = PCars(*struct.unpack('HBBbbBBbBBBfffffffffffffffffffffHBBhHhHHBBBBBbffHHBBbBffffffffBBfffBBffBBBhHHHHHffffHffBBbbBbbbfBB', dat[0:250]))
#     # print(pcars)
#     speed_cur = pcars.speed*3.6/1.6 # comes in m/s, multiply to convert to metric (km/h)
#     acc = (speed_cur - speed_pre)/0.2 # actually fake
#     if ( acc > 30 ):
#         acc = 30
#     if (acc < -30 ):
#         acc = -30

#     print("speed = " ,speed_cur)
#     print("acc = ", acc)
#     print("-----------------")

#     update_music(speed_cur)

#     io.emit('ppMessage', {'messageId':"SPEED", 'value':speed_cur})
#     io.emit('ppMessage', {'messageId':"ACC", 'value':acc})
#     speed_pre = speed_cur

# s.close()