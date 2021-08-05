DOMAIN = "solaredge_modbus"
DEFAULT_NAME = "solaredge"
DEFAULT_SCAN_INTERVAL = 30
DEFAULT_PORT = 1502
DEFAULT_READ_METER1 = False
DEFAULT_READ_METER2 = False
DEFAULT_READ_METER3 = False
CONF_SOLAREDGE_HUB = "solaredge_hub"
ATTR_STATUS_DESCRIPTION = "status_description"
ATTR_MANUFACTURER = "Solaredge"
CONF_READ_METER1 = "read_meter_1"
CONF_READ_METER2 = "read_meter_2"
CONF_READ_METER3 = "read_meter_3"

SENSOR_TYPES = {
    "AC_Current": ["AC Current", "accurrent", "A", "mdi:current-ac", DEVICE_CLASS_CURRENT],
    "AC_CurrentA": ["AC Current A", "accurrenta", "A", "mdi:current-ac", DEVICE_CLASS_CURRENT],
    "AC_CurrentB": ["AC Current B", "accurrentb", "A", "mdi:current-ac", DEVICE_CLASS_CURRENT],
    "AC_CurrentC": ["AC Current C", "accurrentc", "A", "mdi:current-ac", DEVICE_CLASS_CURRENT],
    "AC_VoltageAB": ["AC Voltage AB", "acvoltageab", "V", None, DEVICE_CLASS_VOLTAGE],
    "AC_VoltageBC": ["AC Voltage BC", "acvoltagebc", "V", None, DEVICE_CLASS_VOLTAGE],
    "AC_VoltageCA": ["AC Voltage CA", "acvoltageca", "V", None, DEVICE_CLASS_VOLTAGE],
    "AC_VoltageAN": ["AC Voltage AN", "acvoltagean", "V", None, DEVICE_CLASS_VOLTAGE],
    "AC_VoltageBN": ["AC Voltage BN", "acvoltagebn", "V", None, DEVICE_CLASS_VOLTAGE],
    "AC_VoltageCN": ["AC Voltage CN", "acvoltagecn", "V", None, DEVICE_CLASS_VOLTAGE],
    "AC_Power": ["AC Power", "acpower", "W", "mdi:solar-power", DEVICE_CLASS_POWER],
    "AC_Frequency": ["AC Frequency", "acfreq", "Hz", None, None],
    "AC_VA": ["AC VA", "acva", "VA", None, DEVICE_CLASS_POWER],
    "AC_VAR": ["AC VAR", "acvar", "VAR", None, DEVICE_CLASS_POWER],
    "AC_PF": ["AC PF", "acpf", "%", None, DEVICE_CLASS_POWER_FACTOR],
    "AC_Energy_KWH": ["AC Energy KWH", "acenergy", "kWh", "mdi:solar-power", DEVICE_CLASS_ENERGY],
    "DC_Current": ["DC Current", "dccurrent", "A", "mdi:current-dc", DEVICE_CLASS_CURRENT,
    "DC_Voltage": ["DC Voltage", "dcvoltage", "V", None, DEVICE_CLASS_VOLTAGE],
    "DC_Power": ["DC Power", "dcpower", "W", "mdi:solar-power", DEVICE_CLASS_POWER],
    "Temp_Sink": ["Temp Sink", "tempsink", "°C", None, DEVICE_CLASS_TEMPERATURE],
    "Status": ["Status", "status", None, None, None],
    "Status_Vendor": ["Status Vendor", "statusvendor", None, None, None],
}


METER1_SENSOR_TYPES = {
    "M1_AC_Current": ["M1 AC Current", "m1_accurrent", "A", "mdi:current-ac", DEVICE_CLASS_CURRENT],
    "M1_AC_Current_A": ["M1 AC Current_A", "m1_accurrenta", "A", "mdi:current-ac", DEVICE_CLASS_CURRENT],
    "M1_AC_Current_B": ["M1 AC Current_B", "m1_accurrentb", "A", "mdi:current-ac", DEVICE_CLASS_CURRENT],
    "M1_AC_Current_C": ["M1 AC Current_C", "m1_accurrentc", "A", "mdi:current-ac", DEVICE_CLASS_CURRENT],
    "M1_AC_Voltage_LN": ["M1 AC Voltage LN", "m1_acvoltageln", "V", None, DEVICE_CLASS_VOLTAGE],
    "M1_AC_Voltage_AN": ["M1 AC Voltage AN", "m1_acvoltagean", "V", None, DEVICE_CLASS_VOLTAGE],
    "M1_AC_Voltage_BN": ["M1 AC Voltage BN", "m1_acvoltagebn", "V", None, DEVICE_CLASS_VOLTAGE],
    "M1_AC_Voltage_CN": ["M1 AC Voltage CN", "m1_acvoltagecn", "V", None, DEVICE_CLASS_VOLTAGE],
    "M1_AC_Voltage_LL": ["M1 AC Voltage LL", "m1_acvoltagell", "V", None, DEVICE_CLASS_VOLTAGE],
    "M1_AC_Voltage_AB": ["M1 AC Voltage AB", "m1_acvoltageab", "V", None, DEVICE_CLASS_VOLTAGE],
    "M1_AC_Voltage_BC": ["M1 AC Voltage BC", "m1_acvoltagebc", "V", None, DEVICE_CLASS_VOLTAGE],
    "M1_AC_Voltage_CA": ["M1 AC Voltage CA", "m1_acvoltageca", "V", None, DEVICE_CLASS_VOLTAGE],
    "M1_AC_Frequency": ["M1 AC Frequency", "m1_acfreq", "Hz", None, None],
    "M1_AC_Power": ["M1 AC Power", "m1_acpower", "W", None, DEVICE_CLASS_POWER],
    "M1_AC_Power_A": ["M1 AC Power A", "m1_acpowera", "W", None, DEVICE_CLASS_POWER],
    "M1_AC_Power_B": ["M1 AC Power B", "m1_acpowerb", "W", None, DEVICE_CLASS_POWER],
    "M1_AC_Power_C": ["M1 AC Power C", "m1_acpowerc", "W", None, DEVICE_CLASS_POWER],
    "M1_AC_VA": ["M1 AC VA", "m1_acva", "VA", None, DEVICE_CLASS_POWER],
    "M1_AC_VA_A": ["M1 AC VA A", "m1_acvaa", "VA", None, DEVICE_CLASS_POWER],
    "M1_AC_VA_B": ["M1 AC VA B", "m1_acvab", "VA", None, DEVICE_CLASS_POWER],
    "M1_AC_VA_C": ["M1 AC VA C", "m1_acvac", "VA", None, DEVICE_CLASS_POWER],
    "M1_AC_VAR": ["M1 AC VAR", "m1_acvar", "VAR", None, DEVICE_CLASS_POWER],
    "M1_AC_VAR_A": ["M1 AC VAR A", "m1_acvara", "VAR", None, DEVICE_CLASS_POWER],
    "M1_AC_VAR_B": ["M1 AC VAR B", "m1_acvarb", "VAR", None, DEVICE_CLASS_POWER],
    "M1_AC_VAR_C": ["M1 AC VAR C", "m1_acvarc", "VAR", None, DEVICE_CLASS_POWER],
    "M1_AC_PF": ["M1 AC PF", "m1_acpf", "%", None, DEVICE_CLASS_POWER_FACTOR],
    "M1_AC_PF_A": ["M1 AC PF A", "m1_acpfa", "%", None, DEVICE_CLASS_POWER_FACTOR],
    "M1_AC_PF_B": ["M1 AC PF B", "m1_acpfb", "%", None, DEVICE_CLASS_POWER_FACTOR],
    "M1_AC_PF_C": ["M1 AC PF C", "m1_acpfc", "%", None, DEVICE_CLASS_POWER_FACTOR],
    "M1_EXPORTED_KWH": ["M1 EXPORTED KWH", "m1_exported", "kWh", None, DEVICE_CLASS_ENERGY],
    "M1_EXPORTED_A_KWH": ["M1 EXPORTED A KWH", "m1_exporteda", "kWh", None, DEVICE_CLASS_ENERGY],
    "M1_EXPORTED_B_KWH": ["M1 EXPORTED B KWH", "m1_exportedb", "kWh", None, DEVICE_CLASS_ENERGY],
    "M1_EXPORTED_C_KWH": ["M1 EXPORTED C KWH", "m1_exportedc", "kWh", None, DEVICE_CLASS_ENERGY],
    "M1_IMPORTED_KWH": ["M1 IMPORTED KWH", "m1_imported", "kWh", None, DEVICE_CLASS_ENERGY],
    "M1_IMPORTED_KWH_A": ["M1 IMPORTED A KWH", "m1_importeda", "kWh", None, DEVICE_CLASS_ENERGY],
    "M1_IMPORTED_KWH_B": ["M1 IMPORTED B KWH", "m1_importedb", "kWh", None, DEVICE_CLASS_ENERGY],
    "M1_IMPORTED_KWH_C": ["M1 IMPORTED C KWH", "m1_importedc", "kWh", None, DEVICE_CLASS_ENERGY],
    "M1_EXPORTED_VA": ["M1 EXPORTED VAh", "m1_exportedva", "VAh", None, DEVICE_CLASS_ENERGY],
    "M1_EXPORTED_VA_A": ["M1 EXPORTED A VAh", "m1_exportedvaa", "VAh", None, DEVICE_CLASS_ENERGY],
    "M1_EXPORTED_VA_B": ["M1 EXPORTED B VAh", "m1_exportedvab", "VAh", None, DEVICE_CLASS_ENERGY],
    "M1_EXPORTED_VA_C": ["M1 EXPORTED C VAh", "m1_exportedvac", "VAh", None, DEVICE_CLASS_ENERGY],
    "M1_IMPORTED_VA": ["M1 IMPORTED VAh", "m1_importedva", "VAh", None, DEVICE_CLASS_ENERGY],
    "M1_IMPORTED_VA_A": ["M1 IMPORTED A VAh", "m1_importedvaa", "VAh", None, DEVICE_CLASS_ENERGY],
    "M1_IMPORTED_VA_B": ["M1 IMPORTED B VAh", "m1_importedvab", "VAh", None, DEVICE_CLASS_ENERGY],
    "M1_IMPORTED_VA_C": ["M1 IMPORTED C VAh", "m1_importedvac", "VAh", None, DEVICE_CLASS_ENERGY],
    "M1_IMPORT_VARH_Q1": ["M1 IMPORT VARH Q1", "m1_importvarhq1", "VARh", None, DEVICE_CLASS_ENERGY],
    "M1_IMPORT_VARH_Q1_A": ["M1 IMPORT VARH Q1 A", "m1_importvarhq1a", "VARh", None, DEVICE_CLASS_ENERGY],
    "M1_IMPORT_VARH_Q1_B": ["M1 IMPORT VARH Q1 B", "m1_importvarhq1b", "VARh", None, DEVICE_CLASS_ENERGY],
    "M1_IMPORT_VARH_Q1_C": ["M1 IMPORT VARH Q1 C", "m1_importvarhq1c", "VARh", None, DEVICE_CLASS_ENERGY],
    "M1_IMPORT_VARH_Q2": ["M1 IMPORT VARH Q2", "m1_importvarhq2", "VARh", None, DEVICE_CLASS_ENERGY],
    "M1_IMPORT_VARH_Q2_A": ["M1 IMPORT VARH Q2 A", "m1_importvarhq2a", "VARh", None, DEVICE_CLASS_ENERGY],
    "M1_IMPORT_VARH_Q2_B": ["M1 IMPORT VARH Q2 B", "m1_importvarhq2b", "VARh", None, DEVICE_CLASS_ENERGY],
    "M1_IMPORT_VARH_Q2_C": ["M1 IMPORT VARH Q2 C", "m1_importvarhq2c", "VARh", None, DEVICE_CLASS_ENERGY],
    "M1_IMPORT_VARH_Q3": ["M1 IMPORT VARH Q3", "m1_importvarhq3", "VARh", None, DEVICE_CLASS_ENERGY],
    "M1_IMPORT_VARH_Q3_A": ["M1 IMPORT VARH Q3 A", "m1_importvarhq3a", "VARh", None, DEVICE_CLASS_ENERGY],
    "M1_IMPORT_VARH_Q3_B": ["M1 IMPORT VARH Q3 B", "m1_importvarhq3b", "VARh", None, DEVICE_CLASS_ENERGY],
    "M1_IMPORT_VARH_Q3_C": ["M1 IMPORT VARH Q3 C", "m1_importvarhq3c", "VARh", None, DEVICE_CLASS_ENERGY],
    "M1_IMPORT_VARH_Q4": ["M1 IMPORT VARH Q4", "m1_importvarhq4", "VARh", None, DEVICE_CLASS_ENERGY],
    "M1_IMPORT_VARH_Q4_A": ["M1 IMPORT VARH Q4 A", "m1_importvarhq4a", "VARh", None, DEVICE_CLASS_ENERGY],
    "M1_IMPORT_VARH_Q4_B": ["M1 IMPORT VARH Q4 B", "m1_importvarhq4b", "VARh", None, DEVICE_CLASS_ENERGY],
    "M1_IMPORT_VARH_Q4_C": ["M1 IMPORT VARH Q4 C", "m1_importvarhq4c", "VARh", None, DEVICE_CLASS_ENERGY],
}

METER2_SENSOR_TYPES = {
    "M2_AC_Current": ["M2 AC Current", "m2_accurrent", "A", "mdi:current-ac", DEVICE_CLASS_CURRENT],
    "M2_AC_Current_A": ["M2 AC Current_A", "m2_accurrenta", "A", "mdi:current-ac", DEVICE_CLASS_CURRENT],
    "M2_AC_Current_B": ["M2 AC Current_B", "m2_accurrentb", "A", "mdi:current-ac", DEVICE_CLASS_CURRENT],
    "M2_AC_Current_C": ["M2 AC Current_C", "m2_accurrentc", "A", "mdi:current-ac", DEVICE_CLASS_CURRENT],
    "M2_AC_Voltage_LN": ["M2 AC Voltage LN", "m2_acvoltageln", "V", None, DEVICE_CLASS_VOLTAGE],
    "M2_AC_Voltage_AN": ["M2 AC Voltage AN", "m2_acvoltagean", "V", None, DEVICE_CLASS_VOLTAGE],
    "M2_AC_Voltage_BN": ["M2 AC Voltage BN", "m2_acvoltagebn", "V", None, DEVICE_CLASS_VOLTAGE],
    "M2_AC_Voltage_CN": ["M2 AC Voltage CN", "m2_acvoltagecn", "V", None, DEVICE_CLASS_VOLTAGE],
    "M2_AC_Voltage_LL": ["M2 AC Voltage LL", "m2_acvoltagell", "V", None, DEVICE_CLASS_VOLTAGE],
    "M2_AC_Voltage_AB": ["M2 AC Voltage AB", "m2_acvoltageab", "V", None, DEVICE_CLASS_VOLTAGE],
    "M2_AC_Voltage_BC": ["M2 AC Voltage BC", "m2_acvoltagebc", "V", None, DEVICE_CLASS_VOLTAGE],
    "M2_AC_Voltage_CA": ["M2 AC Voltage CA", "m2_acvoltageca", "V", None, DEVICE_CLASS_VOLTAGE],
    "M2_AC_Frequency": ["M2 AC Frequency", "m2_acfreq", "Hz", None, None],
    "M2_AC_Power": ["M2 AC Power", "m2_acpower", "W", None, DEVICE_CLASS_POWER],
    "M2_AC_Power_A": ["M2 AC Power A", "m2_acpowera", "W", None, DEVICE_CLASS_POWER],
    "M2_AC_Power_B": ["M2 AC Power B", "m2_acpowerb", "W", None, DEVICE_CLASS_POWER],
    "M2_AC_Power_C": ["M2 AC Power C", "m2_acpowerc", "W", None, DEVICE_CLASS_POWER],
    "M2_AC_VA": ["M2 AC VA", "m2_acva", "VA", None, DEVICE_CLASS_POWER],
    "M2_AC_VA_A": ["M2 AC VA A", "m2_acvaa", "VA", None, DEVICE_CLASS_POWER],
    "M2_AC_VA_B": ["M2 AC VA B", "m2_acvab", "VA", None, DEVICE_CLASS_POWER],
    "M2_AC_VA_C": ["M2 AC VA C", "m2_acvac", "VA", None, DEVICE_CLASS_POWER],
    "M2_AC_VAR": ["M2 AC VAR", "m2_acvar", "VAR", None, DEVICE_CLASS_POWER],
    "M2_AC_VAR_A": ["M2 AC VAR A", "m2_acvara", "VAR", None, DEVICE_CLASS_POWER],
    "M2_AC_VAR_B": ["M2 AC VAR B", "m2_acvarb", "VAR", None, DEVICE_CLASS_POWER],
    "M2_AC_VAR_C": ["M2 AC VAR C", "m2_acvarc", "VAR", None, DEVICE_CLASS_POWER],
    "M2_AC_PF": ["M2 AC PF", "m2_acpf", "%", None, DEVICE_CLASS_POWER_FACTOR],
    "M2_AC_PF_A": ["M2 AC PF A", "m2_acpfa", "%", None, DEVICE_CLASS_POWER_FACTOR],
    "M2_AC_PF_B": ["M2 AC PF B", "m2_acpfb", "%", None, DEVICE_CLASS_POWER_FACTOR],
    "M2_AC_PF_C": ["M2 AC PF C", "m2_acpfc", "%", None, DEVICE_CLASS_POWER_FACTOR],
    "M2_EXPORTED_KWH": ["M2 EXPORTED KWH", "m2_exported", "kWh", None, DEVICE_CLASS_ENERGY],
    "M2_EXPORTED_A_KWH": ["M2 EXPORTED A KWH", "m2_exporteda", "kWh", None, DEVICE_CLASS_ENERGY],
    "M2_EXPORTED_B_KWH": ["M2 EXPORTED B KWH", "m2_exportedb", "kWh", None, DEVICE_CLASS_ENERGY],
    "M2_EXPORTED_C_KWH": ["M2 EXPORTED C KWH", "m2_exportedc", "kWh", None, DEVICE_CLASS_ENERGY],
    "M2_IMPORTED_KWH": ["M2 IMPORTED KWH", "m2_imported", "kWh", None, DEVICE_CLASS_ENERGY],
    "M2_IMPORTED_KWH_A": ["M2 IMPORTED A KWH", "m2_importeda", "kWh", None, DEVICE_CLASS_ENERGY],
    "M2_IMPORTED_KWH_B": ["M2 IMPORTED B KWH", "m2_importedb", "kWh", None, DEVICE_CLASS_ENERGY],
    "M2_IMPORTED_KWH_C": ["M2 IMPORTED C KWH", "m2_importedc", "kWh", None, DEVICE_CLASS_ENERGY],
    "M2_EXPORTED_VA": ["M2 EXPORTED VAh", "m2_exportedva", "VAh", None, DEVICE_CLASS_ENERGY],
    "M2_EXPORTED_VA_A": ["M2 EXPORTED A VAh", "m2_exportedvaa", "VAh", None, DEVICE_CLASS_ENERGY],
    "M2_EXPORTED_VA_B": ["M2 EXPORTED B VAh", "m2_exportedvab", "VAh", None, DEVICE_CLASS_ENERGY],
    "M2_EXPORTED_VA_C": ["M2 EXPORTED C VAh", "m2_exportedvac", "VAh", None, DEVICE_CLASS_ENERGY],
    "M2_IMPORTED_VA": ["M2 IMPORTED VAh", "m2_importedva", "VAh", None, DEVICE_CLASS_ENERGY],
    "M2_IMPORTED_VA_A": ["M2 IMPORTED A VAh", "m2_importedvaa", "VAh", None, DEVICE_CLASS_ENERGY],
    "M2_IMPORTED_VA_B": ["M2 IMPORTED B VAh", "m2_importedvab", "VAh", None, DEVICE_CLASS_ENERGY],
    "M2_IMPORTED_VA_C": ["M2 IMPORTED C VAh", "m2_importedvac", "VAh", None, DEVICE_CLASS_ENERGY],
    "M2_IMPORT_VARH_Q1": ["M2 IMPORT VARH Q1", "m2_importvarhq1", "VARh", None, DEVICE_CLASS_ENERGY],
    "M2_IMPORT_VARH_Q1_A": ["M2 IMPORT VARH Q1 A", "m2_importvarhq1a", "VARh", None, DEVICE_CLASS_ENERGY],
    "M2_IMPORT_VARH_Q1_B": ["M2 IMPORT VARH Q1 B", "m2_importvarhq1b", "VARh", None, DEVICE_CLASS_ENERGY],
    "M2_IMPORT_VARH_Q1_C": ["M2 IMPORT VARH Q1 C", "m2_importvarhq1c", "VARh", None, DEVICE_CLASS_ENERGY],
    "M2_IMPORT_VARH_Q2": ["M2 IMPORT VARH Q2", "m2_importvarhq2", "VARh", None, DEVICE_CLASS_ENERGY],
    "M2_IMPORT_VARH_Q2_A": ["M2 IMPORT VARH Q2 A", "m2_importvarhq2a", "VARh", None, DEVICE_CLASS_ENERGY],
    "M2_IMPORT_VARH_Q2_B": ["M2 IMPORT VARH Q2 B", "m2_importvarhq2b", "VARh", None, DEVICE_CLASS_ENERGY],
    "M2_IMPORT_VARH_Q2_C": ["M2 IMPORT VARH Q2 C", "m2_importvarhq2c", "VARh", None, DEVICE_CLASS_ENERGY],
    "M2_IMPORT_VARH_Q3": ["M2 IMPORT VARH Q3", "m2_importvarhq3", "VARh", None, DEVICE_CLASS_ENERGY],
    "M2_IMPORT_VARH_Q3_A": ["M2 IMPORT VARH Q3 A", "m2_importvarhq3a", "VARh", None, DEVICE_CLASS_ENERGY],
    "M2_IMPORT_VARH_Q3_B": ["M2 IMPORT VARH Q3 B", "m2_importvarhq3b", "VARh", None, DEVICE_CLASS_ENERGY],
    "M2_IMPORT_VARH_Q3_C": ["M2 IMPORT VARH Q3 C", "m2_importvarhq3c", "VARh", None, DEVICE_CLASS_ENERGY],
    "M2_IMPORT_VARH_Q4": ["M2 IMPORT VARH Q4", "m2_importvarhq4", "VARh", None, DEVICE_CLASS_ENERGY],
    "M2_IMPORT_VARH_Q4_A": ["M2 IMPORT VARH Q4 A", "m2_importvarhq4a", "VARh", None, DEVICE_CLASS_ENERGY],
    "M2_IMPORT_VARH_Q4_B": ["M2 IMPORT VARH Q4 B", "m2_importvarhq4b", "VARh", None, DEVICE_CLASS_ENERGY],
    "M2_IMPORT_VARH_Q4_C": ["M2 IMPORT VARH Q4 C", "m2_importvarhq4c", "VARh", None, DEVICE_CLASS_ENERGY],
}

METER3_SENSOR_TYPES = {
    "M3_AC_Current": ["M3 AC Current", "m3_accurrent", "A", "mdi:current-ac", DEVICE_CLASS_CURRENT],
    "M3_AC_Current_A": ["M3 AC Current_A", "m3_accurrenta", "A", "mdi:current-ac", DEVICE_CLASS_CURRENT],
    "M3_AC_Current_B": ["M3 AC Current_B", "m3_accurrentb", "A", "mdi:current-ac", DEVICE_CLASS_CURRENT],
    "M3_AC_Current_C": ["M3 AC Current_C", "m3_accurrentc", "A", "mdi:current-ac", DEVICE_CLASS_CURRENT],
    "M3_AC_Voltage_LN": ["M3 AC Voltage LN", "m3_acvoltageln", "V", None, DEVICE_CLASS_VOLTAGE],
    "M3_AC_Voltage_AN": ["M3 AC Voltage AN", "m3_acvoltagean", "V", None, DEVICE_CLASS_VOLTAGE],
    "M3_AC_Voltage_BN": ["M3 AC Voltage BN", "m3_acvoltagebn", "V", None, DEVICE_CLASS_VOLTAGE],
    "M3_AC_Voltage_CN": ["M3 AC Voltage CN", "m3_acvoltagecn", "V", None, DEVICE_CLASS_VOLTAGE],
    "M3_AC_Voltage_LL": ["M3 AC Voltage LL", "m3_acvoltagell", "V", None, DEVICE_CLASS_VOLTAGE],
    "M3_AC_Voltage_AB": ["M3 AC Voltage AB", "m3_acvoltageab", "V", None, DEVICE_CLASS_VOLTAGE],
    "M3_AC_Voltage_BC": ["M3 AC Voltage BC", "m3_acvoltagebc", "V", None, DEVICE_CLASS_VOLTAGE],
    "M3_AC_Voltage_CA": ["M3 AC Voltage CA", "m3_acvoltageca", "V", None, DEVICE_CLASS_VOLTAGE],
    "M3_AC_Frequency": ["M3 AC Frequency", "m3_acfreq", "Hz", None, None],
    "M3_AC_Power": ["M3 AC Power", "m3_acpower", "W", None, DEVICE_CLASS_POWER],
    "M3_AC_Power_A": ["M3 AC Power A", "m3_acpowera", "W", None, DEVICE_CLASS_POWER],
    "M3_AC_Power_B": ["M3 AC Power B", "m3_acpowerb", "W", None, DEVICE_CLASS_POWER],
    "M3_AC_Power_C": ["M3 AC Power C", "m3_acpowerc", "W", None, DEVICE_CLASS_POWER],
    "M3_AC_VA": ["M3 AC VA", "m3_acva", "VA", None, DEVICE_CLASS_POWER],
    "M3_AC_VA_A": ["M3 AC VA A", "m3_acvaa", "VA", None, DEVICE_CLASS_POWER],
    "M3_AC_VA_B": ["M3 AC VA B", "m3_acvab", "VA", None, DEVICE_CLASS_POWER],
    "M3_AC_VA_C": ["M3 AC VA C", "m3_acvac", "VA", None, DEVICE_CLASS_POWER],
    "M3_AC_VAR": ["M3 AC VAR", "m3_acvar", "VAR", None, DEVICE_CLASS_POWER],
    "M3_AC_VAR_A": ["M3 AC VAR A", "m3_acvara", "VAR", None, DEVICE_CLASS_POWER],
    "M3_AC_VAR_B": ["M3 AC VAR B", "m3_acvarb", "VAR", None, DEVICE_CLASS_POWER],
    "M3_AC_VAR_C": ["M3 AC VAR C", "m3_acvarc", "VAR", None, DEVICE_CLASS_POWER],
    "M3_AC_PF": ["M3 AC PF", "m3_acpf", "%", None, DEVICE_CLASS_POWER_FACTOR],
    "M3_AC_PF_A": ["M3 AC PF A", "m3_acpfa", "%", None, DEVICE_CLASS_POWER_FACTOR],
    "M3_AC_PF_B": ["M3 AC PF B", "m3_acpfb", "%", None, DEVICE_CLASS_POWER_FACTOR],
    "M3_AC_PF_C": ["M3 AC PF C", "m3_acpfc", "%", None, DEVICE_CLASS_POWER_FACTOR],
    "M3_EXPORTED_KWH": ["M3 EXPORTED KWH", "m3_exported", "kWh", None, DEVICE_CLASS_ENERGY],
    "M3_EXPORTED_A_KWH": ["M3 EXPORTED A KWH", "m3_exporteda", "kWh", None, DEVICE_CLASS_ENERGY],
    "M3_EXPORTED_B_KWH": ["M3 EXPORTED B KWH", "m3_exportedb", "kWh", None, DEVICE_CLASS_ENERGY],
    "M3_EXPORTED_C_KWH": ["M3 EXPORTED C KWH", "m3_exportedc", "kWh", None, DEVICE_CLASS_ENERGY],
    "M3_IMPORTED_KWH": ["M3 IMPORTED KWH", "m3_imported", "kWh", None, DEVICE_CLASS_ENERGY],
    "M3_IMPORTED_KWH_A": ["M3 IMPORTED A KWH", "m3_importeda", "kWh", None, DEVICE_CLASS_ENERGY],
    "M3_IMPORTED_KWH_B": ["M3 IMPORTED B KWH", "m3_importedb", "kWh", None, DEVICE_CLASS_ENERGY],
    "M3_IMPORTED_KWH_C": ["M3 IMPORTED C KWH", "m3_importedc", "kWh", None, DEVICE_CLASS_ENERGY],
    "M3_EXPORTED_VA": ["M3 EXPORTED VAh", "m3_exportedva", "VAh", None, DEVICE_CLASS_ENERGY],
    "M3_EXPORTED_VA_A": ["M3 EXPORTED A VAh", "m3_exportedvaa", "VAh", None, DEVICE_CLASS_ENERGY],
    "M3_EXPORTED_VA_B": ["M3 EXPORTED B VAh", "m3_exportedvab", "VAh", None, DEVICE_CLASS_ENERGY],
    "M3_EXPORTED_VA_C": ["M3 EXPORTED C VAh", "m3_exportedvac", "VAh", None, DEVICE_CLASS_ENERGY],
    "M3_IMPORTED_VA": ["M3 IMPORTED VAh", "m3_importedva", "VAh", None, DEVICE_CLASS_ENERGY],
    "M3_IMPORTED_VA_A": ["M3 IMPORTED A VAh", "m3_importedvaa", "VAh", None, DEVICE_CLASS_ENERGY],
    "M3_IMPORTED_VA_B": ["M3 IMPORTED B VAh", "m3_importedvab", "VAh", None, DEVICE_CLASS_ENERGY],
    "M3_IMPORTED_VA_C": ["M3 IMPORTED C VAh", "m3_importedvac", "VAh", None, DEVICE_CLASS_ENERGY],
    "M3_IMPORT_VARH_Q1": ["M3 IMPORT VARH Q1", "m3_importvarhq1", "VARh", None, DEVICE_CLASS_ENERGY],
    "M3_IMPORT_VARH_Q1_A": ["M3 IMPORT VARH Q1 A", "m3_importvarhq1a", "VARh", None, DEVICE_CLASS_ENERGY],
    "M3_IMPORT_VARH_Q1_B": ["M3 IMPORT VARH Q1 B", "m3_importvarhq1b", "VARh", None, DEVICE_CLASS_ENERGY],
    "M3_IMPORT_VARH_Q1_C": ["M3 IMPORT VARH Q1 C", "m3_importvarhq1c", "VARh", None, DEVICE_CLASS_ENERGY],
    "M3_IMPORT_VARH_Q2": ["M3 IMPORT VARH Q2", "m3_importvarhq2", "VARh", None, DEVICE_CLASS_ENERGY],
    "M3_IMPORT_VARH_Q2_A": ["M3 IMPORT VARH Q2 A", "m3_importvarhq2a", "VARh", None, DEVICE_CLASS_ENERGY],
    "M3_IMPORT_VARH_Q2_B": ["M3 IMPORT VARH Q2 B", "m3_importvarhq2b", "VARh", None, DEVICE_CLASS_ENERGY],
    "M3_IMPORT_VARH_Q2_C": ["M3 IMPORT VARH Q2 C", "m3_importvarhq2c", "VARh", None, DEVICE_CLASS_ENERGY],
    "M3_IMPORT_VARH_Q3": ["M3 IMPORT VARH Q3", "m3_importvarhq3", "VARh", None, DEVICE_CLASS_ENERGY],
    "M3_IMPORT_VARH_Q3_A": ["M3 IMPORT VARH Q3 A", "m3_importvarhq3a", "VARh", None, DEVICE_CLASS_ENERGY],
    "M3_IMPORT_VARH_Q3_B": ["M3 IMPORT VARH Q3 B", "m3_importvarhq3b", "VARh", None, DEVICE_CLASS_ENERGY],
    "M3_IMPORT_VARH_Q3_C": ["M3 IMPORT VARH Q3 C", "m3_importvarhq3c", "VARh", None, DEVICE_CLASS_ENERGY],
    "M3_IMPORT_VARH_Q4": ["M3 IMPORT VARH Q4", "m3_importvarhq4", "VARh", None, DEVICE_CLASS_ENERGY],
    "M3_IMPORT_VARH_Q4_A": ["M3 IMPORT VARH Q4 A", "m3_importvarhq4a", "VARh", None, DEVICE_CLASS_ENERGY],
    "M3_IMPORT_VARH_Q4_B": ["M3 IMPORT VARH Q4 B", "m3_importvarhq4b", "VARh", None, DEVICE_CLASS_ENERGY],
    "M3_IMPORT_VARH_Q4_C": ["M3 IMPORT VARH Q4 C", "m3_importvarhq4c", "VARh", None, DEVICE_CLASS_ENERGY],
}

DEVICE_STATUSSES = {
    1: "Off",
    2: "Sleeping (auto-shutdown) – Night mode",
    3: "Grid Monitoring/wake-up",
    4: "Inverter is ON and producing power",
    5: "Production (curtailed)",
    6: "Shutting down",
    7: "Fault",
    8: "Maintenance/setup",
}
