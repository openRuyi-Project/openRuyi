# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: yyjeqhc <1772413353@qq.com>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           libjpeg-turbo
Version:        3.1.2
Release:        %autorelease
Summary:        A SIMD-accelerated library for manipulating JPEG image files
License:        Zlib AND BSD-3-Clause AND MIT AND IJG
URL:            https://github.com/libjpeg-turbo/libjpeg-turbo
#!RemoteAsset
Source:         https://github.com/libjpeg-turbo/libjpeg-turbo/archive/refs/tags/%{version}.tar.gz
Patch:          0001-libjpeg-turbo-cmake.patch
BuildSystem:    cmake

BuildOption(conf): -DENABLE_STATIC:BOOL=NO
BuildOption(conf): -DFLOATTEST:STRING="fp-contract"

BuildRequires:  gcc
BuildRequires:  cmake
BuildRequires:  libtool

%description
The libjpeg-turbo package contains a library of functions for manipulating JPEG
images, accelerated with SIMD instructions.

%package        devel
Summary:        Headers for the libjpeg-turbo library
Requires:       libjpeg-turbo = %{version}

%description    devel
This package contains header files necessary for developing programs which use
the libjpeg-turbo library.

%package        utils
Summary:        Utilities for manipulating JPEG images
Requires:       libjpeg-turbo = %{version}

%description    utils
This package contains command-line utilities for creating, decompressing, and
transforming JPEG files.

%package -n     turbojpeg
Summary:        TurboJPEG library
Requires:       libjpeg-turbo = %{version}

%description -n turbojpeg
This package contains the TurboJPEG shared library, a higher-level API for
JPEG compression and decompression.

%package -n     turbojpeg-devel
Summary:        Headers for the TurboJPEG library
Requires:       turbojpeg = %{version}
Requires:       libjpeg-turbo-devel = %{version}

%description -n turbojpeg-devel
This package contains header files for developing programs that use the
TurboJPEG library.

%install -a
find %{buildroot} -type f -name "*.la" -delete -print

rm -f %{buildroot}/%{_bindir}/tjbench

%files
%license LICENSE.md
%doc README.md README.ijg ChangeLog.md
%{_libdir}/libjpeg.so.62*

%files devel
%doc doc/coderules.txt src/jconfig.txt doc/libjpeg.txt doc/structure.txt
%{_includedir}/jconfig.h
%{_includedir}/jerror.h
%{_includedir}/jmorecfg.h
%{_includedir}/jpeglib.h
%{_includedir}/jpegint.h
%{_libdir}/libjpeg.so
%{_libdir}/pkgconfig/libjpeg.pc
%dir %{_libdir}/cmake/libjpeg-turbo
%{_libdir}/cmake/libjpeg-turbo/*.cmake

%files utils
%doc doc/usage.txt doc/wizard.txt
%{_bindir}/cjpeg
%{_bindir}/djpeg
%{_bindir}/jpegtran
%{_bindir}/rdjpgcom
%{_bindir}/wrjpgcom
%{_mandir}/man1/cjpeg.1*
%{_mandir}/man1/djpeg.1*
%{_mandir}/man1/jpegtran.1*
%{_mandir}/man1/rdjpgcom.1*
%{_mandir}/man1/wrjpgcom.1*

%files -n turbojpeg
%license LICENSE.md
%doc README.md README.ijg ChangeLog.md
%{_libdir}/libturbojpeg.so.0*

%files -n turbojpeg-devel
%{_includedir}/turbojpeg.h
%{_libdir}/libturbojpeg.so
%{_libdir}/pkgconfig/libturbojpeg.pc

%changelog
%{?autochangelog}
