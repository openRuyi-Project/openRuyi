# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           go-set
%define go_import_path  github.com/scylladb/go-set
%define commit_id       cc7b2070d91ebf40d233207b633e28f5bd8f03a5

Name:           go-github-scylladb-go-set
Version:        1.0.3~0.git20260719.cc7b2070d91e
Release:        %autorelease
Summary:        Go library packaged for syft dependency resolution
License:        Apache-2.0
URL:            https://github.com/scylladb/go-set
#!RemoteAsset:  sha256:8f9abdfe2a0da6fe2ea500ccf99ae879bad5f8b45a29fac8c7e6e50301864d77
Source0:        %{url}/archive/%{commit_id}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n %{_name}-%{commit_id}

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/fatih/set)

Provides:       go(github.com/scylladb/go-set) = %{version}

Requires:       go(github.com/fatih/set)

%description
Go library packaged for syft dependency resolution.

%files
%doc README*
%license LICENSE*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
