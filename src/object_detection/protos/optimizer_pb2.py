# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: object_detection/protos/optimizer.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\'object_detection/protos/optimizer.proto\x12\x17object_detection.protos\"\xb5\x02\n\tOptimizer\x12G\n\x12rms_prop_optimizer\x18\x01 \x01(\x0b\x32).object_detection.protos.RMSPropOptimizerH\x00\x12H\n\x12momentum_optimizer\x18\x02 \x01(\x0b\x32*.object_detection.protos.MomentumOptimizerH\x00\x12@\n\x0e\x61\x64\x61m_optimizer\x18\x03 \x01(\x0b\x32&.object_detection.protos.AdamOptimizerH\x00\x12 \n\x12use_moving_average\x18\x04 \x01(\x08:\x04true\x12$\n\x14moving_average_decay\x18\x05 \x01(\x02:\x06\x30.9999B\x0b\n\toptimizer\"\x9f\x01\n\x10RMSPropOptimizer\x12<\n\rlearning_rate\x18\x01 \x01(\x0b\x32%.object_detection.protos.LearningRate\x12%\n\x18momentum_optimizer_value\x18\x02 \x01(\x02:\x03\x30.9\x12\x12\n\x05\x64\x65\x63\x61y\x18\x03 \x01(\x02:\x03\x30.9\x12\x12\n\x07\x65psilon\x18\x04 \x01(\x02:\x01\x31\"x\n\x11MomentumOptimizer\x12<\n\rlearning_rate\x18\x01 \x01(\x0b\x32%.object_detection.protos.LearningRate\x12%\n\x18momentum_optimizer_value\x18\x02 \x01(\x02:\x03\x30.9\"M\n\rAdamOptimizer\x12<\n\rlearning_rate\x18\x01 \x01(\x0b\x32%.object_detection.protos.LearningRate\"\x80\x03\n\x0cLearningRate\x12O\n\x16\x63onstant_learning_rate\x18\x01 \x01(\x0b\x32-.object_detection.protos.ConstantLearningRateH\x00\x12`\n\x1f\x65xponential_decay_learning_rate\x18\x02 \x01(\x0b\x32\x35.object_detection.protos.ExponentialDecayLearningRateH\x00\x12T\n\x19manual_step_learning_rate\x18\x03 \x01(\x0b\x32/.object_detection.protos.ManualStepLearningRateH\x00\x12V\n\x1a\x63osine_decay_learning_rate\x18\x04 \x01(\x0b\x32\x30.object_detection.protos.CosineDecayLearningRateH\x00\x42\x0f\n\rlearning_rate\"4\n\x14\x43onstantLearningRate\x12\x1c\n\rlearning_rate\x18\x01 \x01(\x02:\x05\x30.002\"\x97\x01\n\x1c\x45xponentialDecayLearningRate\x12$\n\x15initial_learning_rate\x18\x01 \x01(\x02:\x05\x30.002\x12\x1c\n\x0b\x64\x65\x63\x61y_steps\x18\x02 \x01(\r:\x07\x34\x30\x30\x30\x30\x30\x30\x12\x1a\n\x0c\x64\x65\x63\x61y_factor\x18\x03 \x01(\x02:\x04\x30.95\x12\x17\n\tstaircase\x18\x04 \x01(\x08:\x04true\"\xf1\x01\n\x16ManualStepLearningRate\x12$\n\x15initial_learning_rate\x18\x01 \x01(\x02:\x05\x30.002\x12V\n\x08schedule\x18\x02 \x03(\x0b\x32\x44.object_detection.protos.ManualStepLearningRate.LearningRateSchedule\x12\x15\n\x06warmup\x18\x03 \x01(\x08:\x05\x66\x61lse\x1a\x42\n\x14LearningRateSchedule\x12\x0c\n\x04step\x18\x01 \x01(\r\x12\x1c\n\rlearning_rate\x18\x02 \x01(\x02:\x05\x30.002\"\xbe\x01\n\x17\x43osineDecayLearningRate\x12!\n\x12learning_rate_base\x18\x01 \x01(\x02:\x05\x30.002\x12\x1c\n\x0btotal_steps\x18\x02 \x01(\r:\x07\x34\x30\x30\x30\x30\x30\x30\x12$\n\x14warmup_learning_rate\x18\x03 \x01(\x02:\x06\x30.0002\x12\x1b\n\x0cwarmup_steps\x18\x04 \x01(\r:\x05\x31\x30\x30\x30\x30\x12\x1f\n\x14hold_base_rate_steps\x18\x05 \x01(\r:\x01\x30')



