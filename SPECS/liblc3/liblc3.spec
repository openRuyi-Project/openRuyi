# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:          liblc3
Version:       1.1.3
Release:       %autorelease
Summary:       Low Complexity Communication Codec (LC3) Library
License:       Apache-2.0
URL:           https://github.com/google/liblc3
#!RemoteAsset
Source:        https://github.com/google/liblc3/archive/refs/tags/v%{version}.tar.gz
BuildSystem:   meson

Patch0:        0001-Revert-build-fix-rpath-issue.patch

BuildOption(conf):  -Dtools=true
BuildOption(conf):  -Dpython=true

BuildRequires:  gcc
BuildRequires:  meson
BuildRequires:  pkgconfig(python3)

%description
The Low Complexity Communication Codec (LC3) is an audio codec used by
Bluetooth LE Audio. It enables high quality audio over low bandwidth
connections. This package contains the shared library.

%package        devel
Summary:        Development files for liblc3
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
This package contains libraries and header files for developing applications
that use the LC3 codec library.

%package     -n python-lc3
Summary:        Python bindings for liblc3
Provides:       python3-lc3 = %{version}-%{release}
%python_provide python3-lc3
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description -n python-lc3
This package contains Python bindings for the LC3 codec library.

%files
%license LICENSE
%{_libdir}/liblc3.so.1*
%{_bindir}/dlc3
%{_bindir}/elc3

%files devel
%{_includedir}/lc3*
%{_libdir}/pkgconfig/lc3.pc
%{_libdir}/liblc3.so

%files -n python-lc3
%pycached %{python3_sitelib}/lc3.py

%changelog
%autochangelog
