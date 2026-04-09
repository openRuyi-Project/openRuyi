# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Jingwiw <wangjingwei@iscas.ac.cn>
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           libcgroup
Version:        3.2.0
Release:        %autorelease
Summary:        Library and tools for cgroup inspection and management
License:        LGPL-2.0-or-later
URL:            https://github.com/libcgroup/libcgroup
#!RemoteAsset
Source0:        https://github.com/libcgroup/libcgroup/archive/refs/tags/v%{version}.tar.gz
BuildSystem:    autotools

BuildOption(conf):  --disable-daemon
BuildOption(conf):  --enable-opaque-hierarchy="name=systemd"
BuildOption(conf):  --disable-static
BuildOption(conf):  --enable-pam-module-dir=%{_libdir}/security

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  gcc-c++
BuildRequires:  bison
BuildRequires:  flex
BuildRequires:  pkgconfig(pam)
BuildRequires:  pkgconfig(libsystemd)

%description
The libcgroup library and associated tools for interacting with Linux
Control Groups. On openRuyi, these are primarily for inspection and
compatibility, as system-wide resource management is handled by systemd.

%package        tools
Summary:        Command-line tools for inspecting control groups
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    tools
Contains tools like lscgroup, cgget, and cgexec for scripting and
manual interaction with the cgroup filesystem.

%package        pam
Summary:        PAM module for classifying user sessions into cgroups
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    pam
The pam_cgroup PAM module, used to place user login sessions into
pre-configured control groups.

%package        devel
Summary:        Development files for the libcgroup library
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
Header files and libraries for developing applications that use libcgroup.

%conf -p
autoreconf -fiv

%install -a
# Clean up artifacts related to the disabled legacy daemons.
rm -rf %{buildroot}%{_sysconfdir}/cgconfig.conf
rm -rf %{buildroot}%{_sysconfdir}/cgrules.conf
rm -rf %{buildroot}%{_sysconfdir}/cgsnapshot_blacklist.conf
rm -rf %{buildroot}%{_unitdir}/cgconfig.service
rm -rf %{buildroot}%{_unitdir}/cgrules.service

%files
%license COPYING
%{_libdir}/libcgroup.so.*

%files tools
%license COPYING
%doc README README_systemd
%{_bindir}/*
%{_sbindir}/*
%{_mandir}/man*/*

%files pam
%license COPYING
%{_libdir}/security/pam_cgroup.so

%files devel
%license COPYING
%{_includedir}/libcgroup.h
%{_includedir}/libcgroup/*.h
%{_libdir}/libcgroup.so
%{_libdir}/pkgconfig/libcgroup.pc

%changelog
%autochangelog
