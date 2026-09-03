# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           bluemonday
%define go_import_path  github.com/microcosm-cc/bluemonday

Name:           go-github-microcosm-cc-bluemonday
Version:        1.0.27
Release:        %autorelease
Summary:        HTML sanitizer for Go
License:        BSD-3-Clause
URL:            https://github.com/microcosm-cc/bluemonday
#!RemoteAsset:  sha256:02f57c2cc795a7ec9d74354d182fcff5cc69734c7a46f82b33b656f8bdb19703
Source0:        https://github.com/microcosm-cc/bluemonday/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/aymerick/douceur)
BuildRequires:  go(github.com/gorilla/css)
BuildRequires:  go(golang.org/x/net)

Provides:       go(github.com/microcosm-cc/bluemonday) = %{version}

Requires:       go(github.com/aymerick/douceur)
Requires:       go(github.com/gorilla/css)
Requires:       go(golang.org/x/net)

%description
bluemonday sanitizes untrusted HTML using configurable allowlists inspired by
the OWASP Java HTML Sanitizer.

%files
%doc README*
%license LICENSE*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
