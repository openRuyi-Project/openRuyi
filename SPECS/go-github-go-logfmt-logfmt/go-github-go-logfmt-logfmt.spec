# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Julian Zhu <julian.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           logfmt
%define go_import_path  github.com/go-logfmt/logfmt

Name:           go-github-go-logfmt-logfmt
Version:        0.6.1
Release:        %autorelease
Summary:        Package logfmt marshals and unmarshals logfmt messages.
License:        MIT
URL:            https://github.com/go-logfmt/logfmt
#!RemoteAsset
Source0:        https://github.com/go-logfmt/logfmt/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/google/go-cmp)

Provides:       go(github.com/go-logfmt/logfmt) = %{version}

Requires:       go(github.com/google/go-cmp)

%description
Package logfmt implements utilities to marshal and unmarshal data in the
logfmt format (https://brandur.org/logfmt). It provides an API similar
to encoding/json (https://pkg.go.dev/encoding/json) and encoding/xml
(https://pkg.go.dev/encoding/xml).

The logfmt format was first documented by Brandur Leach in this article
(https://brandur.org/logfmt). The format has not been formally
standardized. The most authoritative public specification to date has
been the documentation of a Go Language package
(https://pkg.go.dev/github.com/kr/logfmt) written by Blake Mizerany and
Keith Rarick.

%files
%license LICENSE*
%doc README*
%{go_sys_gopath}/%{go_import_path}

%changelog
%{?autochangelog}
