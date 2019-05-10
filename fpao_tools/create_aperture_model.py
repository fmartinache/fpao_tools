#!/usr/bin/env python3

''' ---------------------------------------------------------------------------
This tiny script uses tools from the xara and the xaosim packages to create a
discrete representation of the SCExAO asymmetric aperture used by "qtzap" for
wavefront sensing purposes.

The end product is a multi-extension fits file that contains most of the 
information required by "qtzap" to compute a wavefront from a direct focal
image, based on the "eigen-phase".

The script is appended to the package here so as to provide the user with 
the means to update the model.
--------------------------------------------------------------------------- '''

import xaosim as xs
import xara

pdiam   = 7.92 # telescope diameter in meters
ppscale = 0.01 # pupil scale (in meters per pixel)
step    = 0.40 # model grid step (in meters)

psz = int(pdiam / ppscale) # size of the representation of the pupil (in pixels)

pupil = xs.pupil.subaru_asym(psz, psz, psz//2, spiders=True, PA=180., thick=0.15)

modl  = xara.core.create_discrete_model(pupil, ppscale, step, binary=True)
kmodl = xara.KPI(array=modl)
kmodl.save_to_file("scexao_asym_kmodel.fits")

