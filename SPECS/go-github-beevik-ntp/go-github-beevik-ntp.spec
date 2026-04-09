# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Julian Zhu <julian.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           ntp
%define go_import_path  github.com/beevik/ntp
# Tests need network
%define go_test_ignore_failure 1

Name:           go-github-beevik-ntp
Version:        1.5.0
Release:        %autorelease
Summary:        a simple ntp client package for go
License:        BSD-2-Clause
URL:            https://github.com/beevik/ntp
#!RemoteAsset
Source0:        https://github.com/beevik/ntp/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/stretchr/testify)
BuildRequires:  go(golang.org/x/net)

Provides:       go(github.com/beevik/ntp) = %{version}

Requires:       go(github.com/stretchr/testify)
Requires:       go(golang.org/x/net)

%description
The ntp package is an implementation of a Simple NTP (SNTP) client based
on RFC 5905 (https://tools.ietf.org/html/rfc5905). It allows you to
connect to a remote NTP server and request information about the current
time.

%files
%license LICENSE*
%doc README*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
