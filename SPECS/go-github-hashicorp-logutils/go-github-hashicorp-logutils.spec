# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: tangyihong <yihong.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           logutils
%define go_import_path  github.com/hashicorp/logutils

Name:           go-github-hashicorp-logutils
Version:        1.0.0
Release:        %autorelease
Summary:        Utilities for slightly better logging in Go
License:        MPL-2.0
URL:            https://github.com/hashicorp/logutils
#!RemoteAsset:  sha256:9e3c7cee3552acacd2ad1d212f87c682d227179e34b306afdce945b41799e4b6
Source0:        https://github.com/hashicorp/logutils/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/hashicorp/logutils) = %{version}

%description
logutils augments the Go standard library "log" package with level-based
filtering, without fragmenting the ecosystem with a new logging package. It is
used by the hashicorp/serf agent CLI.

%files
%doc README*
%license LICENSE*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
