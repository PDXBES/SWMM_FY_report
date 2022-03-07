import arcpy


def set_to_1_if_overlap(target_fc, overlap_fc, field_to_fill):
    arcpy.management.SelectLayerByLocation(target_fc, "HAVE_THEIR_CENTER_IN", overlap_fc, "#", "NEW_SELECTION")
    with arcpy.da.UpdateCursor(target_fc, [field_to_fill]) as cursor:
        for row in cursor:
            row[0] = 1
            cursor.updateRow(row)
    arcpy.management.SelectLayerByAttribute(target_fc, "CLEAR_SELECTION")
    with arcpy.da.UpdateCursor(target_fc, [field_to_fill]) as cursor:
        for row in cursor:
            if row[0] != 1:
                row[0] = 0
            cursor.updateRow(row)
    arcpy.management.SelectLayerByAttribute(target_fc, "CLEAR_SELECTION")