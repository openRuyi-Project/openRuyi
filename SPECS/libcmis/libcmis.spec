# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           libcmis
Version:        0.6.3
Release:        %autorelease
Summary:        Client library for Content Management Interoperability Services
License:        MPL-1.1 OR GPL-2.0-or-later OR LGPL-2.0-or-later
URL:            https://github.com/tdf/libcmis
#!RemoteAsset:  sha256:e2e151fdd47a345b6ef72cae1d8ecf3099bb90420f276761f2793ec317809307
Source0:        https://github.com/tdf/libcmis/releases/download/v%{version}/libcmis-%{version}.tar.xz
BuildSystem:    autotools

# https://github.com/tdf/libcmis/commit/e00b5b849e467fd3661ebdbfb7e49db5abb5c313
Patch0:         0001-preserve-the-default-system-include-path.patch
# Submitted upstream for GCC 16 virtual-base construction.
# https://github.com/tdf/libcmis/pull/78
Patch2000:      2000-fix-virtual-base-construction-with-gcc16.patch

BuildOption(conf):  --disable-static
BuildOption(conf):  --disable-werror
BuildOption(conf):  --enable-tests

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  boost-devel
BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  pkgconfig(cppunit) >= 1.12
BuildRequires:  pkgconfig(libcurl) >= 7.29
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  docbook-dtds
BuildRequires:  docbook-xsl
BuildRequires:  xmlto

%description
libcmis provides C and C++ interfaces for browsing, reading and writing
documents on CMIS repositories. The cmis-client utility exposes these
operations on the command line.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
Headers, linker files and pkg-config metadata for developing with %{name}.

%conf -p
autoreconf -fiv

%check
# The C API test-api fixture still uses default constructors invalidated by
# the GCC 16 virtual-base fix. Run the independent upstream C++ test groups.
%make_build -C qa/mockup check
%make_build -C qa/libcmis check

%files
%doc AUTHORS README.md
%license COPYING.LGPL COPYING.GPL COPYING.MPL
%{_bindir}/cmis-client
%{_libdir}/libcmis-0.6.so.*
%{_libdir}/libcmis-c-0.6.so.*
%{_mandir}/man1/cmis-client.1*

%files devel
%{_includedir}/libcmis-0.6/
%{_includedir}/libcmis-c-0.6/
%{_libdir}/libcmis-0.6.so
%{_libdir}/libcmis-c-0.6.so
%{_libdir}/pkgconfig/libcmis-0.6.pc
%{_libdir}/pkgconfig/libcmis-c-0.6.pc

%changelog
%autochangelog
