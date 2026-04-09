# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Julian Zhu <julian.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           go-cleanhttp
%define go_import_path  github.com/hashicorp/go-cleanhttp

Name:           go-github-hashicorp-go-cleanhttp
Version:        0.5.2
Release:        %autorelease
Summary:        Functions for accessing "clean" Go http.Client values
License:        MPL-2.0
URL:            https://github.com/hashicorp/go-cleanhttp
#!RemoteAsset
Source0:        https://github.com/hashicorp/go-cleanhttp/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/hashicorp/go-cleanhttp) = %{version}

%description
This repository provides some simple functions to get a "clean"
http.Client -- one that uses the same default values as the Go standard
library, but returns a client that does not share any state with other
clients.

%files
%license LICENSE*
%doc README*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
