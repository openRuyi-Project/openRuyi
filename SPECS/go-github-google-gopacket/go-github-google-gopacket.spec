# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Kimmy <yucheng.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           gopacket
%define go_import_path  github.com/google/gopacket
# Skip optional native capture backends and examples that require unpackaged
# local libraries; nexttrace only needs the pure-Go core. libpcap fails with
# "fatal error: pcap.h: No such file or directory", while PF_RING fails with
# "fatal error: pfring.h: No such file or directory" and is not in the repo.
# Keep pcapgo testable by spelling out pcap and its children instead of pcap*.
%define go_test_exclude_glob %{shrink:
    %{go_import_path}/pcap
    %{go_import_path}/pcap/*
    %{go_import_path}/pfring
    %{go_import_path}/examples/*
}

Name:           go-github-google-gopacket
Version:        1.1.19
Release:        %autorelease
Summary:        Packet decoding library for Go
License:        BSD-3-Clause
URL:            https://github.com/google/gopacket
VCS:            git:https://github.com/google/gopacket
#!RemoteAsset:  sha256:31efa87cc9d2b41e5e66c7daa8839d841d2a43cc477bf595c9e8c24ef6903830
Source0:        https://github.com/google/gopacket/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

# Fix Go 1.26 vet errors: %q is invalid for uint16 DNS priority and weight.
Patch2000:      2000-fix-dns-test-format-for-go1.26.patch

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(golang.org/x/net)
BuildRequires:  go(golang.org/x/sys)

Provides:       go(github.com/google/gopacket) = %{version}

Requires:       go(golang.org/x/net)
Requires:       go(golang.org/x/sys)

%description
Gopacket provides packet decoding for Go. It includes support for many network
protocols and packet capture formats, along with packet filtering and assembly
utilities.

%prep -a
# These source-only generator files are not installed as executable commands.
chmod a-x layers/test_creator.py pcapgo/write.go

%files
%doc AUTHORS CONTRIBUTING.md README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
