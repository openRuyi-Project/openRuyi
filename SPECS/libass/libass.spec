# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <1772413353@qq.com>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           libass
Version:        0.17.4
Release:        %autorelease
Summary:        Library for SSA/ASS-formatted subtitle rendering
License:        ISC
URL:            https://github.com/libass/libass
#!RemoteAsset
Source:         https://github.com/libass/libass/archive/refs/tags/%{version}.tar.gz
BuildSystem:    autotools

BuildOption(conf): --disable-silent-rules
BuildOption(conf): --disable-static

BuildRequires:  nasm libtool autoconf automake
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(fontconfig) >= 2.10.92
BuildRequires:  pkgconfig(freetype2) >= 9.10.3
BuildRequires:  pkgconfig(fribidi) >= 0.19.0
BuildRequires:  pkgconfig(harfbuzz) >= 1.2.3
BuildRequires:  pkgconfig(libunibreak)

%description
libass is a subtitle renderer for the ASS/SSA (Advanced Substation Alpha)
subtitle format. This is a metapackage that requires the runtime library.

%package        devel
Summary:        Development files for libass, a subtitle rendering library
Requires:       glibc-devel
Requires:       %{name}%{?_isa} = %{version}
Requires:       pkgconfig(fontconfig) >= 2.10.92
Requires:       pkgconfig(freetype2) >= 9.10.3
Requires:       pkgconfig(fribidi) >= 0.19.0
Requires:       pkgconfig(harfbuzz) >= 1.2.3
Requires:       pkgconfig(libunibreak) >= 1.1

%description devel
This package contains the header files and libraries needed to develop
applications that use the libass library.

%conf -p
./autogen.sh

%files
%license COPYING
%{_libdir}/libass.so.9*

%files devel
%{_includedir}/ass
%{_libdir}/libass.so
%{_libdir}/pkgconfig/libass.pc

%changelog
%{?autochangelog}
