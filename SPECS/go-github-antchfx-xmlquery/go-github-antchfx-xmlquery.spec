# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           xmlquery
%define go_import_path  github.com/antchfx/xmlquery

Name:           go-github-antchfx-xmlquery
Version:        1.5.1
Release:        %autorelease
Summary:        XPath queries for XML documents in Go
License:        MIT
URL:            https://github.com/antchfx/xmlquery
#!RemoteAsset:  sha256:15da176f8fee10736e3e57efb9699bfbdccd6d84ed0cae512123bc772d8560ba
Source0:        https://github.com/antchfx/xmlquery/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/antchfx/xpath)
BuildRequires:  go(github.com/golang/groupcache)
BuildRequires:  go(golang.org/x/net)

Provides:       go(%{go_import_path}) = %{version}

Requires:       go(github.com/antchfx/xpath)
Requires:       go(github.com/golang/groupcache)
Requires:       go(golang.org/x/net)

%description
This package parses XML documents and evaluates XPath expressions, with
support for streaming parsing and compiled-query caching.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
