# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           liborcus
Version:        0.21.0
Release:        %autorelease
Summary:        Spreadsheet file import filters
License:        MPL-2.0
URL:            https://gitlab.com/orcus/orcus
#!RemoteAsset:  sha256:1c6e473d6b8a63d61d0e6874a1762d6f0e0e78338d763e48ac93126ecde19b37
Source0:        https://gitlab.com/api/v4/projects/orcus%2Forcus/packages/generic/source/%{version}/%{name}-%{version}.tar.xz
BuildSystem:    autotools

BuildOption(conf):  --disable-static
BuildOption(conf):  CXXFLAGS="%{optflags} -std=gnu++17"
BuildOption(conf):  --disable-spreadsheet-model
BuildOption(conf):  --without-tools
BuildOption(conf):  --without-benchmark
BuildOption(conf):  --without-doc-example
BuildOption(conf):  --disable-python

BuildRequires:  boost-devel
BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  pkgconfig(mdds-3.0) >= 3.0.0
BuildRequires:  pkgconfig(zlib)

%description
Orcus reads spreadsheet files and emits their contents through a C++
import interface. It includes filters for ODS, XLSX, Excel XML and
Gnumeric documents and parsers for structured text.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
Headers, linker files and pkg-config metadata for developing with %{name}.

%files
%doc AUTHORS README.md
%license LICENSE
%{_libdir}/liborcus*-0.21.so.*

%files devel
%{_includedir}/liborcus-0.21/
%{_libdir}/liborcus*-0.21.so
%{_libdir}/pkgconfig/liborcus-0.21.pc

%changelog
%autochangelog
