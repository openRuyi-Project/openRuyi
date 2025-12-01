# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <1772413353@qq.com>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           libotf
Version:        0.9.16
Release:        %autorelease
Summary:        A Library for handling OpenType Font
License:        LGPL-2.1-or-later
URL:            http://www.nongnu.org/m17n/
#!RemoteAsset
Source:         http://download.savannah.gnu.org/releases/m17n/libotf-%{version}.tar.gz
BuildSystem:    autotools

BuildOption(conf): --disable-static

BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  freetype-devel

Requires:       freetype

%description
The library "libotf" provides facilities to read Open Type Layout Tables
from OTF files and convert Unicode character sequences to glyph code
sequences.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       pkgconfig

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%install -a
rm -f %{buildroot}%{_bindir}/libotf-config

%files
%doc AUTHORS COPYING README NEWS
%{_libdir}/libotf.so.1*
%{_bindir}/otfdump
%{_bindir}/otflist
%{_bindir}/otftobdf

%files devel
%doc example
%{_includedir}/*
%{_libdir}/libotf.so
%{_libdir}/pkgconfig/libotf.pc

%changelog
%{?autochangelog}
