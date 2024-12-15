import socketio
import pygame
import socket
import struct
import collections
import sys
import time



# Change the address below to yours
address = 'http://127.0.0.1:9981'

io = socketio.Client()
pygame.mixer.init()
pygame.mixer.set_num_channels(40)
print(pygame.mixer.get_num_channels())

# define channel for techno
techno_bass_1 = pygame.mixer.Sound('./Sound_Tracks/Techno_bass_decreased.MP3')
techno_bass_2 = pygame.mixer.Sound('./Sound_Tracks/Techno_bass_basic.mp3')
techno_bass_3 = pygame.mixer.Sound('./Sound_Tracks/Techno_bass_plus.MP3')
techno_melody_1 = pygame.mixer.Sound('./Sound_Tracks/Techno_melody_soft.MP3')
techno_melody_2 = pygame.mixer.Sound('./Sound_Tracks/Techno_melody_strong.MP3')
techno_drum_1 = pygame.mixer.Sound('./Sound_Tracks/Techno_drum_soft.MP3')
techno_drum_2 = pygame.mixer.Sound('./Sound_Tracks/Techno_drum_strong.MP3')
techno_backing1 = pygame.mixer.Sound('./Sound_Tracks/Techno_backing_soft.MP3')
channel_techno_bass1 = pygame.mixer.Channel(0)
channel_techno_bass2 = pygame.mixer.Channel(1)
channel_techno_bass3 = pygame.mixer.Channel(2)
channel_techno_melody1 = pygame.mixer.Channel(3)
channel_techno_melody2 = pygame.mixer.Channel(4)
channel_techno_drum1 = pygame.mixer.Channel(5)
channel_techno_drum2 = pygame.mixer.Channel(6)
channel_techno_backing1 = pygame.mixer.Channel(28)

# define channel for rock
rock_bass_1 = pygame.mixer.Sound('./Sound_Tracks/Rock_bass_decreased.MP3')
rock_bass_2 = pygame.mixer.Sound('./Sound_Tracks/Rock_bass_basic.MP3')
rock_bass_3 = pygame.mixer.Sound('./Sound_Tracks/Rock_bass_plus.MP3')
rock_backing_1 = pygame.mixer.Sound('./Sound_Tracks/Rock_backing.MP3')
rock_backing_plus = pygame.mixer.Sound('./Sound_Tracks/Rock_backing_plus.MP3')
rock_melody_1 = pygame.mixer.Sound('./Sound_Tracks/rock_melody_soft_long.MP3')
rock_melody_2 = pygame.mixer.Sound('./Sound_Tracks/Rock_melody_strong.MP3')
rock_melody_plus_1 = pygame.mixer.Sound('./Sound_Tracks/Rock_melody_plus_soft.MP3')
rock_melody_plus_2 = pygame.mixer.Sound('./Sound_Tracks/Rock_melody_plus_strong.MP3')
rock_drum_1 = pygame.mixer.Sound('./Sound_Tracks/rock_drum_soft_long.MP3')
rock_drum_2 = pygame.mixer.Sound('./Sound_Tracks/rock_drum_strong_long.MP3')
channel_rock_bass_1 = pygame.mixer.Channel(7)
channel_rock_bass_2 = pygame.mixer.Channel(8)
channel_rock_bass_3 = pygame.mixer.Channel(9)
channel_rock_backing_1 = pygame.mixer.Channel(10)
channel_rock_backing_plus = pygame.mixer.Channel(11)
channel_rock_melody_1 = pygame.mixer.Channel(12)
channel_rock_melody_2 = pygame.mixer.Channel(13)
channel_rock_melody_plus_1 = pygame.mixer.Channel(14)
channel_rock_melody_plus_2 = pygame.mixer.Channel(15)
channel_rock_drum_1 = pygame.mixer.Channel(16)
channel_rock_drum_2 = pygame.mixer.Channel(17)

