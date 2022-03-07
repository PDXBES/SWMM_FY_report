import config
import arcpy
import os
import utility


def run_FY_sums(fiscal_year):
    print("STARTING FY SUM PROCESS")
    begin_year = fiscal_year - 1
    #date_string = "FINALDATE >= '{}-07-01' AND FINALDATE <= '{}-06-30'".format(begin_year, fiscal_year)
    date_string = "\"FINALDATE\" >= date'{}-07-01' AND \"FINALDATE\" <= date'{}-06-30'".format(begin_year, fiscal_year)
    # arcpy.management.SelectLayerByAttribute(config.permit_sites_copy, "NEW_SELECTION", date_string)
    FY_permits = arcpy.management.MakeFeatureLayer(config.permit_sites_copy, "in_memory\FY_permits", date_string)
    # select by location vs MS4, fill field with 1 if overlap
    utility.set_to_1_if_overlap(FY_permits, config.MS4_boundary_sub, "MS4")
    # select by location vs CSO, fill field with 1 if overlap
    utility.set_to_1_if_overlap(FY_permits, config.CSO_boundaries, "CSO")
    # run summary statistics - hard copy output
    sum_table = os.path.join(config.output_gdb, "FY" + str(fiscal_year) + "_sums")
    arcpy.analysis.Statistics(FY_permits, sum_table, "TRIGGERED_IMPRVS_SQFT SUM; FCLTY_TOT_IMPRVS_SQFT SUM", "MS4;CSO")
    # save out intermediate table for QC
    working_fc = os.path.join(config.output_gdb, "FY" + str(fiscal_year) + "_working")
    arcpy.CopyFeatures_management(FY_permits, working_fc)
    print("FY SUM PROCESS COMPLETE")
    print("Outputs saved to " + config.output_gdb)

fiscal_year = 2021
run_FY_sums(fiscal_year)
