# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <1772413353@qq.com>
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
Patch0:        0001-Revert-build-fix-rpath-issue.patch
BuildSystem:   meson

BuildOption(conf): -Dtools=true
BuildOption(conf): -Dpython=true

BuildRequires:  gcc
BuildRequires:  meson
BuildRequires:  python3-devel

%description
The Low Complexity Communication Codec (LC3) is an audio codec used by
Bluetooth LE Audio. It enables high quality audio over low bandwidth
connections. This package contains the shared library.

%package        devel
Summary:        Development files for liblc3
Requires:       %{name}%{?_isa} = %{version}

%description    devel
This package contains libraries and header files for developing applications
that use the LC3 codec library.

%package     -n python3-lc3
Summary:        Python 3 bindings for liblc3
Requires:       %{name}%{?_isa} = %{version}

%description -n python3-lc3
This package contains Python 3 bindings for the LC3 codec library.

%files
%license LICENSE
%{_libdir}/liblc3.so.1*
%{_bindir}/dlc3
%{_bindir}/elc3

%files devel
%{_includedir}/lc3*
%{_libdir}/pkgconfig/lc3.pc
%{_libdir}/liblc3.so

%files -n python3-lc3
%pycached %{python3_sitelib}/lc3.py

%changelog
%{?autochangelog}
