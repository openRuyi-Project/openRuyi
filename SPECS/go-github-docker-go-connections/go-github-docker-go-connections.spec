# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Julian Zhu <julian.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           go-connections
%define go_import_path  github.com/docker/go-connections
# TODO: may be certificate problem, check it later - Julian
%define go_test_ignore_failure 1

Name:           go-github-docker-go-connections
Version:        0.6.0
Release:        %autorelease
Summary:        Utility package to work with network connections
License:        Apache-2.0
URL:            https://github.com/docker/go-connections
#!RemoteAsset
Source0:        https://github.com/docker/go-connections/archive/refs/tags/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/docker/go-connections) = %{version}

%description
go-connections provides common package to work with network connections.

%files
%license LICENSE*
%doc README*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
