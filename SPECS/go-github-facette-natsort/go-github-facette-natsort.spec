# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: HNO3Miracle <xiangao.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           natsort
%define go_import_path  github.com/facette/natsort
%define commit_id 2cd4dd1e2dcba4d85d6d3ead4adf4cfd2b70caf2

Name:           go-github-facette-natsort
Version:        0+git20260607.2cd4dd1
Release:        %autorelease
Summary:        Natural strings sorting in Go
License:        BSD-3-Clause
URL:            https://github.com/facette/natsort
#!RemoteAsset:  sha256:182e6dc9a313095acb504b30651b569a8b8410ef3e48120be6e1af39fe7ce7a5
Source0:        https://github.com/facette/natsort/archive/%{commit_id}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/facette/natsort) = %{version}

%description
This is an implementation of the "Alphanum Algorithm"
by Dave Koelle in Go.

%files
%doc README*
%license LICENSE*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
