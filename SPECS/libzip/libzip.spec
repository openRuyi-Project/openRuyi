# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           libzip
Version:        1.11.4
Release:        %autorelease
Summary:        A C library for reading, creating, and modifying zip archives
License:        BSD-3-Clause
URL:            https://libzip.org/
VCS:            git:https://github.com/nih-at/libzip
#!RemoteAsset:  sha256:8a247f57d1e3e6f6d11413b12a6f28a9d388de110adc0ec608d893180ed7097b
Source:         https://github.com/nih-at/libzip/releases/download/v%{version}/libzip-%{version}.tar.xz
BuildSystem:    cmake

BuildOption(conf):  -DDOCUMENTATION_FORMAT:STRING=man
BuildOption(conf):  -DBUILD_TOOLS:BOOL=ON
BuildOption(conf):  -DBUILD_REGRESS:BOOL=OFF
BuildOption(conf):  -DBUILD_EXAMPLES:BOOL=OFF

BuildRequires:  cmake >= 3.0.2
BuildRequires:  groff
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(bzip2)
BuildRequires:  pkgconfig(gnutls)
BuildRequires:  pkgconfig(liblzma) >= 5.2
BuildRequires:  pkgconfig(libzstd)
BuildRequires:  pkgconfig(nettle) >= 3.0
BuildRequires:  pkgconfig(zlib) >= 1.1.2

%description
libzip is a C library for reading, creating, and modifying zip archives.
This package contains the runtime library and command-line tools.

%package        devel
Summary:        Development files for libzip
Requires:       glibc-devel
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
This package contains the header files, pkg-config files, and other
files needed to develop applications that use the libzip library.

%files
%license LICENSE
%doc AUTHORS NEWS.md THANKS
# Files from original 'tools' package
%{_bindir}/zipcmp
%{_bindir}/zipmerge
%{_bindir}/ziptool
%{_mandir}/man1/zipcmp.1*
%{_mandir}/man1/zipmerge.1*
%{_mandir}/man1/ziptool.1*
%{_mandir}/man5/zip*.5*
%{_libdir}/libzip.so.5*

%files devel
%{_libdir}/libzip.so
%{_includedir}/zip.h
%{_includedir}/zipconf.h
%{_libdir}/pkgconfig/libzip.pc
%dir %{_libdir}/cmake
%{_libdir}/cmake/libzip/
%{_mandir}/man3/*.3*

%changelog
%autochangelog
