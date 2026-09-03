# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           pcap
%define go_import_path  github.com/miekg/pcap
# Live packet capture tests require CAP_NET_RAW on the OBS worker.
%define go_test_exclude %{go_import_path}

Name:           go-github-miekg-pcap
Version:        1.0.1
Release:        %autorelease
Summary:        Packet capture file reader for Go
License:        BSD-3-Clause
URL:            https://github.com/miekg/pcap
#!RemoteAsset:  sha256:ff45a96b94d18d0f0646645adc4dcb351b3e5e90304f3e605774e96740bda193
Source0:        https://github.com/miekg/pcap/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  pkgconfig(libpcap)

Provides:       go(%{go_import_path}) = %{version}

Requires:       pkgconfig(libpcap)

%description
Pcap is a native Go reader for packet capture files and includes tools for
filtering and inspecting captured packets.

%check -a
# Compile the package without running tests that require CAP_NET_RAW.
go test -c -o /dev/null %{go_import_path}

%files
%doc README.mkd
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