# define channel for Funk
funk_bass_1 = pygame.mixer.Sound('./Sound_Tracks/funk_bass_decreased.MP3')
funk_bass_2 = pygame.mixer.Sound('./Sound_Tracks/funk_bass_basic.MP3')
funk_bass_3 = pygame.mixer.Sound('./Sound_Tracks/funk_bass_plus.MP3')
funk_backing_1 = pygame.mixer.Sound('./Sound_Tracks/funk_backing_soft.MP3')
funk_backing_plus = pygame.mixer.Sound('./Sound_Tracks/funk_plus_backing_strong.MP3')
funk_melody_1 = pygame.mixer.Sound('./Sound_Tracks/funk_melody_plus_soft.MP3')
funk_melody_plus = pygame.mixer.Sound('./Sound_Tracks/funk_melody_strong.MP3')
funk_drum_1 = pygame.mixer.Sound('./Sound_Tracks/funk_drum_soft.MP3')
funk_drum_2 = pygame.mixer.Sound('./Sound_Tracks/funk_drum_strong.MP3')
channel_funk_bass_1 = pygame.mixer.Channel(18)
channel_funk_bass_2 = pygame.mixer.Channel(19)
channel_funk_bass_3 = pygame.mixer.Channel(20)
channel_funk_backing_1 = pygame.mixer.Channel(21)
channel_funk_backing_plus = pygame.mixer.Channel(22)
channel_funk_melody_1 = pygame.mixer.Channel(23)
channel_funk_melody_2 = pygame.mixer.Channel(24)
channel_funk_drum_1 = pygame.mixer.Channel(25)
channel_funk_drum_2 = pygame.mixer.Channel(26)

# define channel for Reggae
reggae_bass_1 = pygame.mixer.Sound('./Sound_Tracks/Raggae_bass_1.MP3')
reggae_bass_2 = pygame.mixer.Sound('./Sound_Tracks/Raggae_bass_2.MP3')
reggae_bass_3 = pygame.mixer.Sound('./Sound_Tracks/Raggae_bass_4.MP3')
reggae_backing_1 = pygame.mixer.Sound('./Sound_Tracks/Raggae_backing_1.MP3')
reggae_backing_2 = pygame.mixer.Sound('./Sound_Tracks/Raggae_backing_2.MP3')
reggae_drum_1 = pygame.mixer.Sound('./Sound_Tracks/Raggae_drum_1.MP3')
reggae_melody_1 = pygame.mixer.Sound('./Sound_Tracks/Raggae_melody_1.MP3')
reggae_melody_2 = pygame.mixer.Sound('./Sound_Tracks/Raggae_melody_2.MP3')
reggae_backing_plus = pygame.mixer.Sound('./Sound_Tracks/Raggae_backing_plus_1.MP3')
reggae_melody_plus_1 = pygame.mixer.Sound('./Sound_Tracks/Raggae_melody_plus_1.MP3')
reggae_melody_plus_2 = pygame.mixer.Sound('Raggae_melody_plus2.MP3')
reggae_drum_plus_1 = pygame.mixer.Sound('./Sound_Tracks/Raggae_drum_plus_1.MP3')
reggae_drum_plus_2 = pygame.mixer.Sound('./Sound_Tracks/Raggae_drum_plus_2.MP3')
channel_reggae_bass_1 = pygame.mixer.Channel(27)
channel_reggae_bass_2 = pygame.mixer.Channel(28)
channel_reggae_bass_3 = pygame.mixer.Channel(29)
channel_reggae_backing_1 = pygame.mixer.Channel(30)
channel_reggae_backing_2 = pygame.mixer.Channel(31)
channel_reggae_drum_1 = pygame.mixer.Channel(32)
channel_reggae_drum_plus_1 = pygame.mixer.Channel(33)
channel_reggae_drum_plus_2 = pygame.mixer.Channel(39)
channel_reggae_backing_plus = pygame.mixer.Channel(34)
channel_reggae_melody_1 = pygame.mixer.Channel(35)
channel_reggae_melody_2 = pygame.mixer.Channel(36)
channel_reggae_melody_plus_1 = pygame.mixer.Channel(37)
channel_reggae_melody_plus_2 = pygame.mixer.Channel(38)


