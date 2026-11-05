# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

cmake_minimum_required(VERSION 3.16)
project(decNumber VERSION 3.68 LANGUAGES C)
include(GNUInstallDirs)
include(TestBigEndian)
test_big_endian(DECNUMBER_BIG_ENDIAN)
if(DECNUMBER_BIG_ENDIAN)
    set(DECNUMBER_LITTLE_ENDIAN 0)
else()
    set(DECNUMBER_LITTLE_ENDIAN 1)
endif()
add_library(decNumber SHARED decNumber.c decContext.c decDouble.c decQuad.c
    decSingle.c decPacked.c decimal32.c decimal64.c decimal128.c)
target_compile_definitions(decNumber PRIVATE DECLITEND=${DECNUMBER_LITTLE_ENDIAN})
set_target_properties(decNumber PROPERTIES VERSION ${PROJECT_VERSION} SOVERSION 3)
install(TARGETS decNumber LIBRARY DESTINATION ${CMAKE_INSTALL_LIBDIR})
install(FILES decNumber.h decContext.h decDouble.h decQuad.h decSingle.h
    decPacked.h decimal32.h decimal64.h decimal128.h
    DESTINATION ${CMAKE_INSTALL_INCLUDEDIR}/decnumber)
configure_file(decnumber.pc.in decnumber.pc @ONLY)
install(FILES ${CMAKE_CURRENT_BINARY_DIR}/decnumber.pc
    DESTINATION ${CMAKE_INSTALL_LIBDIR}/pkgconfig)
