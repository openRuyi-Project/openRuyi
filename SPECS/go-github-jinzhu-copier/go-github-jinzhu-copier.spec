# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           copier
%define go_import_path  github.com/jinzhu/copier

Name:           go-github-jinzhu-copier
Version:        0.4.0
Release:        %autorelease
Summary:        Copier for golang, copy value from struct to struct and more
License:        MIT
URL:            https://github.com/jinzhu/copier
#!RemoteAsset:  sha256:918ef876733550ec73ee7e8040fa3251f033e5a7a6a7d9419862a438b974814c
Source0:        %{url}/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n %{_name}-%{version}
# Upstream v0.4.0 has a Fatalf %q format mismatch in copier_converter_test.go;
# disable go vet while still running tests.
BuildOption(check):  -vet=off

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/jinzhu/copier) = %{version}

%description
I am a copier, I copy everything from one to another

%files
%doc README*
%license License*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