def update_volume_reggae(driving_setting):
    driving_setting = 0.8 * float(driving_setting)
    channel_reggae_backing_1.set_volume(0)
    channel_reggae_backing_2.set_volume(0)
    channel_reggae_drum_1.set_volume(0)
    channel_reggae_drum_plus_1.set_volume(0)
    channel_reggae_drum_plus_2.set_volume(0)
    channel_reggae_backing_plus.set_volume(0)
    channel_reggae_melody_1.set_volume(0)
    channel_reggae_melody_2.set_volume(0)
    channel_reggae_melody_plus_1.set_volume(0)
    channel_reggae_melody_plus_2.set_volume(0)
    if driving_setting < 41:
        channel_reggae_bass_1.set_volume(1)
        channel_reggae_bass_2.set_volume(0.3 * driving_setting / 100)
        channel_reggae_bass_3.set_volume(0)
    if 40 < driving_setting < 81:
        channel_reggae_bass_1.set_volume(driving_setting / 100)
        channel_reggae_bass_2.set_volume(1)
        if driving_setting < 60:
            channel_reggae_bass_3.set_volume(0)
        else:
            channel_reggae_bass_3.set_volume(0.5 * driving_setting / 100)
    if 80 < driving_setting < 99:
        channel_reggae_bass_1.set_volume(0)
        channel_reggae_bass_2.set_volume(1 - (driving_setting / 100))
        channel_reggae_bass_3.set_volume(driving_setting / 100)
    if driving_setting > 98:
        channel_reggae_bass_3.set_volume(1)


def update_volume_funk(driving_setting):
    driving_setting = 0.8 * float(driving_setting)
    channel_funk_backing_1.set_volume(0)
    channel_funk_backing_plus.set_volume(0)
    channel_funk_melody_1.set_volume(0)
    channel_funk_melody_2.set_volume(0)
    channel_funk_drum_1.set_volume(0)
    channel_funk_drum_2.set_volume(0)
    if driving_setting < 41:
        channel_funk_bass_1.set_volume(1)
        channel_funk_bass_2.set_volume(0.3 * driving_setting / 100)
        channel_funk_bass_3.set_volume(0)
    if 40 < driving_setting < 81:
        channel_funk_bass_1.set_volume(driving_setting / 100)
        channel_funk_bass_2.set_volume(1)
        if driving_setting < 60:
            channel_funk_bass_3.set_volume(0)
        else:
            channel_funk_bass_3.set_volume(0.5 * driving_setting / 100)
    if 80 < driving_setting < 99:
        channel_funk_bass_1.set_volume(0)
        channel_funk_bass_2.set_volume(1 - (driving_setting / 100))
        channel_funk_bass_3.set_volume(driving_setting / 100)
    if driving_setting > 98:
        channel_funk_bass_3.set_volume(1)


def update_volume_techno(driving_setting):
    driving_setting = 0.8 * float(driving_setting)
    channel_techno_melody1.set_volume(0)
    channel_techno_melody2.set_volume(0)
    channel_techno_drum1.set_volume(0)
    channel_techno_drum2.set_volume(0)
    channel_techno_backing1.set_volume(0)

    if driving_setting < 41:
        channel_techno_bass1.set_volume(1)
        channel_techno_bass2.set_volume(0.3 * driving_setting / 100)
        channel_techno_bass3.set_volume(0)
    if 40 < driving_setting < 81:
        channel_techno_bass1.set_volume(driving_setting / 100)
        channel_techno_bass2.set_volume(1)
        if driving_setting < 60:
            channel_techno_bass3.set_volume(0)
        else:
            channel_techno_bass3.set_volume(0.5 * driving_setting / 100)
    if 80 < driving_setting < 99:
        channel_techno_bass1.set_volume(0)
        channel_techno_bass2.set_volume(1 - (driving_setting / 100))
        channel_techno_bass3.set_volume(driving_setting / 100)
    if driving_setting > 98:
        channel_rock_bass_3.set_volume(1)


