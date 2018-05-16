#!/usr/bin/env python
# -*- coding: utf-8 -*-

################################################################################
# Copyright 2017 ROBOTIS CO., LTD.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
################################################################################

# Author: Ryu Woon Jung (Leon)

import ctypes
from ctypes import cdll
# dxl_lib = cdll.LoadLibrary("../../c/build/win32/output/dxl_x86_c.dll")  # for windows 32bit
# dxl_lib = cdll.LoadLibrary("../../c/build/win64/output/dxl_x64_c.dll")  # for windows 64bit
# dxl_lib = cdll.LoadLibrary("../../c/build/linux32/libdxl_x86_c.so")     # for linux 32bit
dxl_lib = cdll.LoadLibrary("libdxl_x64_c.so")     # for linux 64bit
# dxl_lib = cdll.LoadLibrary("../../c/build/linux_sbc/libdxl_sbc_c.so")   # for SBC linux
# dxl_lib = cdll.LoadLibrary("../../c/build/mac/libdxl_mac_c.dylib")      # for Mac OS

# port_handler
portHandler = dxl_lib.portHandler

openPort = dxl_lib.openPort
closePort = dxl_lib.closePort
clearPort = dxl_lib.clearPort

setPortName = dxl_lib.setPortName
getPortName = dxl_lib.getPortName

setBaudRate = dxl_lib.setBaudRate
getBaudRate = dxl_lib.getBaudRate

readPort = dxl_lib.readPort
writePort = dxl_lib.writePort

setPacketTimeout = dxl_lib.setPacketTimeout
setPacketTimeoutMSec = dxl_lib.setPacketTimeoutMSec
isPacketTimeout = dxl_lib.isPacketTimeout

# packet_handler
packetHandler = dxl_lib.packetHandler

printTxRxResult = dxl_lib.printTxRxResult
getTxRxResult = dxl_lib.getTxRxResult
getTxRxResult.restype = ctypes.c_char_p
printRxPacketError = dxl_lib.printRxPacketError
getRxPacketError = dxl_lib.getRxPacketError
getRxPacketError.restype = ctypes.c_char_p

getLastTxRxResult = dxl_lib.getLastTxRxResult
getLastRxPacketError = dxl_lib.getLastRxPacketError

setDataWrite = dxl_lib.setDataWrite
getDataRead = dxl_lib.getDataRead

txPacket = dxl_lib.txPacket

rxPacket = dxl_lib.rxPacket

txRxPacket = dxl_lib.txRxPacket

ping = dxl_lib.ping

pingGetModelNum = dxl_lib.pingGetModelNum

broadcastPing = dxl_lib.broadcastPing
getBroadcastPingResult = dxl_lib.getBroadcastPingResult

reboot = dxl_lib.reboot

factoryReset = dxl_lib.factoryReset

readTx = dxl_lib.readTx
readRx = dxl_lib.readRx
readTxRx = dxl_lib.readTxRx

read1ByteTx = dxl_lib.read1ByteTx
read1ByteRx = dxl_lib.read1ByteRx
read1ByteTxRx = dxl_lib.read1ByteTxRx

read2ByteTx = dxl_lib.read2ByteTx
read2ByteRx = dxl_lib.read2ByteRx
read2ByteTxRx = dxl_lib.read2ByteTxRx

read4ByteTx = dxl_lib.read4ByteTx
read4ByteRx = dxl_lib.read4ByteRx
read4ByteTxRx = dxl_lib.read4ByteTxRx

writeTxOnly = dxl_lib.writeTxOnly
writeTxRx = dxl_lib.writeTxRx

write1ByteTxOnly = dxl_lib.write1ByteTxOnly
write1ByteTxRx = dxl_lib.write1ByteTxRx

write2ByteTxOnly = dxl_lib.write2ByteTxOnly
write2ByteTxRx = dxl_lib.write2ByteTxRx

write4ByteTxOnly = dxl_lib.write4ByteTxOnly
write4ByteTxRx = dxl_lib.write4ByteTxRx

regWriteTxOnly = dxl_lib.regWriteTxOnly
regWriteTxRx = dxl_lib.regWriteTxRx

syncReadTx = dxl_lib.syncReadTx
# syncReadRx   -> GroupSyncRead
# syncReadTxRx -> GroupSyncRead

syncWriteTxOnly = dxl_lib.syncWriteTxOnly

bulkReadTx = dxl_lib.bulkReadTx
# bulkReadRx   -> GroupBulkRead
# bulkReadTxRx -> GroupBulkRead

bulkWriteTxOnly = dxl_lib.bulkWriteTxOnly

# group_bulk_read
groupBulkRead = dxl_lib.groupBulkRead

groupBulkReadAddParam = dxl_lib.groupBulkReadAddParam
groupBulkReadRemoveParam = dxl_lib.groupBulkReadRemoveParam
groupBulkReadClearParam = dxl_lib.groupBulkReadClearParam

groupBulkReadTxPacket = dxl_lib.groupBulkReadTxPacket
groupBulkReadRxPacket = dxl_lib.groupBulkReadRxPacket
groupBulkReadTxRxPacket = dxl_lib.groupBulkReadTxRxPacket

