# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Julian Zhu <julian.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           go-units
%define go_import_path  github.com/docker/go-units

Name:           go-github-docker-go-units
Version:        0.5.0
Release:        %autorelease
Summary:        Parse and print size and time units in human-readable format
License:        Apache-2.0
URL:            https://github.com/docker/go-units
#!RemoteAsset
Source0:        https://github.com/docker/go-units/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/docker/go-units) = %{version}

%description
go-units is a library to transform human friendly measurements into
machine friendly values.

%files
%license LICENSE*
%doc README*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
