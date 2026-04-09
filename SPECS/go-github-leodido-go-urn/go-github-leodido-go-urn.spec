# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           go-urn
%define go_import_path  github.com/leodido/go-urn

Name:           go-github-leodido-go-urn
Version:        1.4.0
Release:        %autorelease
Summary:        Parser for uniform resource names as seen on RFC 8141, RFC 2141, and RFC 7643
License:        MIT
URL:            https://github.com/leodido/go-urn
#!RemoteAsset
Source0:        https://github.com/leodido/go-urn/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n %{_name}-%{version}

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/stretchr/testify)

Provides:       go(github.com/leodido/go-urn) = %{version}

Requires:       go(github.com/stretchr/testify)

%description
A parser for URNs. As seen on RFC 2141 (https://datatracker.ietf.org/doc/html/rfc2141),
RFC 7643 (https://datatracker.ietf.org/doc/html/rfc7643#section-10),
and on RFC 8141 (https://datatracker.ietf.org/doc/html/rfc8141).

%files
%license LICENSE*
%doc README*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
