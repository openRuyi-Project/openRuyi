# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           libqxp
Version:        0.0.3
Release:        %autorelease
Summary:        QuarkXPress document import library
License:        MPL-2.0
URL:            https://wiki.documentfoundation.org/DLP/Libraries/libqxp
VCS:            git:https://git.libreoffice.org/libqxp
#!RemoteAsset:  sha256:4687a9cc96c32d7406e5072c4da150fca696c563e5cde62b024f82fa53d32332
Source0:        https://dev-www.libreoffice.org/src/%{name}/%{name}-%{version}.tar.xz
BuildSystem:    autotools

BuildOption(conf):  --disable-static
BuildOption(conf):  CXXFLAGS="%{optflags} -std=gnu++17"
BuildOption(conf):  --without-docs
BuildOption(conf):  --enable-tests
BuildOption(conf):  --enable-tools

BuildRequires:  boost-devel
BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  pkgconfig(librevenge-0.0)
BuildRequires:  pkgconfig(icu-uc)
BuildRequires:  pkgconfig(cppunit)
BuildRequires:  pkgconfig(librevenge-generators-0.0)
BuildRequires:  pkgconfig(librevenge-stream-0.0)

%description
libqxp reads QuarkXPress publications. Its conversion utilities
write SVG, extract text and display raw document events.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
Headers, linker files and pkg-config metadata for developing with %{name}.

%files
%doc AUTHORS README
%license COPYING
%{_bindir}/qxp2raw
%{_bindir}/qxp2svg
%{_bindir}/qxp2text
%{_libdir}/libqxp-0.0.so.*

%files devel
%{_includedir}/libqxp-0.0/
%{_libdir}/libqxp-0.0.so
%{_libdir}/pkgconfig/libqxp-0.0.pc

%changelog
%autochangelog