def init_volume_rock():
    channel_rock_bass_1.set_volume(0)
    channel_rock_bass_2.set_volume(1)
    channel_rock_bass_3.set_volume(0)
    channel_rock_backing_1.set_volume(0)
    channel_rock_backing_plus.set_volume(0)
    channel_rock_melody_1.set_volume(0)
    channel_rock_melody_2.set_volume(0)
    channel_rock_melody_plus_1.set_volume(0)
    channel_rock_melody_plus_2.set_volume(0)
    channel_rock_drum_1.set_volume(0)
    channel_rock_drum_2.set_volume(0)


def update_volume_rock(driving_setting):
    driving_setting = 0.8 * float(driving_setting)
    if driving_setting < 31:
        channel_rock_bass_1.set_volume(1)
        channel_rock_bass_2.set_volume(0.3 * driving_setting / 100)
        channel_rock_bass_3.set_volume(0)
        # print("received")
    if 30 < driving_setting < 91:
        channel_rock_bass_1.set_volume(0)
        channel_rock_bass_2.set_volume(1)
        if driving_setting < 60:
            channel_rock_bass_3.set_volume(0)
        else:
            channel_rock_bass_3.set_volume(0.5 * driving_setting / 100)

    if 90 < driving_setting < 100:
        channel_techno_bass1.set_volume(0)
        channel_techno_bass2.set_volume(1 - (driving_setting / 100))
        channel_techno_bass3.set_volume(driving_setting / 100)


def play_reggae():
    channel_reggae_bass_1.play(reggae_bass_1, loops=-1)
    channel_reggae_bass_2.play(reggae_bass_2, loops=-1)
    channel_reggae_bass_3.play(reggae_bass_3, loops=-1)
    channel_reggae_backing_1.play(reggae_backing_1, loops=-1)
    channel_reggae_backing_2.play(reggae_backing_2, loops=-1)
    channel_reggae_backing_plus.play(reggae_backing_plus, loops=-1)
    channel_reggae_melody_1.play(reggae_melody_1, loops=-1)
    channel_reggae_melody_2.play(reggae_melody_2, loops=-1)
    channel_reggae_melody_plus_1.play(reggae_melody_plus_1, loops=-1)
    channel_reggae_melody_plus_2.play(reggae_melody_plus_2, loops=-1)
    channel_reggae_drum_1.play(reggae_drum_1, loops=-1)
    channel_reggae_drum_plus_1.play(reggae_drum_plus_1, loops=-1)
    channel_reggae_drum_plus_2.play(reggae_drum_plus_2, loops=-1)


def stop_reggae():
    channel_reggae_bass_1.stop()
    channel_reggae_bass_2.stop()
    channel_reggae_bass_3.stop()
    channel_reggae_backing_1.stop()
    channel_reggae_backing_2.stop()
    channel_reggae_backing_plus.stop()
    channel_reggae_melody_1.stop()
    channel_reggae_melody_2.stop()
    channel_reggae_melody_plus_1.stop()
    channel_reggae_melody_plus_2.stop()
    channel_reggae_drum_1.stop()
    channel_reggae_drum_plus_1.stop()
    channel_reggae_drum_plus_2.stop()


def play_rock():
    channel_rock_bass_1.play(rock_bass_1, loops=-1)
    channel_rock_bass_2.play(rock_bass_2, loops=-1)
    channel_rock_bass_3.play(rock_bass_3, loops=-1)
    channel_rock_backing_1.play(rock_backing_1, loops=-1)
    channel_rock_backing_plus.play(rock_backing_plus, loops=-1)
    channel_rock_melody_1.play(rock_melody_1, loops=-1)
    channel_rock_melody_2.play(rock_melody_2, loops=-1)
    channel_rock_melody_plus_1.play(rock_melody_plus_1, loops=-1)
    channel_rock_melody_plus_2.play(rock_melody_plus_2, loops=-1)
    channel_rock_drum_1.play(rock_drum_1, loops=-1)
    channel_rock_drum_2.play(rock_drum_2, loops=-1)


