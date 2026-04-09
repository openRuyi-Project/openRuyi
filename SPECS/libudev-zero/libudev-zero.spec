# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: avrovadonz2026 <jinyuan.or@isrc.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

# Keep pkg-config metadata from participating in solver choice for pkgconfig(libudev).
%global __provides_exclude_from ^%{_libdir}/pkgconfig/libudev\\.pc$
%global __requires_exclude_from ^%{_libdir}/pkgconfig/libudev\\.pc$

Name:           libudev-zero
Version:        1.0.3
Release:        %autorelease
Summary:        Drop-in replacement for libudev
License:        ISC
URL:            https://github.com/illiliti/libudev-zero
#!RemoteAsset
Source0:        %{url}/archive/refs/tags/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildSystem:    autotools

BuildOption(build):  PREFIX=%{_prefix}
BuildOption(build):  LIBDIR=%{_libdir}
BuildOption(build):  INCLUDEDIR=%{_includedir}
BuildOption(build):  CC="%{__cc}"
BuildOption(build):  CFLAGS="%{build_cflags}"
BuildOption(build):  LDFLAGS="%{build_ldflags}"
BuildOption(install):  PREFIX=%{_prefix}
BuildOption(install):  LIBDIR=%{_libdir}
BuildOption(install):  INCLUDEDIR=%{_includedir}
BuildOption(install):  PKGCONFIGDIR=%{_libdir}/pkgconfig

BuildRequires:  gcc
BuildRequires:  make

# Conflicting libudev.so.1
Conflicts:      systemd-udev

# Pretend to provide any libudev.so(*)() that systemd-udev provides
BuildRequires:  systemd-udev
Provides:       %(rpm -q systemd-udev --provides | grep '^libudev\.so' | tr '\n' ' ')

%description
%{name} is a drop-in replacement for libudev intended to work with
different Linux device managers.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Conflicts:      pkgconfig(libudev)

%description    devel
This package contains header files and the pkg-config metadata for %{name}.

# libudev-zero does not use a configure script.
%conf

%check
# Upstream Makefile has no test suite and no 'check' target.
:

%install -a
# Do not ship static library in this package set.
rm -f %{buildroot}%{_libdir}/libudev.a

%files
%license LICENSE
%doc README.md
%{_libdir}/libudev.so.1

%files devel
%{_includedir}/libudev.h
%{_libdir}/libudev.so
%{_libdir}/pkgconfig/libudev.pc

%changelog
%autochangelog
