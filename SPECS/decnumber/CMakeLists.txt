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

# Exercise the upstream examples against the shared library, including
# exact decimal arithmetic, quad precision, and long leading-zero input.
enable_testing()
add_executable(example1 example1.c)
target_link_libraries(example1 PRIVATE decNumber)
add_executable(example7 example7.c)
target_link_libraries(example7 PRIVATE decNumber)
add_executable(example8 example8.c)
target_compile_definitions(example8 PRIVATE DECNUMDIGITS=34)
target_link_libraries(example8 PRIVATE decNumber)
add_test(NAME number-add COMMAND example1 1.23 1.27)
set_tests_properties(number-add PROPERTIES PASS_REGULAR_EXPRESSION "=> 2[.]50")
add_test(NAME quad-add COMMAND example7 1.23 1.27)
set_tests_properties(quad-add PROPERTIES PASS_REGULAR_EXPRESSION "=> 2[.]50")
add_test(NAME quad-power COMMAND example8 2 3)
set_tests_properties(quad-power PROPERTIES PASS_REGULAR_EXPRESSION "=> 64")
string(REPEAT "0" 200 ZEROS)
add_test(NAME quad-leading-zeros COMMAND example7 "${ZEROS}1.25" 2.75)
set_tests_properties(quad-leading-zeros PROPERTIES PASS_REGULAR_EXPRESSION "=> 4[.]00")
add_test(NAME quad-zero-fraction COMMAND example7 "0.${ZEROS}" 0)
set_tests_properties(quad-zero-fraction PROPERTIES PASS_REGULAR_EXPRESSION "=> 0")
