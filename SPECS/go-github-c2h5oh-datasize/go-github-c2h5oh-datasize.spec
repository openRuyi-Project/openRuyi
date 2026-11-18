# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           datasize
%define go_import_path  github.com/c2h5oh/datasize
%define commit_id       aa82cc1e65004e2b59a6e44d26f774ca961b24d8

Name:           go-github-c2h5oh-datasize
Version:        0+git20261118.aa82cc1
Release:        %autorelease
Summary:        Golang helpers for data sizes
License:        MIT
URL:            https://github.com/c2h5oh/datasize
#!RemoteAsset:  sha256:1320a5b3d1c04363e4f096c05a1fd697bf59625c1571ce461b8c6d961f482393
Source0:        https://github.com/c2h5oh/datasize/archive/%{commit_id}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n %{_name}-%{commit_id}

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/c2h5oh/datasize) = %{version}

%description
Golang helpers for parsing, formatting, and marshaling data sizes.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
