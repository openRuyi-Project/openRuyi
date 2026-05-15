# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Julian Zhu <julian.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           time
%define go_import_path  golang.org/x/time

Name:           go-golang-x-time
Version:        0.15.0
Release:        %autorelease
Summary:        Go supplementary time packages
License:        BSD-3-Clause
URL:            https://golang.org/x/time
VCS:            git:https://github.com/golang/time
#!RemoteAsset:  sha256:32a60b8633619084bc18ac9bce6c722608472cccfe760a671898a84ea7573782
Source0:        https://github.com/golang/time/archive/refs/tags/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(golang.org/x/time) = %{version}

%description
Supplementary Go time packages.

%files
%license LICENSE*
%doc README*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
