import arcpy
import os

#written to run with python 3.x

print("RUNNING SETUP")

output_gdb = r"\\besfile1\asm_projects\9ESEN22GI001\Stormwater_Manual\private_permit_pilot\dev\SWMM_FY_output.gdb"

sde_egh_public = r"\\oberon\grp117\DAshney\Scripts\connections"

EGH_PUBLIC = os.path.join(sde_egh_public, "egh_public on gisdb1.rose.portland.local.sde")

permit_sites = EGH_PUBLIC + r"\EGH_PUBLIC.ARCMAP_ADMIN.BES_SWMF_FINALED_STP_PDX"
MS4_boundaries = EGH_PUBLIC + r"\EGH_PUBLIC.ARCMAP_ADMIN.of_drainage_bounds_bes_pdx"
sewer_boundaries = EGH_PUBLIC + r"\EGH_PUBLIC.ARCMAP_ADMIN.sewer_basins_bes_pdx"

MS4_boundary_sub = arcpy.MakeFeatureLayer_management(MS4_boundaries, r"in_memory\MS4_boundary_sub", "Basin <> 'N/A' and Basin is not Null AND Boundary_Type= 'MS4'")
CSO_boundaries = arcpy.MakeFeatureLayer_management(sewer_boundaries, r"in_memory\combined_boundaries", "TYPE = 'C'")

permit_sites_copy = arcpy.CopyFeatures_management(permit_sites, r"in_memory\permit_sites_copy")
arcpy.AddFields_management(permit_sites_copy, [
    ["MS4", "SHORT"],
    ["CSO", "SHORT"]
])