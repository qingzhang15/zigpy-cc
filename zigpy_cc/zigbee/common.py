import enum

from zigpy_cc.types import uint8_t


class NvItemsIds(uint8_t, enum.Enum):
    EXTADDR = 1
    BOOTCOUNTER = 2
    STARTUP_OPTION = 3
    START_DELAY = 4
    NIB = 33
    DEVICE_LIST = 34
    ADDRMGR = 35
    POLL_RATE = 36
    QUEUED_POLL_RATE = 37
    RESPONSE_POLL_RATE = 38
    REJOIN_POLL_RATE = 39
    DATA_RETRIES = 40
    POLL_FAILURE_RETRIES = 41
    STACK_PROFILE = 42
    INDIRECT_MSG_TIMEOUT = 43
    ROUTE_EXPIRY_TIME = 44
    EXTENDED_PAN_ID = 45
    BCAST_RETRIES = 46
    PASSIVE_ACK_TIMEOUT = 47
    BCAST_DELIVERY_TIME = 48
    NWK_MODE = 49
    CONCENTRATOR_ENABLE = 50
    CONCENTRATOR_DISCOVERY = 51
    CONCENTRATOR_RADIUS = 52
    CONCENTRATOR_RC = 54
    NWK_MGR_MODE = 55
    SRC_RTG_EXPIRY_TIME = 56
    ROUTE_DISCOVERY_TIME = 57
    NWK_ACTIVE_KEY_INFO = 58
    NWK_ALTERN_KEY_INFO = 59
    ROUTER_OFF_ASSOC_CLEANUP = 60
    NWK_LEAVE_REQ_ALLOWED = 61
    NWK_CHILD_AGE_ENABLE = 62
    DEVICE_LIST_KA_TIMEOUT = 63
    BINDING_TABLE = 65
    GROUP_TABLE = 66
    APS_FRAME_RETRIES = 67
    APS_ACK_WAIT_DURATION = 68
    APS_ACK_WAIT_MULTIPLIER = 69
    BINDING_TIME = 70
    APS_USE_EXT_PANID = 71
    APS_USE_INSECURE_JOIN = 72
    COMMISSIONED_NWK_ADDR = 73
    APS_NONMEMBER_RADIUS = 75
    APS_LINK_KEY_TABLE = 76
    APS_DUPREJ_TIMEOUT_INC = 77
    APS_DUPREJ_TIMEOUT_COUNT = 78
    APS_DUPREJ_TABLE_SIZE = 79
    DIAGNOSTIC_STATS = 80
    BDBNODEISONANETWORK = 85
    SECURITY_LEVEL = 97
    PRECFGKEY = 98
    PRECFGKEYS_ENABLE = 99
    SECURITY_MODE = 100
    SECURE_PERMIT_JOIN = 101
    APS_LINK_KEY_TYPE = 102
    APS_ALLOW_R19_SECURITY = 103
    IMPLICIT_CERTIFICATE = 105
    DEVICE_PRIVATE_KEY = 106
    CA_PUBLIC_KEY = 107
    KE_MAX_DEVICES = 108
    USE_DEFAULT_TCLK = 109
    RNG_COUNTER = 111
    RANDOM_SEED = 112
    TRUSTCENTER_ADDR = 113
    LEGACY_NWK_SEC_MATERIAL_TABLE_START = 117  # Valid for <= Z-Stack 3.0.x
    EX_NWK_SEC_MATERIAL_TABLE = 7  # Valid for >= Z-Stack 3.x.0
    USERDESC = 129
    NWKKEY = 130
    PANID = 131
    CHANLIST = 132
    LEAVE_CTRL = 133
    SCAN_DURATION = 134
    LOGICAL_TYPE = 135
    NWKMGR_MIN_TX = 136
    NWKMGR_ADDR = 137
    ZDO_DIRECT_CB = 143
    SCENE_TABLE = 145
    MIN_FREE_NWK_ADDR = 146
    MAX_FREE_NWK_ADDR = 147
    MIN_FREE_GRP_ID = 148
    MAX_FREE_GRP_ID = 149
    MIN_GRP_IDS = 150
    MAX_GRP_IDS = 151
    OTA_BLOCK_REQ_DELAY = 152
    SAPI_ENDPOINT = 161
    SAS_SHORT_ADDR = 177
    SAS_EXT_PANID = 178
    SAS_PANID = 179
    SAS_CHANNEL_MASK = 180
    SAS_PROTOCOL_VER = 181
    SAS_STACK_PROFILE = 182
    SAS_STARTUP_CTRL = 183
    SAS_TC_ADDR = 193
    SAS_TC_MASTER_KEY = 194
    SAS_NWK_KEY = 195
    SAS_USE_INSEC_JOIN = 196
    SAS_PRECFG_LINK_KEY = 197
    SAS_NWK_KEY_SEQ_NUM = 198
    SAS_NWK_KEY_TYPE = 199
    SAS_NWK_MGR_ADDR = 200
    SAS_CURR_TC_MASTER_KEY = 209
    SAS_CURR_NWK_KEY = 210
    SAS_CURR_PRECFG_LINK_KEY = 211
    LEGACY_TCLK_TABLE_START = 257  # Valid for <= Z-Stack 3.0.x
    LEGACY_TCLK_TABLE_END = 511  # Valid for <= Z-Stack 3.0.x
    EX_TCLK_TABLE = 4  # Valid for >= Z-Stack 3.0.x
    APS_LINK_KEY_DATA_START = 513
    APS_LINK_KEY_DATA_END = 767
    DUPLICATE_BINDING_TABLE = 768
    DUPLICATE_DEVICE_LIST = 769
    DUPLICATE_DEVICE_LIST_KA_TIMEOUT = 770
    ZNP_HAS_CONFIGURED_ZSTACK1 = 3840
    ZNP_HAS_CONFIGURED_ZSTACK3 = 96


