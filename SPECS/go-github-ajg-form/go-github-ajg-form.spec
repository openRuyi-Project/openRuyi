# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Julian Zhu <julian.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           form
%define go_import_path  github.com/ajg/form

Name:           go-github-ajg-form
Version:        1.7.1
Release:        %autorelease
Summary:        A Form Encoding & Decoding Package for Go
License:        BSD-3-Clause
URL:            https://github.com/ajg/form
#!RemoteAsset:  sha256:a336ae5e7407ba63b099cd1fca4423fd7174e082c7ced9751b6faa06f9f16f69
Source0:        https://github.com/ajg/form/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/ajg/form) = %{version}

%description
This library is designed to allow seamless, high-fidelity encoding and
decoding of arbitrary data in application/x-www-form-urlencoded format
and
as url.Values (http://golang.org/pkg/net/url/#Values). It is intended to
be useful primarily in dealing with web forms and URI query strings,
both of which natively employ said format.

%files
%license LICENSE*
%doc README*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
