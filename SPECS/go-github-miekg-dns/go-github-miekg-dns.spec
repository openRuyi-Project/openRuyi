# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Julian Zhu <julian.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           dns
%define go_import_path  github.com/miekg/dns

Name:           go-github-miekg-dns
Version:        1.1.72
Release:        %autorelease
Summary:        DNS library in Go
License:        BSD-3-Clause
URL:            https://github.com/miekg/dns
#!RemoteAsset
Source0:        https://github.com/miekg/dns/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(golang.org/x/net)
BuildRequires:  go(golang.org/x/sys)
BuildRequires:  go(golang.org/x/sync)
BuildRequires:  go(golang.org/x/tools)

Provides:       go(github.com/miekg/dns) = %{version}

%description
Alternative (more granular) approach to a DNS library
Less is more.

Complete and usable DNS library. All Resource Records are supported, including the DNSSEC types. It follows a lean and mean philosophy. If there is stuff you should know as a DNS programmer there isn't a convenience function for it. Server side and client side programming is supported, i.e. you can build servers and resolvers with it.

We try to keep the "master" branch as sane as possible and at the bleeding edge of standards, avoiding breaking changes wherever reasonable. We support the last two versions of Go.

%files
%license LICENSE*
%doc README*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