_OPTIMIZER = DESCRIPTOR.message_types_by_name['Optimizer']
_RMSPROPOPTIMIZER = DESCRIPTOR.message_types_by_name['RMSPropOptimizer']
_MOMENTUMOPTIMIZER = DESCRIPTOR.message_types_by_name['MomentumOptimizer']
_ADAMOPTIMIZER = DESCRIPTOR.message_types_by_name['AdamOptimizer']
_LEARNINGRATE = DESCRIPTOR.message_types_by_name['LearningRate']
_CONSTANTLEARNINGRATE = DESCRIPTOR.message_types_by_name['ConstantLearningRate']
_EXPONENTIALDECAYLEARNINGRATE = DESCRIPTOR.message_types_by_name['ExponentialDecayLearningRate']
_MANUALSTEPLEARNINGRATE = DESCRIPTOR.message_types_by_name['ManualStepLearningRate']
_MANUALSTEPLEARNINGRATE_LEARNINGRATESCHEDULE = _MANUALSTEPLEARNINGRATE.nested_types_by_name['LearningRateSchedule']
_COSINEDECAYLEARNINGRATE = DESCRIPTOR.message_types_by_name['CosineDecayLearningRate']
Optimizer = _reflection.GeneratedProtocolMessageType('Optimizer', (_message.Message,), {
  'DESCRIPTOR' : _OPTIMIZER,
  '__module__' : 'object_detection.protos.optimizer_pb2'
  # @@protoc_insertion_point(class_scope:object_detection.protos.Optimizer)
  })
_sym_db.RegisterMessage(Optimizer)

RMSPropOptimizer = _reflection.GeneratedProtocolMessageType('RMSPropOptimizer', (_message.Message,), {
  'DESCRIPTOR' : _RMSPROPOPTIMIZER,
  '__module__' : 'object_detection.protos.optimizer_pb2'
  # @@protoc_insertion_point(class_scope:object_detection.protos.RMSPropOptimizer)
  })
_sym_db.RegisterMessage(RMSPropOptimizer)

MomentumOptimizer = _reflection.GeneratedProtocolMessageType('MomentumOptimizer', (_message.Message,), {
  'DESCRIPTOR' : _MOMENTUMOPTIMIZER,
  '__module__' : 'object_detection.protos.optimizer_pb2'
  # @@protoc_insertion_point(class_scope:object_detection.protos.MomentumOptimizer)
  })
_sym_db.RegisterMessage(MomentumOptimizer)

AdamOptimizer = _reflection.GeneratedProtocolMessageType('AdamOptimizer', (_message.Message,), {
  'DESCRIPTOR' : _ADAMOPTIMIZER,
  '__module__' : 'object_detection.protos.optimizer_pb2'
  # @@protoc_insertion_point(class_scope:object_detection.protos.AdamOptimizer)
  })
_sym_db.RegisterMessage(AdamOptimizer)

LearningRate = _reflection.GeneratedProtocolMessageType('LearningRate', (_message.Message,), {
  'DESCRIPTOR' : _LEARNINGRATE,
  '__module__' : 'object_detection.protos.optimizer_pb2'
  # @@protoc_insertion_point(class_scope:object_detection.protos.LearningRate)
  })
