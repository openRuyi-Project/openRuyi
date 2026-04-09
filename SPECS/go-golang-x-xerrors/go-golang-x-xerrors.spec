# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           xerrors
%define go_import_path  golang.org/x/xerrors
# Upstream does not provide proper git tags, use commit ID instead - 251
%define commit_id 7835f813f4da395c9a1f7c0fe732a63d1c79d331

Name:           go-golang-x-xerrors
Version:        0+git20240903.7835f81
Release:        %autorelease
Summary:        new Go 1.13 error values
License:        BSD-3-Clause
URL:            https://golang.org/x/xerrors
VCS:            git:https://github.com/golang/xerrors
#!RemoteAsset
Source0:        https://github.com/golang/xerrors/archive/%{commit_id}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n %{_name}-%{commit_id}
BuildOption(check):  -vet=off -short

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(golang.org/x/xerrors) = %{version}

%description
This repository holds the transition packages for the new Go 1.13 error values.
See golang.org/design/29934-error-values.

%files
%license LICENSE*
%doc README*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
