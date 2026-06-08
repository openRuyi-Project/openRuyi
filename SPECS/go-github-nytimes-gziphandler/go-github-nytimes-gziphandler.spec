# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: HNO3Miracle <xiangao.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           gziphandler
%define go_import_path  github.com/NYTimes/gziphandler

Name:           go-github-nytimes-gziphandler
Version:        1.1.1
Release:        %autorelease
Summary:        HTTP gzip response middleware for Go
License:        Apache-2.0
URL:            https://github.com/NYTimes/gziphandler
#!RemoteAsset:  sha256:c236c216a16e4286338e66e0947938944992f918fe827c31f8745c0be98818d2
Source0:        https://github.com/NYTimes/gziphandler/archive/refs/tags/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/stretchr/testify)

Provides:       go(github.com/NYTimes/gziphandler) = %{version}

%description
gziphandler is HTTP middleware for compressing Go HTTP responses with gzip
when clients advertise support for it. It is used by Kubernetes OpenAPI
serving code to reduce the size of generated API schema responses.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
