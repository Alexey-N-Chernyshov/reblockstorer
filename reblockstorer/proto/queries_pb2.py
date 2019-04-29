# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: queries.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from . import primitive_pb2 as primitive__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='queries.proto',
  package='iroha.protocol',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\rqueries.proto\x12\x0eiroha.protocol\x1a\x0fprimitive.proto\"S\n\x10TxPaginationMeta\x12\x11\n\tpage_size\x18\x01 \x01(\r\x12\x17\n\rfirst_tx_hash\x18\x02 \x01(\tH\x00\x42\x13\n\x11opt_first_tx_hash\" \n\nGetAccount\x12\x12\n\naccount_id\x18\x01 \x01(\t\"\x1a\n\x08GetBlock\x12\x0e\n\x06height\x18\x01 \x01(\x04\"$\n\x0eGetSignatories\x12\x12\n\naccount_id\x18\x01 \x01(\t\"g\n\x16GetAccountTransactions\x12\x12\n\naccount_id\x18\x01 \x01(\t\x12\x39\n\x0fpagination_meta\x18\x02 \x01(\x0b\x32 .iroha.protocol.TxPaginationMeta\"~\n\x1bGetAccountAssetTransactions\x12\x12\n\naccount_id\x18\x01 \x01(\t\x12\x10\n\x08\x61sset_id\x18\x02 \x01(\t\x12\x39\n\x0fpagination_meta\x18\x03 \x01(\x0b\x32 .iroha.protocol.TxPaginationMeta\"$\n\x0fGetTransactions\x12\x11\n\ttx_hashes\x18\x01 \x03(\t\"&\n\x10GetAccountAssets\x12\x12\n\naccount_id\x18\x01 \x01(\t\"t\n\x10GetAccountDetail\x12\x14\n\naccount_id\x18\x01 \x01(\tH\x00\x12\r\n\x03key\x18\x02 \x01(\tH\x01\x12\x10\n\x06writer\x18\x03 \x01(\tH\x02\x42\x10\n\x0eopt_account_idB\t\n\x07opt_keyB\x0c\n\nopt_writer\" \n\x0cGetAssetInfo\x12\x10\n\x08\x61sset_id\x18\x01 \x01(\t\"\n\n\x08GetRoles\"%\n\x12GetRolePermissions\x12\x0f\n\x07role_id\x18\x01 \x01(\t\"\x18\n\x16GetPendingTransactions\"[\n\x10QueryPayloadMeta\x12\x14\n\x0c\x63reated_time\x18\x01 \x01(\x04\x12\x1a\n\x12\x63reator_account_id\x18\x02 \x01(\t\x12\x15\n\rquery_counter\x18\x03 \x01(\x04\"\x9e\x07\n\x05Query\x12.\n\x07payload\x18\x01 \x01(\x0b\x32\x1d.iroha.protocol.Query.Payload\x12,\n\tsignature\x18\x02 \x01(\x0b\x32\x19.iroha.protocol.Signature\x1a\xb6\x06\n\x07Payload\x12.\n\x04meta\x18\x01 \x01(\x0b\x32 .iroha.protocol.QueryPayloadMeta\x12\x31\n\x0bget_account\x18\x03 \x01(\x0b\x32\x1a.iroha.protocol.GetAccountH\x00\x12\x39\n\x0fget_signatories\x18\x04 \x01(\x0b\x32\x1e.iroha.protocol.GetSignatoriesH\x00\x12J\n\x18get_account_transactions\x18\x05 \x01(\x0b\x32&.iroha.protocol.GetAccountTransactionsH\x00\x12U\n\x1eget_account_asset_transactions\x18\x06 \x01(\x0b\x32+.iroha.protocol.GetAccountAssetTransactionsH\x00\x12;\n\x10get_transactions\x18\x07 \x01(\x0b\x32\x1f.iroha.protocol.GetTransactionsH\x00\x12>\n\x12get_account_assets\x18\x08 \x01(\x0b\x32 .iroha.protocol.GetAccountAssetsH\x00\x12>\n\x12get_account_detail\x18\t \x01(\x0b\x32 .iroha.protocol.GetAccountDetailH\x00\x12-\n\tget_roles\x18\n \x01(\x0b\x32\x18.iroha.protocol.GetRolesH\x00\x12\x42\n\x14get_role_permissions\x18\x0b \x01(\x0b\x32\".iroha.protocol.GetRolePermissionsH\x00\x12\x36\n\x0eget_asset_info\x18\x0c \x01(\x0b\x32\x1c.iroha.protocol.GetAssetInfoH\x00\x12J\n\x18get_pending_transactions\x18\r \x01(\x0b\x32&.iroha.protocol.GetPendingTransactionsH\x00\x12-\n\tget_block\x18\x0e \x01(\x0b\x32\x18.iroha.protocol.GetBlockH\x00\x42\x07\n\x05query\"k\n\x0b\x42locksQuery\x12.\n\x04meta\x18\x01 \x01(\x0b\x32 .iroha.protocol.QueryPayloadMeta\x12,\n\tsignature\x18\x02 \x01(\x0b\x32\x19.iroha.protocol.Signatureb\x06proto3')
  ,
  dependencies=[primitive__pb2.DESCRIPTOR,])




