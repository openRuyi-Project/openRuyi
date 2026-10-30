# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           udpcast
Version:        20250223
Release:        %autorelease
Summary:        UDP broadcast file distribution and installation tool
License:        GPL-2.0-only AND BSD-2-Clause
URL:            https://udpcast.linux.lu/
# VCS: No VCS link available
#!RemoteAsset:  sha256:cefd7554c877e1bc76987d2b96b23f7699a2e5340c254454f61b6e0dae370aa7
Source:         https://udpcast.linux.lu/download/%{name}-%{version}.tar.gz
BuildSystem:    autotools

BuildRequires:  m4
BuildRequires:  make
BuildRequires:  perl

%description
Udpcast is a tool that sends data over a local network to several hosts
at once, using multicast or broadcast. It is used by Clonezilla and DRBL
to clone many machines in parallel. The package contains the udp-sender
and udp-receiver utilities.

%package        devel
Summary:        Development files for udpcast
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The udpcast-devel package contains the header file needed to build
udpcast rate governor modules.

%check
#no check

%files
%doc Changelog.txt cmd.html
%license COPYING
%{_sbindir}/udp-receiver
%{_sbindir}/udp-sender
%{_mandir}/man1/udp-receiver.1*
%{_mandir}/man1/udp-sender.1*

%files devel
%{_includedir}/udpcast/rateGovernor.h

%changelog
%autochangelog
