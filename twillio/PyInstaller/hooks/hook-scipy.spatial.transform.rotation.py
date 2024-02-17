#-----------------------------------------------------------------------------
# Copyright (c) 2021-2022, PyInstaller Development Team.
#
# Distributed under the terms of the GNU General Public License (version 2
# or later) with exception for distributing the bootloader.
#
# The full license is in the file COPYING.txt, distributed with this software.
#
# SPDX-License-Identifier: (GPL-2.0-or-later WITH Bootloader-exception)
#-----------------------------------------------------------------------------

from PyInstaller.utils.hooks import is_module_satisfies

# As of scipy 1.6.0, scipy.spatial.transform.rotation is cython-compiled, so we fail to automatically pick up its
# imports.
if is_module_satisfies("scipy >= 1.6.0"):
    hiddenimports = ['scipy.spatial.transform._rotation_groups']
