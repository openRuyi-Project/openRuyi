# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
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

BuildOption(conf):  --disable-silent-rules
BuildOption(conf):  --disable-static

BuildRequires:  nasm
BuildRequires:  libtool
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(fontconfig)
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(fribidi)
BuildRequires:  pkgconfig(harfbuzz)
BuildRequires:  pkgconfig(libunibreak)

%description
libass is a subtitle renderer for the ASS/SSA (Advanced Substation Alpha)
subtitle format. This is a metapackage that requires the runtime library.

%package        devel
Summary:        Development files for libass, a subtitle rendering library
Requires:       glibc-devel
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       pkgconfig(fontconfig)
Requires:       pkgconfig(freetype2)
Requires:       pkgconfig(fribidi)
Requires:       pkgconfig(harfbuzz)
Requires:       pkgconfig(libunibreak)

%description    devel
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
%autochangelog
