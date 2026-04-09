# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           libqalculate
Version:        5.9.0
Release:        %autorelease
Summary:        Multi-purpose calculator library
License:        GPL-2.0-or-later
URL:            https://github.com/Qalculate/libqalculate
#!RemoteAsset:  sha256:63bcd5a4a32bc7811d0c60865fa35caa2e32aa0a09493b3760d913013bcd2be6
Source0:        https://github.com/Qalculate/libqalculate/archive/refs/tags/v%{version}.tar.gz
BuildSystem:    autotools

BuildOption(conf):  --disable-static

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  intltool
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(readline)
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  pkgconfig(icu-i18n)
BuildRequires:  pkgconfig(mpfr)
BuildRequires:  perl(XML::Parser)

%description
This library underpins the Qalculate! multi-purpose desktop calculator.

%package        devel
Summary:        Development tools for the Qalculate calculator library
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       pkgconfig(libxml-2.0)
Requires:       pkgconfig(mpfr)

%description    devel
The libqalculate-devel package contains the header files needed for development
with libqalculate.

%conf -p
autoreconf -fiv

%install -a
%find_lang %{name} --generate-subpackages

%files -f %{name}.lang
%doc AUTHORS ChangeLog TODO
%license COPYING
%{_bindir}/qalc
%{_libdir}/libqalculate.so.*
%{_datadir}/qalculate/
%{_mandir}/man1/qalc.1*

%files devel
%{_libdir}/libqalculate.so
%{_libdir}/pkgconfig/libqalculate.pc
%{_includedir}/libqalculate/

%changelog
%autochangelog
