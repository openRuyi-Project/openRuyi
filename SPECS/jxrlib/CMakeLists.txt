cmake_minimum_required(VERSION 3.13)
project(jxrlib VERSION 1.4.2 LANGUAGES C)

include(GNUInstallDirs)

set(JXRLIB_LIB_VERSION ${PROJECT_VERSION})
set(JXRLIB_SO_VERSION 0)

#find_package(JNI)
#if (JNI_FOUND)
#    message (STATUS "JNI_INCLUDE_DIRS=${JNI_INCLUDE_DIRS}")
#    message (STATUS "JNI_LIBRARIES=${JNI_LIBRARIES}")
#    message (STATUS "JAVA_INCLUDE_PATH=${JAVA_INCLUDE_PATH}")
#    message (STATUS "JAVA_INCLUDE_PATH2=${JAVA_INCLUDE_PATH2}")
#endif()
#INCLUDE_DIRECTORIES(${JAVA_INCLUDE_PATH})
#INCLUDE_DIRECTORIES(${JAVA_INCLUDE_PATH2})

include(TestBigEndian)
test_big_endian(ISBIGENDIAN)
if(ISBIGENDIAN)
  set(DEF_ENDIAN -D_BIG__ENDIAN_)
endif()

add_definitions(-D__ANSI__ -DDISABLE_PERF_MEASUREMENT ${DEF_ENDIAN})

include_directories(
  common/include
  image/sys
  jxrgluelib
  jxrtestlib
)

# JXR Library
file(GLOB jpegxr_SRC image/sys/*.c image/decode/*.c image/encode/*.c)
file(GLOB jpegxr_HDR image/sys/*.h image/decode/*.h image/encode/*.h)

add_library(jpegxr SHARED ${jpegxr_SRC} ${jpegxr_HDR})
set_target_properties(jpegxr PROPERTIES VERSION ${JXRLIB_LIB_VERSION} SOVERSION ${JXRLIB_SO_VERSION})

install(TARGETS jpegxr
  RUNTIME DESTINATION ${CMAKE_INSTALL_BINDIR}
  LIBRARY DESTINATION ${CMAKE_INSTALL_LIBDIR}
  ARCHIVE DESTINATION ${CMAKE_INSTALL_LIBDIR}
)

# JXR-GLUE Library
file(GLOB jxrglue_SRC jxrgluelib/*.c jxrtestlib/*.c)
file(GLOB jxrglue_HDR jxrgluelib/*.h jxrtestlib/*.h)

add_library(jxrglue SHARED ${jxrglue_SRC} ${jxrglue_HDR})
set_target_properties(jxrglue PROPERTIES VERSION ${JXRLIB_LIB_VERSION} SOVERSION ${JXRLIB_SO_VERSION})
target_link_libraries(jxrglue jpegxr m)

install(TARGETS jxrglue
  RUNTIME DESTINATION ${CMAKE_INSTALL_BINDIR}
  LIBRARY DESTINATION ${CMAKE_INSTALL_LIBDIR}
  ARCHIVE DESTINATION ${CMAKE_INSTALL_LIBDIR}
)

# JXR-JAVA Library
#file(GLOB jxrjava_SRC java/target/swig/JXR_wrap.cxx cpp/lib/*.cpp)
#file(GLOB jxrjava_SRC cpp/lib/*.hpp)

#add_library(jxrjava SHARED ${jxrjava_SRC} ${jxrjava_HDR})
#set_target_properties(jxrjava PROPERTIES VERSION ${JXRLIB_LIB_VERSION} SOVERSION ${JXRLIB_SO_VERSION})
#target_link_libraries(jxrjava jpegxr m)

#install(TARGETS jxrjava
#  RUNTIME DESTINATION bin
#  LIBRARY DESTINATION lib${LIB_SUFFIX}
#  ARCHIVE DESTINATION lib${LIB_SUFFIX}
#)

# JxrEncApp Executable
add_executable(JxrEncApp jxrencoderdecoder/JxrEncApp.c)
target_link_libraries(JxrEncApp jxrglue)
install(TARGETS JxrEncApp RUNTIME DESTINATION ${CMAKE_INSTALL_BINDIR})

# JxrDecApp Executable
add_executable(JxrDecApp jxrencoderdecoder/JxrDecApp.c)
target_link_libraries(JxrDecApp jxrglue)
install(TARGETS JxrDecApp RUNTIME DESTINATION ${CMAKE_INSTALL_BINDIR})

# Headers
install(FILES jxrgluelib/JXRGlue.h jxrgluelib/JXRMeta.h jxrgluelib/JXRVersion.h
  jxrtestlib/JXRTest.h image/sys/windowsmediaphoto.h
  DESTINATION ${CMAKE_INSTALL_INCLUDEDIR}/jxrlib
)
install(DIRECTORY common/include/ DESTINATION ${CMAKE_INSTALL_INCLUDEDIR}/jxrlib
  FILES_MATCHING PATTERN "*.h"
)

file(WRITE ${CMAKE_CURRENT_BINARY_DIR}/libjxr.pc
  "prefix=${CMAKE_INSTALL_PREFIX}\n"
  "exec_prefix=\${prefix}\n"
  "libdir=${CMAKE_INSTALL_FULL_LIBDIR}\n"
  "includedir=\${prefix}/${CMAKE_INSTALL_INCLUDEDIR}\n\n"
  "Name: libjxr\n"
  "Description: A library for reading JPEG XR images.\n"
  "Version: ${PROJECT_VERSION}\n"
  "Libs: -L\${libdir} -ljpegxr -ljxrglue\n"
  "Libs.private: -lm\n"
  "Cflags: -I\${includedir}/jxrlib -D__ANSI__ -DDISABLE_PERF_MEASUREMENT\n"
)
install(FILES ${CMAKE_CURRENT_BINARY_DIR}/libjxr.pc
  DESTINATION ${CMAKE_INSTALL_LIBDIR}/pkgconfig
)