_TXPAGINATIONMETA = _descriptor.Descriptor(
  name='TxPaginationMeta',
  full_name='iroha.protocol.TxPaginationMeta',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='page_size', full_name='iroha.protocol.TxPaginationMeta.page_size', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='first_tx_hash', full_name='iroha.protocol.TxPaginationMeta.first_tx_hash', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
    _descriptor.OneofDescriptor(
      name='opt_first_tx_hash', full_name='iroha.protocol.TxPaginationMeta.opt_first_tx_hash',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=50,
  serialized_end=133,
)


_GETACCOUNT = _descriptor.Descriptor(
  name='GetAccount',
  full_name='iroha.protocol.GetAccount',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='account_id', full_name='iroha.protocol.GetAccount.account_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=135,
  serialized_end=167,
)


_GETBLOCK = _descriptor.Descriptor(
  name='GetBlock',
  full_name='iroha.protocol.GetBlock',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='height', full_name='iroha.protocol.GetBlock.height', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=169,
  serialized_end=195,
)


_GETSIGNATORIES = _descriptor.Descriptor(
  name='GetSignatories',
  full_name='iroha.protocol.GetSignatories',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='account_id', full_name='iroha.protocol.GetSignatories.account_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=197,
  serialized_end=233,
)


_GETACCOUNTTRANSACTIONS = _descriptor.Descriptor(
  name='GetAccountTransactions',
  full_name='iroha.protocol.GetAccountTransactions',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='account_id', full_name='iroha.protocol.GetAccountTransactions.account_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='pagination_meta', full_name='iroha.protocol.GetAccountTransactions.pagination_meta', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=235,
  serialized_end=338,
)


_GETACCOUNTASSETTRANSACTIONS = _descriptor.Descriptor(
  name='GetAccountAssetTransactions',
  full_name='iroha.protocol.GetAccountAssetTransactions',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='account_id', full_name='iroha.protocol.GetAccountAssetTransactions.account_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='asset_id', full_name='iroha.protocol.GetAccountAssetTransactions.asset_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='pagination_meta', full_name='iroha.protocol.GetAccountAssetTransactions.pagination_meta', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=340,
  serialized_end=466,
)


_GETTRANSACTIONS = _descriptor.Descriptor(
  name='GetTransactions',
  full_name='iroha.protocol.GetTransactions',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='tx_hashes', full_name='iroha.protocol.GetTransactions.tx_hashes', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=468,
  serialized_end=504,
)


_GETACCOUNTASSETS = _descriptor.Descriptor(
  name='GetAccountAssets',
  full_name='iroha.protocol.GetAccountAssets',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='account_id', full_name='iroha.protocol.GetAccountAssets.account_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=506,
  serialized_end=544,
)


_GETACCOUNTDETAIL = _descriptor.Descriptor(
  name='GetAccountDetail',
  full_name='iroha.protocol.GetAccountDetail',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='account_id', full_name='iroha.protocol.GetAccountDetail.account_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='key', full_name='iroha.protocol.GetAccountDetail.key', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='writer', full_name='iroha.protocol.GetAccountDetail.writer', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
    _descriptor.OneofDescriptor(
      name='opt_account_id', full_name='iroha.protocol.GetAccountDetail.opt_account_id',
      index=0, containing_type=None, fields=[]),
    _descriptor.OneofDescriptor(
      name='opt_key', full_name='iroha.protocol.GetAccountDetail.opt_key',
      index=1, containing_type=None, fields=[]),
    _descriptor.OneofDescriptor(
      name='opt_writer', full_name='iroha.protocol.GetAccountDetail.opt_writer',
      index=2, containing_type=None, fields=[]),
  ],
  serialized_start=546,
  serialized_end=662,
)