groupBulkReadIsAvailable = dxl_lib.groupBulkReadIsAvailable
groupBulkReadGetData = dxl_lib.groupBulkReadGetData

#group_bulk_write
groupBulkWrite = dxl_lib.groupBulkWrite

groupBulkWriteAddParam = dxl_lib.groupBulkWriteAddParam
groupBulkWriteRemoveParam = dxl_lib.groupBulkWriteRemoveParam
groupBulkWriteChangeParam = dxl_lib.groupBulkWriteChangeParam
groupBulkWriteClearParam = dxl_lib.groupBulkWriteClearParam

groupBulkWriteTxPacket = dxl_lib.groupBulkWriteTxPacket

#group_sync_read
groupSyncRead = dxl_lib.groupSyncRead

groupSyncReadAddParam = dxl_lib.groupSyncReadAddParam
groupSyncReadRemoveParam = dxl_lib.groupSyncReadRemoveParam
groupSyncReadClearParam = dxl_lib.groupSyncReadClearParam

groupSyncReadTxPacket = dxl_lib.groupSyncReadTxPacket
groupSyncReadRxPacket = dxl_lib.groupSyncReadRxPacket
groupSyncReadTxRxPacket = dxl_lib.groupSyncReadTxRxPacket

groupSyncReadIsAvailable = dxl_lib.groupSyncReadIsAvailable
groupSyncReadGetData = dxl_lib.groupSyncReadGetData

#group_sync_write
groupSyncWrite = dxl_lib.groupSyncWrite

groupSyncWriteAddParam = dxl_lib.groupSyncWriteAddParam
groupSyncWriteRemoveParam = dxl_lib.groupSyncWriteRemoveParam
groupSyncWriteChangeParam = dxl_lib.groupSyncWriteChangeParam
groupSyncWriteClearParam = dxl_lib.groupSyncWriteClearParam

groupSyncWriteTxPacket = dxl_lib.groupSyncWriteTxPacket


# Constants

ADDR_MODEL_NUMBER = 0
ADDR_FIRMWARE_VERSION = 2
ADDR_ID = 3
ADDR_BAUD_RATE = 4
ADDR_RETURN_DELAY_TIME = 5
ADDR_CW_ANGLE_LIMIT = 6
ADDR_CCW_ANGLE_LIMIT = 8
ADDR_TEMPERATURE_LIMIT = 11
ADDR_MIN_VOLTAGE_LIMIT = 12
ADDR_MAX_VOLTAGE_LIMIT = 13
ADDR_MAX_TORQUE = 14
ADDR_STATUS_RETURN_LEVEL = 16
ADDR_ALARM_LED = 17
ADDR_SHUTDOWN_INFO = 18
ADDR_MULTI_TURN_OFFSET = 20
ADDR_RESOLUTION_DIVIDER = 20
ADDR_TORQUE_ENABLE = 24
ADDR_LED = 23
ADDR_D_GAIN = 26
ADDR_I_GAIN = 27
ADDR_P_GAIN = 28
ADDR_GOAL_POSITION = 30
ADDR_MOVING_SPEED = 32
ADDR_TORQUE_LIMIT = 34
ADDR_PRESENT_POSITION = 36
ADDR_PRESENT_SPEED = 38
ADDR_PRESENT_LOAD = 40
ADDR_PRESENT_VOLTAGE = 42
ADDR_PRESENT_TEMPERATURE = 43
ADDR_REGISTERED = 44
ADDR_MOVING = 46
ADDR_LOCK = 47
ADDR_PUNCH = 48
ADDR_REALTIME_TICK = 50
ADDR_GOAL_ACCELERATION = 73

LEN_MODEL_NUMBER = 1
LEN_FIRMWARE_VERSION = 1
LEN_ID = 1
LEN_BAUD_RATE = 1
LEN_RETURN_DELAY_TIME = 1
LEN_CW_ANGLE_LIMIT = 2
LEN_CCW_ANGLE_LIMIT = 2
LEN_TEMPERATURE_LIMIT = 1
LEN_MIN_VOLTAGE_LIMIT = 1
LEN_MAX_VOLTAGE_LIMIT = 1
LEN_MAX_TORQUE = 2
LEN_STATUS_RETURN_LEVEL = 1
LEN_ALARM_LED = 1
LEN_SHUTDOWN_INFO = 1
LEN_MULTI_TURN_OFFSET = 2
LEN_RESOLUTION_DIVIDER = 1
LEN_TORQUE_ENABLE = 1
LEN_LED = 1
LEN_D_GAIN = 1
LEN_I_GAIN = 1
LEN_P_GAIN = 1
LEN_GOAL_POSITION = 2
LEN_MOVING_SPEED = 2
LEN_TORQUE_LIMIT = 2
LEN_PRESENT_POSITION = 2
LEN_PRESENT_SPEED = 2
LEN_PRESENT_LOAD = 2
LEN_PRESENT_VOLTAGE = 1
LEN_PRESENT_TEMPERATURE = 1
LEN_REGISTERED = 1
LEN_MOVING = 1
LEN_LOCK = 1
LEN_PUNCH = 2
LEN_REALTIME_TICK = 2
LEN_GOAL_ACCELERATION = 1