def stop_rock():
    channel_rock_bass_1.stop()
    channel_rock_bass_2.stop()
    channel_rock_bass_3.stop()
    channel_rock_backing_1.stop()
    channel_rock_backing_plus.stop()
    channel_rock_melody_1.stop()
    channel_rock_melody_2.stop()
    channel_rock_melody_plus_1.stop()
    channel_rock_melody_plus_2.stop()
    channel_rock_drum_1.stop()
    channel_rock_drum_2.stop()


def play_techno():
    channel_techno_bass1.play(techno_bass_1, loops=-1)
    channel_techno_bass2.play(techno_bass_2, loops=-1)
    channel_techno_bass3.play(techno_bass_3, loops=-1)
    channel_techno_melody1.play(techno_melody_1, loops=-1)
    channel_techno_melody2.play(techno_melody_2, loops=-1)
    channel_techno_drum1.play(techno_drum_1, loops=-1)
    channel_techno_drum2.play(techno_drum_2, loops=-1)
    channel_techno_backing1.play(techno_backing1, loops=-1)


def stop_techno():
    channel_techno_bass1.stop()
    channel_techno_bass2.stop()
    channel_techno_bass3.stop()
    channel_techno_melody1.stop()
    channel_techno_melody2.stop()
    channel_techno_drum1.stop()
    channel_techno_drum2.stop()
    channel_techno_backing1.stop()


def play_funk():
    channel_funk_bass_1.play(funk_bass_1, loops=-1)
    channel_funk_bass_2.play(funk_bass_2, loops=-1)
    channel_funk_bass_3.play(funk_bass_3, loops=-1)
    channel_funk_backing_1.play(funk_backing_1, loops=-1)
    channel_funk_backing_plus.play(funk_backing_plus, loops=-1)
    channel_funk_melody_1.play(funk_melody_1, loops=-1)
    channel_funk_melody_2.play(funk_melody_1, loops=-1)
    channel_funk_drum_1.play(funk_drum_1, loops=-1)
    channel_funk_drum_2.play(funk_drum_2, loops=-1)


def stop_funk():
    channel_funk_bass_1.stop()
    channel_funk_bass_2.stop()
    channel_funk_bass_3.stop()
    channel_funk_backing_1.stop()
    channel_funk_backing_plus.stop()
    channel_funk_melody_1.stop()
    channel_funk_melody_2.stop()
    channel_funk_drum_1.stop()
    channel_funk_drum_2.stop()