_GETASSETINFO = _descriptor.Descriptor(
  name='GetAssetInfo',
  full_name='iroha.protocol.GetAssetInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='asset_id', full_name='iroha.protocol.GetAssetInfo.asset_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=664,
  serialized_end=696,
)


_GETROLES = _descriptor.Descriptor(
  name='GetRoles',
  full_name='iroha.protocol.GetRoles',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
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
  serialized_start=698,
  serialized_end=708,
)


_GETROLEPERMISSIONS = _descriptor.Descriptor(
  name='GetRolePermissions',
  full_name='iroha.protocol.GetRolePermissions',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='role_id', full_name='iroha.protocol.GetRolePermissions.role_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=710,
  serialized_end=747,
)


_GETPENDINGTRANSACTIONS = _descriptor.Descriptor(
  name='GetPendingTransactions',
  full_name='iroha.protocol.GetPendingTransactions',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
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
  serialized_start=749,
  serialized_end=773,
)


_QUERYPAYLOADMETA = _descriptor.Descriptor(
  name='QueryPayloadMeta',
  full_name='iroha.protocol.QueryPayloadMeta',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='created_time', full_name='iroha.protocol.QueryPayloadMeta.created_time', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='creator_account_id', full_name='iroha.protocol.QueryPayloadMeta.creator_account_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='query_counter', full_name='iroha.protocol.QueryPayloadMeta.query_counter', index=2,
      number=3, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=775,
  serialized_end=866,
)