class Common:
    devStates = {
        "HOLD": 0,
        "INIT": 1,
        "NWK_DISC": 2,
        "NWK_JOINING": 3,
        "NWK_REJOIN": 4,
        "END_DEVICE_UNAUTH": 5,
        "END_DEVICE": 6,
        "ROUTER": 7,
        "COORD_STARTING": 8,
        "ZB_COORD": 9,
        "NWK_ORPHAN": 10,
        "INVALID_REQTYPE": 128,
        "DEVICE_NOT_FOUND": 129,
        "INVALID_EP": 130,
        "NOT_ACTIVE": 131,
        "NOT_SUPPORTED": 132,
        "TIMEOUT": 133,
        "NO_MATCH": 134,
        "NO_ENTRY": 136,
        "NO_DESCRIPTOR": 137,
        "INSUFFICIENT_SPACE": 138,
        "NOT_PERMITTED": 139,
        "TABLE_FULL": 140,
        "NOT_AUTHORIZED": 141,
        "BINDING_TABLE_FULL": 142
    }
    logicalChannels = {
        "NONE": 0,
        "CH11": 11,
        "CH12": 12,
        "CH13": 13,
        "CH14": 14,
        "CH15": 15,
        "CH16": 16,
        "CH17": 17,
        "CH18": 18,
        "CH19": 19,
        "CH20": 20,
        "CH21": 21,
        "CH22": 22,
        "CH23": 23,
        "CH24": 24,
        "CH25": 25,
        "CH26": 26
    }
    channelMask = {
        "CH11": 2048,
        "CH12": 4096,
        "CH13": 8192,
        "CH14": 16384,
        "CH15": 32768,
        "CH16": 65536,
        "CH17": 131072,
        "CH18": 262144,
        "CH19": 524288,
        "CH20": 1048576,
        "CH21": 2097152,
        "CH22": 4194304,
        "CH23": 8388608,
        "CH24": 16777216,
        "CH25": 33554432,
        "CH26": 67108864,
        "CH_ALL": 134215680
    }
