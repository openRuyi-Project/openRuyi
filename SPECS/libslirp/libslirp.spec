# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Yafen Fang <yafen@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           libslirp
Version:        4.9.1
Release:        %autorelease
Summary:        A general purpose TCP-IP emulator
License:        BSD-3-Clause AND MIT
URL:            https://gitlab.freedesktop.org/slirp/libslirp
#!RemoteAsset:  sha256:3970542143b7c11e6a09a4d2b50f30a133473c41f15ed0bdcc3b7a1c450d9a5c
Source:         https://gitlab.freedesktop.org/slirp/libslirp/-/archive/v%{version}/libslirp-v%{version}.tar.gz
BuildSystem:    meson

BuildRequires:  git-core
BuildRequires:  meson
BuildRequires:  pkgconfig(glib-2.0)

%description
A general purpose TCP-IP emulator used by virtual machine hypervisors
to provide virtual networking services.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%files
%doc README.md CHANGELOG.md
%license COPYRIGHT
%{_libdir}/libslirp.so.0*

%files devel
%dir %{_includedir}/slirp/
%{_includedir}/slirp/*
%{_libdir}/libslirp.so
%{_libdir}/pkgconfig/slirp.pc

%changelog
%autochangelog
