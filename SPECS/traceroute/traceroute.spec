# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Yafen Fang <yafen@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           traceroute
Version:        2.1.6
Release:        %autorelease
Summary:        A new modern implementation of traceroute(8) utility for Linux systems
License:        GPL-2.0-or-later
URL:            https://traceroute.sourceforge.net/
# VCS: No VCS link available
#!RemoteAsset
Source0:        https://sourceforge.net/projects/traceroute/files/traceroute/%{name}-%{version}/%{name}-%{version}.tar.gz
BuildSystem:    autotools

# Enable building with Clang by honoring external CC assignment instead of hardcoding gcc
Patch0:         0001-support-clang-build.patch
# Replace getenv() with secure_getenv() for secure environment variable access
Patch1:         0002-traceroute-secure_getenv.patch

BuildOption(build):  CFLAGS="%{build_cflags}"
BuildOption(build):  LDFLAGS="%{build_ldflags}"
BuildOption(install):  prefix=%{_prefix}

BuildRequires:  gcc
BuildRequires:  make

Provides:       tcptraceroute = %{version}-%{release}

%description
Traceroute tracks the route packets taken from an IP network on their way to a given host.
It utilizes the IP protocol's time to live (TTL) field and attempts to elicit an ICMP TIME_EXCEEDED
response from each gateway along the path to the host.

# No configure
%conf

%install -a
ln -s traceroute %{buildroot}%{_bindir}/traceroute6
install -D -p -m755 wrappers/tcptraceroute %{buildroot}%{_bindir}/tcptraceroute
install -D -p -m644 traceroute/traceroute.8 %{buildroot}%{_mandir}/man8/traceroute.8
ln -s traceroute.8 %{buildroot}%{_mandir}/man8/traceroute6.8
ln -s traceroute.8 %{buildroot}%{_mandir}/man8/tcptraceroute.8

# No check
%check

%files
%license COPYING
%doc README TODO CREDITS
%{_bindir}/*
%{_mandir}/*/*

%changelog
%autochangelog