def update_music_reggae(speed):
    speed = int(speed)
    if channel_reggae_bass_3.get_volume() > 0:
        if speed < 11:
            channel_reggae_backing_1.set_volume(0)
            channel_reggae_backing_2.set_volume(0)
            channel_reggae_drum_1.set_volume(0)
            channel_reggae_drum_plus_1.set_volume(0)
            channel_reggae_drum_plus_2.set_volume(0)
            channel_reggae_backing_plus.set_volume(0)
            channel_reggae_melody_1.set_volume(0)
            channel_reggae_melody_2.set_volume(0)
            channel_reggae_melody_plus_1.set_volume(0)
            channel_reggae_melody_plus_2.set_volume(0)
        if 10 < speed < 31:
            channel_reggae_backing_1.set_volume(0)
            channel_reggae_backing_2.set_volume(0)
            channel_reggae_drum_1.set_volume(0)
            channel_reggae_drum_plus_1.set_volume(0)
            channel_reggae_drum_plus_2.set_volume(0)
            channel_reggae_backing_plus.set_volume(1)
            channel_reggae_melody_1.set_volume(0)
            channel_reggae_melody_2.set_volume(0)
            channel_reggae_melody_plus_1.set_volume(0)
            channel_reggae_melody_plus_2.set_volume(0)
        if 30 < speed < 51:
            channel_reggae_backing_1.set_volume(0)
            channel_reggae_backing_2.set_volume(0)
            channel_reggae_drum_1.set_volume(0)
            channel_reggae_drum_plus_1.set_volume(1)
            channel_reggae_drum_plus_2.set_volume(0)
            channel_reggae_melody_1.set_volume(0)
            channel_reggae_melody_2.set_volume(0)
            channel_reggae_melody_plus_1.set_volume(0)
            channel_reggae_melody_plus_2.set_volume(0)
        if 50 < speed < 71:
            channel_reggae_backing_1.set_volume(0)
            channel_reggae_backing_2.set_volume(0)
            channel_reggae_drum_1.set_volume(0)
            channel_reggae_drum_plus_2.set_volume(0)
            channel_reggae_melody_1.set_volume(0)
            channel_reggae_melody_2.set_volume(0)
            channel_reggae_melody_plus_1.set_volume(0.4)
            channel_reggae_melody_plus_2.set_volume(0)
        if 70 < speed < 81:
            channel_reggae_backing_1.set_volume(0)
            channel_reggae_backing_2.set_volume(0)
            channel_reggae_drum_1.set_volume(0)
            channel_reggae_drum_plus_2.set_volume(1)
            channel_reggae_melody_1.set_volume(0)
            channel_reggae_melody_2.set_volume(0)
            channel_reggae_melody_plus_2.set_volume(0)
        if speed > 80:
            channel_reggae_backing_1.set_volume(0)
            channel_reggae_backing_2.set_volume(0)
            channel_reggae_drum_1.set_volume(0)
            channel_reggae_melody_1.set_volume(0)
            channel_reggae_melody_2.set_volume(0)
            channel_reggae_melody_plus_2.set_volume(0.6)

    else:
        if speed < 10:
            channel_reggae_backing_1.set_volume(0)
            channel_reggae_backing_2.set_volume(0)
            channel_reggae_drum_1.set_volume(0)
            channel_reggae_drum_plus_1.set_volume(0)
            channel_reggae_drum_plus_2.set_volume(0)
            channel_reggae_backing_plus.set_volume(0)
            channel_reggae_melody_1.set_volume(0)
            channel_reggae_melody_2.set_volume(0)
            channel_reggae_melody_plus_1.set_volume(0)
            channel_reggae_melody_plus_2.set_volume(0)
        if 9 < speed < 31:
            channel_reggae_backing_1.set_volume(1)
            channel_reggae_backing_2.set_volume(0)
            channel_reggae_drum_1.set_volume(0)
            channel_reggae_drum_plus_1.set_volume(0)
            channel_reggae_drum_plus_2.set_volume(0)
            channel_reggae_backing_plus.set_volume(0)
            channel_reggae_melody_1.set_volume(0)
            channel_reggae_melody_2.set_volume(0)
            channel_reggae_melody_plus_1.set_volume(0)
            channel_reggae_melody_plus_2.set_volume(0)
        if 30 < speed < 51:
            channel_reggae_backing_2.set_volume(0)
            channel_reggae_drum_1.set_volume(1)
            channel_reggae_drum_plus_1.set_volume(0)
            channel_reggae_drum_plus_2.set_volume(0)
            channel_reggae_backing_plus.set_volume(0)
            channel_reggae_melody_1.set_volume(0)
            channel_reggae_melody_2.set_volume(0)
            channel_reggae_melody_plus_1.set_volume(0)
            channel_reggae_melody_plus_2.set_volume(0)
        if 50 < speed < 71:
            channel_reggae_backing_2.set_volume(0)
            channel_reggae_drum_plus_1.set_volume(0)
            channel_reggae_backing_plus.set_volume(0)
            channel_reggae_drum_plus_2.set_volume(0)
            channel_reggae_melody_1.set_volume(1)
            channel_reggae_melody_2.set_volume(0)
            channel_reggae_melody_plus_1.set_volume(0)
            channel_reggae_melody_plus_2.set_volume(0)
        if 70 < speed < 81:
            channel_reggae_backing_2.set_volume(1)
            channel_reggae_drum_plus_1.set_volume(0)
            channel_reggae_drum_plus_2.set_volume(0)
            channel_reggae_backing_plus.set_volume(0)
            channel_reggae_melody_2.set_volume(0)
            channel_reggae_melody_plus_1.set_volume(0)
            channel_reggae_melody_plus_2.set_volume(0)
        if speed > 80:
            channel_reggae_drum_plus_1.set_volume(0)
            channel_reggae_drum_plus_2.set_volume(0)
            channel_reggae_backing_plus.set_volume(0)
            channel_reggae_melody_2.set_volume(1)
            channel_reggae_melody_plus_1.set_volume(1)
            channel_reggae_melody_plus_2.set_volume(0)


