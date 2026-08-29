# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Suyun <ziyu.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           opencc
Version:        1.2.0
Release:        %autorelease
Summary:        Libraries for Simplified-Traditional Chinese Conversion
License:        Apache-2.0
URL:            https://github.com/BYVoid/OpenCC
#!RemoteAsset:  sha256:f4f86eb25e239450d075081e08594801aa063c298d21d9f6c6aa85cd55241962
Source0:        https://github.com/BYVoid/OpenCC/archive/refs/tags/ver.%{version}.tar.gz
BuildSystem:    cmake

BuildOption(conf):  -DUSE_SYSTEM_MARISA=ON
BuildOption(conf):  -DUSE_SYSTEM_RAPIDJSON=ON

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  gettext
BuildRequires:  python3
BuildRequires:  pkgconfig(marisa)
BuildRequires:  pkgconfig(RapidJSON)

%description
OpenCC is a library for converting characters and phrases between
Traditional Chinese and Simplified Chinese.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%autosetup -n OpenCC-ver.%{version} -p1

%files
%license LICENSE
%{_bindir}/opencc*
%{_libdir}/libopencc.so.*
%{_datadir}/opencc/

%files devel
%{_includedir}/opencc/
%{_libdir}/libopencc.so
%{_libdir}/pkgconfig/opencc.pc
%{_libdir}/cmake/opencc/OpenCC*.cmake

%changelog
%autochangelog
