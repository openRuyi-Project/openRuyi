# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           q
%define go_import_path  github.com/natesales/q
# Skip root and transport test suites because they issue live queries to public DNS resolvers unavailable in the offline buildroot.
%define go_test_exclude %{shrink:
    %{go_import_path}
    %{go_import_path}/transport
}

Name:           go-github-natesales-q
Version:        0.19.12
Release:        %autorelease
Summary:        Tiny and feature-rich DNS client library and CLI
License:        GPL-3.0-only
URL:            https://github.com/natesales/q
#!RemoteAsset:  sha256:1f56ebfb93fd380dee734cca9227149de2491c49db7b2c0f21019fd463081e4c
Source0:        https://github.com/natesales/q/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n %{_name}-%{version}

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/ameshkov/dnscrypt/v2)
BuildRequires:  go(github.com/charmbracelet/log)
BuildRequires:  go(github.com/jedisct1/go-dnsstamps)
BuildRequires:  go(github.com/jessevdk/go-flags)
BuildRequires:  go(github.com/json-iterator/go)
BuildRequires:  go(github.com/miekg/dns)
BuildRequires:  go(github.com/natesales/bgptools-go)
BuildRequires:  go(github.com/quic-go/quic-go)
BuildRequires:  go(github.com/sthorne/odoh-go)
BuildRequires:  go(github.com/stretchr/testify)
BuildRequires:  go(golang.org/x/net)
BuildRequires:  go(gopkg.in/yaml.v3)

Provides:       go(github.com/natesales/q) = %{version}

Requires:       go(github.com/ameshkov/dnscrypt/v2)
Requires:       go(github.com/charmbracelet/log)
Requires:       go(github.com/jedisct1/go-dnsstamps)
Requires:       go(github.com/jessevdk/go-flags)
Requires:       go(github.com/json-iterator/go)
Requires:       go(github.com/miekg/dns)
Requires:       go(github.com/natesales/bgptools-go)
Requires:       go(github.com/quic-go/quic-go)
Requires:       go(github.com/sthorne/odoh-go)
Requires:       go(golang.org/x/net)
Requires:       go(gopkg.in/yaml.v3)

%description
Tiny and feature-rich DNS client library and CLI supporting UDP, TCP, DoT, DoH, DoQ, and ODoH.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
