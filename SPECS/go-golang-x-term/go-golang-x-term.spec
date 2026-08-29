# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
# SPDX-FileContributor: Julian Zhu <julian.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           term
%define go_import_path  golang.org/x/term

Name:           go-golang-x-term
Version:        0.44.0
Release:        %autorelease
Summary:        Go terminal and console support
License:        BSD-3-Clause
URL:            https://golang.org/x/term
VCS:            git:https://github.com/golang/term
#!RemoteAsset:  sha256:b5238a70779c6aad2b9309565a2d5744823e7efba857e8c6086b37b5d918983a
Source0:        https://github.com/golang/term/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n %{_name}-%{version}

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(golang.org/x/sys)

Provides:       go(golang.org/x/term) = %{version}

Requires:       go(golang.org/x/sys)

%description
This repository provides Go terminal and console support packages.

%files
%license LICENSE*
%doc README*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
