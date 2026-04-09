# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Julian Zhu <julian.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           go-simplejson
%define go_import_path  github.com/bitly/go-simplejson

Name:           go-github-bitly-go-simplejson
Version:        0.5.1
Release:        %autorelease
Summary:        a Go package to interact with arbitrary JSON
License:        MIT
URL:            https://github.com/bitly/go-simplejson
#!RemoteAsset
Source0:        https://github.com/bitly/go-simplejson/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/bitly/go-simplejson) = %{version}

%description
a Go package to interact with arbitrary JSON

%files
%license LICENSE*
%doc README*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