_sym_db.RegisterMessage(LearningRate)

ConstantLearningRate = _reflection.GeneratedProtocolMessageType('ConstantLearningRate', (_message.Message,), {
  'DESCRIPTOR' : _CONSTANTLEARNINGRATE,
  '__module__' : 'object_detection.protos.optimizer_pb2'
  # @@protoc_insertion_point(class_scope:object_detection.protos.ConstantLearningRate)
  })
_sym_db.RegisterMessage(ConstantLearningRate)

ExponentialDecayLearningRate = _reflection.GeneratedProtocolMessageType('ExponentialDecayLearningRate', (_message.Message,), {
  'DESCRIPTOR' : _EXPONENTIALDECAYLEARNINGRATE,
  '__module__' : 'object_detection.protos.optimizer_pb2'
  # @@protoc_insertion_point(class_scope:object_detection.protos.ExponentialDecayLearningRate)
  })
_sym_db.RegisterMessage(ExponentialDecayLearningRate)

ManualStepLearningRate = _reflection.GeneratedProtocolMessageType('ManualStepLearningRate', (_message.Message,), {

  'LearningRateSchedule' : _reflection.GeneratedProtocolMessageType('LearningRateSchedule', (_message.Message,), {
    'DESCRIPTOR' : _MANUALSTEPLEARNINGRATE_LEARNINGRATESCHEDULE,
    '__module__' : 'object_detection.protos.optimizer_pb2'
    # @@protoc_insertion_point(class_scope:object_detection.protos.ManualStepLearningRate.LearningRateSchedule)
    })
  ,
  'DESCRIPTOR' : _MANUALSTEPLEARNINGRATE,
  '__module__' : 'object_detection.protos.optimizer_pb2'
  # @@protoc_insertion_point(class_scope:object_detection.protos.ManualStepLearningRate)
  })
_sym_db.RegisterMessage(ManualStepLearningRate)
_sym_db.RegisterMessage(ManualStepLearningRate.LearningRateSchedule)

CosineDecayLearningRate = _reflection.GeneratedProtocolMessageType('CosineDecayLearningRate', (_message.Message,), {
  'DESCRIPTOR' : _COSINEDECAYLEARNINGRATE,
  '__module__' : 'object_detection.protos.optimizer_pb2'
  # @@protoc_insertion_point(class_scope:object_detection.protos.CosineDecayLearningRate)
  })
_sym_db.RegisterMessage(CosineDecayLearningRate)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _OPTIMIZER._serialized_start=69
  _OPTIMIZER._serialized_end=378
  _RMSPROPOPTIMIZER._serialized_start=381
  _RMSPROPOPTIMIZER._serialized_end=540
  _MOMENTUMOPTIMIZER._serialized_start=542
  _MOMENTUMOPTIMIZER._serialized_end=662
  _ADAMOPTIMIZER._serialized_start=664
  _ADAMOPTIMIZER._serialized_end=741
  _LEARNINGRATE._serialized_start=744
  _LEARNINGRATE._serialized_end=1128
  _CONSTANTLEARNINGRATE._serialized_start=1130
  _CONSTANTLEARNINGRATE._serialized_end=1182
  _EXPONENTIALDECAYLEARNINGRATE._serialized_start=1185
  _EXPONENTIALDECAYLEARNINGRATE._serialized_end=1336
  _MANUALSTEPLEARNINGRATE._serialized_start=1339
  _MANUALSTEPLEARNINGRATE._serialized_end=1580
  _MANUALSTEPLEARNINGRATE_LEARNINGRATESCHEDULE._serialized_start=1514
  _MANUALSTEPLEARNINGRATE_LEARNINGRATESCHEDULE._serialized_end=1580
  _COSINEDECAYLEARNINGRATE._serialized_start=1583
  _COSINEDECAYLEARNINGRATE._serialized_end=1773
# @@protoc_insertion_point(module_scope)
