# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: grpc_comm_manager.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='grpc_comm_manager.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x17grpc_comm_manager.proto\"1\n\x0b\x43ommRequest\x12\x11\n\tclient_id\x18\x01 \x01(\x05\x12\x0f\n\x07message\x18\x02 \x01(\x0c\"2\n\x0c\x43ommResponse\x12\x11\n\tclient_id\x18\x01 \x01(\x05\x12\x0f\n\x07message\x18\x02 \x01(\x0c\x32r\n\x0fgRPCCommManager\x12*\n\x0bsendMessage\x12\x0c.CommRequest\x1a\r.CommResponse\x12\x33\n\x14handleReceiveMessage\x12\x0c.CommRequest\x1a\r.CommResponseb\x06proto3'
)




_COMMREQUEST = _descriptor.Descriptor(
  name='CommRequest',
  full_name='CommRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='client_id', full_name='CommRequest.client_id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='message', full_name='CommRequest.message', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=27,
  serialized_end=76,
)


_COMMRESPONSE = _descriptor.Descriptor(
  name='CommResponse',
  full_name='CommResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='client_id', full_name='CommResponse.client_id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='message', full_name='CommResponse.message', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=78,
  serialized_end=128,
)

DESCRIPTOR.message_types_by_name['CommRequest'] = _COMMREQUEST
DESCRIPTOR.message_types_by_name['CommResponse'] = _COMMRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

CommRequest = _reflection.GeneratedProtocolMessageType('CommRequest', (_message.Message,), {
  'DESCRIPTOR' : _COMMREQUEST,
  '__module__' : 'grpc_comm_manager_pb2'
  # @@protoc_insertion_point(class_scope:CommRequest)
  })
_sym_db.RegisterMessage(CommRequest)

CommResponse = _reflection.GeneratedProtocolMessageType('CommResponse', (_message.Message,), {
  'DESCRIPTOR' : _COMMRESPONSE,
  '__module__' : 'grpc_comm_manager_pb2'
  # @@protoc_insertion_point(class_scope:CommResponse)
  })
_sym_db.RegisterMessage(CommResponse)



_GRPCCOMMMANAGER = _descriptor.ServiceDescriptor(
  name='gRPCCommManager',
  full_name='gRPCCommManager',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=130,
  serialized_end=244,
  methods=[
  _descriptor.MethodDescriptor(
    name='sendMessage',
    full_name='gRPCCommManager.sendMessage',
    index=0,
    containing_service=None,
    input_type=_COMMREQUEST,
    output_type=_COMMRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='handleReceiveMessage',
    full_name='gRPCCommManager.handleReceiveMessage',
    index=1,
    containing_service=None,
    input_type=_COMMREQUEST,
    output_type=_COMMRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_GRPCCOMMMANAGER)

DESCRIPTOR.services_by_name['gRPCCommManager'] = _GRPCCOMMMANAGER

# @@protoc_insertion_point(module_scope)