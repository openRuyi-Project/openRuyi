# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           dnscrypt
%define go_import_path  github.com/ameshkov/dnscrypt/v2

Name:           go-github-ameshkov-dnscrypt-v2
Version:        2.4.0
Release:        %autorelease
Summary:        Includes everything you need to work with DNSCrypt
License:        Unlicense
URL:            https://github.com/ameshkov/dnscrypt
#!RemoteAsset:  sha256:a3b01bd53a169369a3c96f7aa60516fbb843af0f58cd2b866c38b52a4e4344c1
Source0:        https://github.com/ameshkov/dnscrypt/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n %{_name}-%{version}
# Skip tests that dial live public DNSCrypt resolvers, which fails in the offline build chroot.
BuildOption(check):  -skip '^(TestTimeoutOnDialError|TestTimeoutOnDialExchange|TestFetchCertPublicResolvers|TestExchangePublicResolvers)$'

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/AdguardTeam/golibs)
BuildRequires:  go(github.com/ameshkov/dnsstamps)
BuildRequires:  go(github.com/jessevdk/go-flags)
BuildRequires:  go(github.com/miekg/dns)
BuildRequires:  go(github.com/stretchr/testify)
BuildRequires:  go(golang.org/x/crypto)
BuildRequires:  go(golang.org/x/net)
BuildRequires:  go(gopkg.in/yaml.v3)

Provides:       go(github.com/ameshkov/dnscrypt/v2) = %{version}

Requires:       go(github.com/AdguardTeam/golibs)
Requires:       go(github.com/ameshkov/dnsstamps)
Requires:       go(github.com/jessevdk/go-flags)
Requires:       go(github.com/miekg/dns)
Requires:       go(golang.org/x/crypto)
Requires:       go(golang.org/x/net)
Requires:       go(gopkg.in/yaml.v3)

%description
Golang implementation of the DNSCrypt v2 protocol for running resolvers and making DNS lookups.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