def update_music_techno(speed):
    speed = int(speed)
    if speed < 10:
        channel_techno_drum1.set_volume(0)
        channel_techno_melody1.set_volume(0)
        channel_techno_melody2.set_volume(0)
        channel_techno_drum2.set_volume(0)
        channel_techno_backing1.set_volume(0)
    if 9 < speed < 31:
        channel_techno_drum1.set_volume(1)
        channel_techno_melody1.set_volume(0)
        channel_techno_melody2.set_volume(0)
        channel_techno_drum2.set_volume(0)
        channel_techno_backing1.set_volume(0)
    if 30 < speed < 51:
        channel_techno_melody1.set_volume(1)
        channel_techno_melody2.set_volume(0)
        channel_techno_drum2.set_volume(0)
        channel_techno_backing1.set_volume(0)
    if 50 < speed < 71:
        channel_techno_melody2.set_volume(0.7)
        channel_techno_drum2.set_volume(0)
        channel_techno_backing1.set_volume(0)
    if 70 < speed < 80:
        channel_techno_drum2.set_volume(1)
        channel_techno_backing1.set_volume(0)
    if speed > 80:
        channel_techno_backing1.set_volume(1)


def update_music_rock(speed):
    speed = float(speed)
    if speed < 11:
        channel_rock_backing_plus.set_volume(0)
        channel_rock_backing_1.set_volume(0)
        channel_rock_melody_1.set_volume(0)
        channel_rock_melody_2.set_volume(0)
        channel_rock_melody_plus_1.set_volume(0)
        channel_rock_melody_plus_2.set_volume(0)
        channel_rock_drum_1.set_volume(0)
        channel_rock_drum_2.set_volume(0)
    if 10 < speed < 31:
        channel_rock_backing_plus.set_volume(0)
        channel_rock_backing_1.set_volume(0)
        channel_rock_melody_1.set_volume(0)
        channel_rock_melody_2.set_volume(0)
        channel_rock_melody_plus_1.set_volume(0)
        channel_rock_melody_plus_2.set_volume(0)
        channel_rock_drum_1.set_volume(0.8)
        channel_rock_drum_2.set_volume(0)
    if 30 < speed < 51:
        channel_rock_drum_1.set_volume(0.5)
        channel_rock_backing_plus.set_volume(0)
        channel_rock_backing_1.set_volume(0)
        channel_rock_melody_1.set_volume(1)
        channel_rock_melody_2.set_volume(0)
        channel_rock_melody_plus_1.set_volume(0)
        channel_rock_melody_plus_2.set_volume(0)
        channel_rock_drum_2.set_volume(0)
    if 50 < speed < 71:
        channel_rock_backing_plus.set_volume(0.4)
        channel_rock_backing_1.set_volume(0)
        channel_rock_melody_2.set_volume(0)
        channel_rock_melody_plus_1.set_volume(0)
        channel_rock_melody_plus_2.set_volume(0)
        channel_rock_drum_2.set_volume(0)
    if 70 < speed < 81:
        channel_rock_backing_1.set_volume(0)
        channel_rock_melody_2.set_volume(0.6)
        channel_rock_melody_plus_1.set_volume(0)
        channel_rock_melody_plus_2.set_volume(0)
        channel_rock_drum_2.set_volume(0)
    if 80 < speed < 91:
        channel_rock_backing_1.set_volume(0)
        channel_rock_melody_plus_1.set_volume(0.5)
        channel_rock_melody_plus_2.set_volume(0)
        channel_rock_drum_2.set_volume(1)
    if speed > 90:
        channel_rock_backing_1.set_volume(0)
        channel_rock_melody_plus_1.set_volume(1)
        channel_rock_melody_plus_2.set_volume(0)


