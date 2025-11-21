# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <1772413353@qq.com>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           dav1d
Version:        1.5.2
Release:        %autorelease
Summary:        A fast and small AV1 decoder
License:        BSD-2-Clause
URL:            https://code.videolan.org/videolan/dav1d
#!RemoteAsset
Source:         https://github.com/videolan/dav1d/archive/refs/tags/%{version}.tar.gz
BuildSystem:    meson

BuildRequires:  meson >= 0.49.0
%ifarch x86_64
BuildRequires:  nasm >= 2.14
%endif
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(libxxhash)

%description
dav1d is a cross-platform, high-performance AV1 decoder focused on speed
and correctness.

%package        devel
Summary:        Development files for dav1d
Requires:       %{name}%{?_isa} = %{version}

%description    devel
This package contains the header files and libraries needed to develop
applications that use the dav1d AV1 decoder library.

%ldconfig_scriptlets

%files
%license COPYING
%doc CONTRIBUTING.md doc/PATENTS NEWS README.md THANKS.md
%{_bindir}/dav1d
%{_libdir}/libdav1d.so.7*

%files devel
%{_includedir}/dav1d
%{_libdir}/libdav1d.so
%{_libdir}/pkgconfig/dav1d.pc

%changelog
%{?autochangelog}
