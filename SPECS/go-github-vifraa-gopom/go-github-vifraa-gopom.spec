# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           gopom
%define go_import_path  github.com/vifraa/gopom

Name:           go-github-vifraa-gopom
Version:        1.0.0
Release:        %autorelease
Summary:        A maven pom.xml parser written in Go
License:        MIT
URL:            https://github.com/vifraa/gopom
#!RemoteAsset:  sha256:b27a79569c2135e16510209eeb9323b0572acc4bd7629c667ebb172a26a3273e
Source0:        %{url}/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n %{_name}-%{version}

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/stretchr/testify)

Provides:       go(github.com/vifraa/gopom) = %{version}

Requires:       go(github.com/stretchr/testify)

%description
gopom is a Golang module to easily parse and work with maven pom.xml files.

%files
%doc README*
%license LICENSE*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