def update_music_funk(speed):
    speed = float(speed)
    if speed < 11:
        channel_funk_backing_1.set_volume(0)
        channel_funk_backing_plus.set_volume(0)
        channel_funk_melody_1.set_volume(0)
        channel_funk_melody_2.set_volume(0)
        channel_funk_drum_1.set_volume(0)
        channel_funk_drum_2.set_volume(0)
    if 10 < speed < 31:
        channel_funk_backing_1.set_volume(0)
        channel_funk_backing_plus.set_volume(0)
        channel_funk_melody_1.set_volume(0)
        channel_funk_melody_2.set_volume(0)
        channel_funk_drum_1.set_volume(0.7 * speed)
        channel_funk_drum_2.set_volume(0)
    if 30 < speed < 51:
        channel_funk_backing_plus.set_volume(0)
        channel_funk_melody_1.set_volume(1)
        channel_funk_melody_2.set_volume(0)
        channel_funk_drum_1.set_volume(1)
        channel_funk_drum_2.set_volume(0)
    if 50 < speed < 71:
        channel_funk_backing_plus.set_volume(0)
        channel_funk_melody_2.set_volume(0)
        channel_funk_drum_2.set_volume(1)
    if 70 < speed < 81:
        channel_funk_backing_plus.set_volume(0)
        channel_funk_melody_2.set_volume(1)
    if speed > 80:
        channel_funk_backing_plus.set_volume(0.7 * speed)


# def update_acc(speed):
#     speed_pre = 0
#     time.sleep(0.5)
#     speed_cur = speed
#     acc = speed_cur - speed_pre
#     speed_pre = speed_cur
#     io.emit('ppMessage', {'messageId': "ACC", 'value': acc})
#     time.sleep(0.5)



@io.on('connect')
def on_connect():
    print('[SOCKERIO] Connected to server')
    io.emit('ppBridgeApp', {'name': 'python'})


@io.on('ppMessage')
def on_message(data):
    message_id = data['messageId']
    value = data['value'] if 'value' in data else None
    print('[SOCKERIO] Receive a Message from connect', data)

    speed_pre = 0

    # game initially start with rock
    if message_id == "START":
        init_volume_rock()

    if message_id == "SETTING_RAGGAE":
        update_volume_reggae(driving_setting=value)

    if message_id == "SETTING_TECHNO":
        update_volume_techno(driving_setting=value)

    if message_id == "SETTING_ROCK":
        update_volume_rock(driving_setting=value)

    if message_id == "SETTING_FUNK":
        update_volume_funk(driving_setting=value)

    if message_id == "PLAY_RAGGAE":
        update_volume_reggae(driving_setting=value)
        play_reggae()

    if message_id == "PLAY_TECHNO":
        update_volume_techno(driving_setting=value)
        play_techno()

    if message_id == "PLAY_ROCK":
        play_rock()

    if message_id == "PLAY_FUNK":
        update_volume_funk(driving_setting=value)
        play_funk()

    if message_id == "STOP_FUNK":
        stop_funk()

    if message_id == "STOP_TECHNO":
        stop_techno()

    if message_id == "STOP_ROCK":
        stop_rock()

    if message_id == "STOP_RAGGAE":
        stop_reggae()

    if message_id == "speed_techno":
        update_music_techno(speed=value)

    if message_id == "speed_rock":
        update_music_rock(speed=value)

    if message_id == "speed_funk":
        update_music_funk(speed=value)

    if message_id == "speed_reggae":
        update_music_reggae(speed=value)

    # if message_id == "SEND_SPEED":
    #     speed_cur = float(value)
    #     acc = speed_cur - speed_pre
    #     io.emit('ppMessage', {'messageId': "ACC", 'value': acc})
    #     time.sleep(0.5)
    #     speed_pre = speed_cur
    #     print(speed_pre, speed_cur)



io.connect(address)
io.wait()