_QUERY_PAYLOAD = _descriptor.Descriptor(
  name='Payload',
  full_name='iroha.protocol.Query.Payload',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='meta', full_name='iroha.protocol.Query.Payload.meta', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='get_account', full_name='iroha.protocol.Query.Payload.get_account', index=1,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='get_signatories', full_name='iroha.protocol.Query.Payload.get_signatories', index=2,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='get_account_transactions', full_name='iroha.protocol.Query.Payload.get_account_transactions', index=3,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='get_account_asset_transactions', full_name='iroha.protocol.Query.Payload.get_account_asset_transactions', index=4,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='get_transactions', full_name='iroha.protocol.Query.Payload.get_transactions', index=5,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='get_account_assets', full_name='iroha.protocol.Query.Payload.get_account_assets', index=6,
      number=8, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='get_account_detail', full_name='iroha.protocol.Query.Payload.get_account_detail', index=7,
      number=9, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='get_roles', full_name='iroha.protocol.Query.Payload.get_roles', index=8,
      number=10, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='get_role_permissions', full_name='iroha.protocol.Query.Payload.get_role_permissions', index=9,
      number=11, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='get_asset_info', full_name='iroha.protocol.Query.Payload.get_asset_info', index=10,
      number=12, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='get_pending_transactions', full_name='iroha.protocol.Query.Payload.get_pending_transactions', index=11,
      number=13, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='get_block', full_name='iroha.protocol.Query.Payload.get_block', index=12,
      number=14, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
    _descriptor.OneofDescriptor(
      name='query', full_name='iroha.protocol.Query.Payload.query',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=973,
  serialized_end=1795,
)

_QUERY = _descriptor.Descriptor(
  name='Query',
  full_name='iroha.protocol.Query',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='payload', full_name='iroha.protocol.Query.payload', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='signature', full_name='iroha.protocol.Query.signature', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_QUERY_PAYLOAD, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=869,
  serialized_end=1795,
)


_BLOCKSQUERY = _descriptor.Descriptor(
  name='BlocksQuery',
  full_name='iroha.protocol.BlocksQuery',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='meta', full_name='iroha.protocol.BlocksQuery.meta', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='signature', full_name='iroha.protocol.BlocksQuery.signature', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=1797,
  serialized_end=1904,
)

_TXPAGINATIONMETA.oneofs_by_name['opt_first_tx_hash'].fields.append(
  _TXPAGINATIONMETA.fields_by_name['first_tx_hash'])
_TXPAGINATIONMETA.fields_by_name['first_tx_hash'].containing_oneof = _TXPAGINATIONMETA.oneofs_by_name['opt_first_tx_hash']
_GETACCOUNTTRANSACTIONS.fields_by_name['pagination_meta'].message_type = _TXPAGINATIONMETA
_GETACCOUNTASSETTRANSACTIONS.fields_by_name['pagination_meta'].message_type = _TXPAGINATIONMETA
_GETACCOUNTDETAIL.oneofs_by_name['opt_account_id'].fields.append(
  _GETACCOUNTDETAIL.fields_by_name['account_id'])
_GETACCOUNTDETAIL.fields_by_name['account_id'].containing_oneof = _GETACCOUNTDETAIL.oneofs_by_name['opt_account_id']
_GETACCOUNTDETAIL.oneofs_by_name['opt_key'].fields.append(
  _GETACCOUNTDETAIL.fields_by_name['key'])
_GETACCOUNTDETAIL.fields_by_name['key'].containing_oneof = _GETACCOUNTDETAIL.oneofs_by_name['opt_key']
_GETACCOUNTDETAIL.oneofs_by_name['opt_writer'].fields.append(
  _GETACCOUNTDETAIL.fields_by_name['writer'])
_GETACCOUNTDETAIL.fields_by_name['writer'].containing_oneof = _GETACCOUNTDETAIL.oneofs_by_name['opt_writer']
_QUERY_PAYLOAD.fields_by_name['meta'].message_type = _QUERYPAYLOADMETA
_QUERY_PAYLOAD.fields_by_name['get_account'].message_type = _GETACCOUNT
_QUERY_PAYLOAD.fields_by_name['get_signatories'].message_type = _GETSIGNATORIES
_QUERY_PAYLOAD.fields_by_name['get_account_transactions'].message_type = _GETACCOUNTTRANSACTIONS
_QUERY_PAYLOAD.fields_by_name['get_account_asset_transactions'].message_type = _GETACCOUNTASSETTRANSACTIONS
_QUERY_PAYLOAD.fields_by_name['get_transactions'].message_type = _GETTRANSACTIONS
_QUERY_PAYLOAD.fields_by_name['get_account_assets'].message_type = _GETACCOUNTASSETS
_QUERY_PAYLOAD.fields_by_name['get_account_detail'].message_type = _GETACCOUNTDETAIL
_QUERY_PAYLOAD.fields_by_name['get_roles'].message_type = _GETROLES
_QUERY_PAYLOAD.fields_by_name['get_role_permissions'].message_type = _GETROLEPERMISSIONS
_QUERY_PAYLOAD.fields_by_name['get_asset_info'].message_type = _GETASSETINFO
_QUERY_PAYLOAD.fields_by_name['get_pending_transactions'].message_type = _GETPENDINGTRANSACTIONS
_QUERY_PAYLOAD.fields_by_name['get_block'].message_type = _GETBLOCK
_QUERY_PAYLOAD.containing_type = _QUERY
_QUERY_PAYLOAD.oneofs_by_name['query'].fields.append(
  _QUERY_PAYLOAD.fields_by_name['get_account'])
_QUERY_PAYLOAD.fields_by_name['get_account'].containing_oneof = _QUERY_PAYLOAD.oneofs_by_name['query']
_QUERY_PAYLOAD.oneofs_by_name['query'].fields.append(
  _QUERY_PAYLOAD.fields_by_name['get_signatories'])
_QUERY_PAYLOAD.fields_by_name['get_signatories'].containing_oneof = _QUERY_PAYLOAD.oneofs_by_name['query']
_QUERY_PAYLOAD.oneofs_by_name['query'].fields.append(
  _QUERY_PAYLOAD.fields_by_name['get_account_transactions'])
_QUERY_PAYLOAD.fields_by_name['get_account_transactions'].containing_oneof = _QUERY_PAYLOAD.oneofs_by_name['query']
_QUERY_PAYLOAD.oneofs_by_name['query'].fields.append(
  _QUERY_PAYLOAD.fields_by_name['get_account_asset_transactions'])
_QUERY_PAYLOAD.fields_by_name['get_account_asset_transactions'].containing_oneof = _QUERY_PAYLOAD.oneofs_by_name['query']
_QUERY_PAYLOAD.oneofs_by_name['query'].fields.append(
  _QUERY_PAYLOAD.fields_by_name['get_transactions'])
_QUERY_PAYLOAD.fields_by_name['get_transactions'].containing_oneof = _QUERY_PAYLOAD.oneofs_by_name['query']
_QUERY_PAYLOAD.oneofs_by_name['query'].fields.append(
  _QUERY_PAYLOAD.fields_by_name['get_account_assets'])
_QUERY_PAYLOAD.fields_by_name['get_account_assets'].containing_oneof = _QUERY_PAYLOAD.oneofs_by_name['query']
_QUERY_PAYLOAD.oneofs_by_name['query'].fields.append(
  _QUERY_PAYLOAD.fields_by_name['get_account_detail'])
_QUERY_PAYLOAD.fields_by_name['get_account_detail'].containing_oneof = _QUERY_PAYLOAD.oneofs_by_name['query']
_QUERY_PAYLOAD.oneofs_by_name['query'].fields.append(
  _QUERY_PAYLOAD.fields_by_name['get_roles'])
_QUERY_PAYLOAD.fields_by_name['get_roles'].containing_oneof = _QUERY_PAYLOAD.oneofs_by_name['query']
_QUERY_PAYLOAD.oneofs_by_name['query'].fields.append(
  _QUERY_PAYLOAD.fields_by_name['get_role_permissions'])
_QUERY_PAYLOAD.fields_by_name['get_role_permissions'].containing_oneof = _QUERY_PAYLOAD.oneofs_by_name['query']
_QUERY_PAYLOAD.oneofs_by_name['query'].fields.append(
  _QUERY_PAYLOAD.fields_by_name['get_asset_info'])
_QUERY_PAYLOAD.fields_by_name['get_asset_info'].containing_oneof = _QUERY_PAYLOAD.oneofs_by_name['query']
_QUERY_PAYLOAD.oneofs_by_name['query'].fields.append(
  _QUERY_PAYLOAD.fields_by_name['get_pending_transactions'])
_QUERY_PAYLOAD.fields_by_name['get_pending_transactions'].containing_oneof = _QUERY_PAYLOAD.oneofs_by_name['query']
_QUERY_PAYLOAD.oneofs_by_name['query'].fields.append(
  _QUERY_PAYLOAD.fields_by_name['get_block'])
_QUERY_PAYLOAD.fields_by_name['get_block'].containing_oneof = _QUERY_PAYLOAD.oneofs_by_name['query']
_QUERY.fields_by_name['payload'].message_type = _QUERY_PAYLOAD
_QUERY.fields_by_name['signature'].message_type = primitive__pb2._SIGNATURE
_BLOCKSQUERY.fields_by_name['meta'].message_type = _QUERYPAYLOADMETA
_BLOCKSQUERY.fields_by_name['signature'].message_type = primitive__pb2._SIGNATURE
DESCRIPTOR.message_types_by_name['TxPaginationMeta'] = _TXPAGINATIONMETA
DESCRIPTOR.message_types_by_name['GetAccount'] = _GETACCOUNT
DESCRIPTOR.message_types_by_name['GetBlock'] = _GETBLOCK
DESCRIPTOR.message_types_by_name['GetSignatories'] = _GETSIGNATORIES
DESCRIPTOR.message_types_by_name['GetAccountTransactions'] = _GETACCOUNTTRANSACTIONS
DESCRIPTOR.message_types_by_name['GetAccountAssetTransactions'] = _GETACCOUNTASSETTRANSACTIONS
DESCRIPTOR.message_types_by_name['GetTransactions'] = _GETTRANSACTIONS
DESCRIPTOR.message_types_by_name['GetAccountAssets'] = _GETACCOUNTASSETS
DESCRIPTOR.message_types_by_name['GetAccountDetail'] = _GETACCOUNTDETAIL
DESCRIPTOR.message_types_by_name['GetAssetInfo'] = _GETASSETINFO
DESCRIPTOR.message_types_by_name['GetRoles'] = _GETROLES
DESCRIPTOR.message_types_by_name['GetRolePermissions'] = _GETROLEPERMISSIONS
DESCRIPTOR.message_types_by_name['GetPendingTransactions'] = _GETPENDINGTRANSACTIONS
DESCRIPTOR.message_types_by_name['QueryPayloadMeta'] = _QUERYPAYLOADMETA
DESCRIPTOR.message_types_by_name['Query'] = _QUERY
DESCRIPTOR.message_types_by_name['BlocksQuery'] = _BLOCKSQUERY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

TxPaginationMeta = _reflection.GeneratedProtocolMessageType('TxPaginationMeta', (_message.Message,), dict(
  DESCRIPTOR = _TXPAGINATIONMETA,
  __module__ = 'queries_pb2'
  # @@protoc_insertion_point(class_scope:iroha.protocol.TxPaginationMeta)
  ))
_sym_db.RegisterMessage(TxPaginationMeta)

GetAccount = _reflection.GeneratedProtocolMessageType('GetAccount', (_message.Message,), dict(
  DESCRIPTOR = _GETACCOUNT,
  __module__ = 'queries_pb2'
  # @@protoc_insertion_point(class_scope:iroha.protocol.GetAccount)
  ))
_sym_db.RegisterMessage(GetAccount)

GetBlock = _reflection.GeneratedProtocolMessageType('GetBlock', (_message.Message,), dict(
  DESCRIPTOR = _GETBLOCK,
  __module__ = 'queries_pb2'
  # @@protoc_insertion_point(class_scope:iroha.protocol.GetBlock)
  ))
_sym_db.RegisterMessage(GetBlock)

GetSignatories = _reflection.GeneratedProtocolMessageType('GetSignatories', (_message.Message,), dict(
  DESCRIPTOR = _GETSIGNATORIES,
  __module__ = 'queries_pb2'
  # @@protoc_insertion_point(class_scope:iroha.protocol.GetSignatories)
  ))
_sym_db.RegisterMessage(GetSignatories)

GetAccountTransactions = _reflection.GeneratedProtocolMessageType('GetAccountTransactions', (_message.Message,), dict(
  DESCRIPTOR = _GETACCOUNTTRANSACTIONS,
  __module__ = 'queries_pb2'
  # @@protoc_insertion_point(class_scope:iroha.protocol.GetAccountTransactions)
  ))
_sym_db.RegisterMessage(GetAccountTransactions)

GetAccountAssetTransactions = _reflection.GeneratedProtocolMessageType('GetAccountAssetTransactions', (_message.Message,), dict(
  DESCRIPTOR = _GETACCOUNTASSETTRANSACTIONS,
  __module__ = 'queries_pb2'
  # @@protoc_insertion_point(class_scope:iroha.protocol.GetAccountAssetTransactions)
  ))
_sym_db.RegisterMessage(GetAccountAssetTransactions)

GetTransactions = _reflection.GeneratedProtocolMessageType('GetTransactions', (_message.Message,), dict(
  DESCRIPTOR = _GETTRANSACTIONS,
  __module__ = 'queries_pb2'
  # @@protoc_insertion_point(class_scope:iroha.protocol.GetTransactions)
  ))
_sym_db.RegisterMessage(GetTransactions)

GetAccountAssets = _reflection.GeneratedProtocolMessageType('GetAccountAssets', (_message.Message,), dict(
  DESCRIPTOR = _GETACCOUNTASSETS,
  __module__ = 'queries_pb2'
  # @@protoc_insertion_point(class_scope:iroha.protocol.GetAccountAssets)
  ))
_sym_db.RegisterMessage(GetAccountAssets)

GetAccountDetail = _reflection.GeneratedProtocolMessageType('GetAccountDetail', (_message.Message,), dict(
  DESCRIPTOR = _GETACCOUNTDETAIL,
  __module__ = 'queries_pb2'
  # @@protoc_insertion_point(class_scope:iroha.protocol.GetAccountDetail)
  ))
_sym_db.RegisterMessage(GetAccountDetail)

GetAssetInfo = _reflection.GeneratedProtocolMessageType('GetAssetInfo', (_message.Message,), dict(
  DESCRIPTOR = _GETASSETINFO,
  __module__ = 'queries_pb2'
  # @@protoc_insertion_point(class_scope:iroha.protocol.GetAssetInfo)
  ))
_sym_db.RegisterMessage(GetAssetInfo)

GetRoles = _reflection.GeneratedProtocolMessageType('GetRoles', (_message.Message,), dict(
  DESCRIPTOR = _GETROLES,
  __module__ = 'queries_pb2'
  # @@protoc_insertion_point(class_scope:iroha.protocol.GetRoles)
  ))
_sym_db.RegisterMessage(GetRoles)

GetRolePermissions = _reflection.GeneratedProtocolMessageType('GetRolePermissions', (_message.Message,), dict(
  DESCRIPTOR = _GETROLEPERMISSIONS,
  __module__ = 'queries_pb2'
  # @@protoc_insertion_point(class_scope:iroha.protocol.GetRolePermissions)
  ))
_sym_db.RegisterMessage(GetRolePermissions)

GetPendingTransactions = _reflection.GeneratedProtocolMessageType('GetPendingTransactions', (_message.Message,), dict(
  DESCRIPTOR = _GETPENDINGTRANSACTIONS,
  __module__ = 'queries_pb2'
  # @@protoc_insertion_point(class_scope:iroha.protocol.GetPendingTransactions)
  ))
_sym_db.RegisterMessage(GetPendingTransactions)

QueryPayloadMeta = _reflection.GeneratedProtocolMessageType('QueryPayloadMeta', (_message.Message,), dict(
  DESCRIPTOR = _QUERYPAYLOADMETA,
  __module__ = 'queries_pb2'
  # @@protoc_insertion_point(class_scope:iroha.protocol.QueryPayloadMeta)
  ))
_sym_db.RegisterMessage(QueryPayloadMeta)

Query = _reflection.GeneratedProtocolMessageType('Query', (_message.Message,), dict(

  Payload = _reflection.GeneratedProtocolMessageType('Payload', (_message.Message,), dict(
    DESCRIPTOR = _QUERY_PAYLOAD,
    __module__ = 'queries_pb2'
    # @@protoc_insertion_point(class_scope:iroha.protocol.Query.Payload)
    ))
  ,
  DESCRIPTOR = _QUERY,
  __module__ = 'queries_pb2'
  # @@protoc_insertion_point(class_scope:iroha.protocol.Query)
  ))
_sym_db.RegisterMessage(Query)
_sym_db.RegisterMessage(Query.Payload)

BlocksQuery = _reflection.GeneratedProtocolMessageType('BlocksQuery', (_message.Message,), dict(
  DESCRIPTOR = _BLOCKSQUERY,
  __module__ = 'queries_pb2'
  # @@protoc_insertion_point(class_scope:iroha.protocol.BlocksQuery)
  ))
_sym_db.RegisterMessage(BlocksQuery)


# @@protoc_insertion_point(module_scope)
