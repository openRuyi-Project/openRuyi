# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           properties
%define go_import_path  github.com/magiconair/properties

Name:           go-github-magiconair-properties
Version:        1.8.10
Release:        %autorelease
Summary:        Java properties scanner for Go
License:        BSD-2-Clause
URL:            https://github.com/magiconair/properties
#!RemoteAsset:  sha256:0992d837b22e0381f315c55ac2a106d5557955e28b9ce10c9630a0a275ffb63a
Source0:        %{url}/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n %{_name}-%{version}
# Go vet rejects upstream non-constant format strings with newer Go. - Jvle
BuildOption(check):  -vet=off

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/magiconair/properties) = %{version}

%description
properties is a Go library for reading and writing properties files.

It supports reading from multiple files or URLs and Spring style recursive
property expansion of expressions like ${key} to their corresponding value.
Value expressions can refer to other keys like in ${key} or to environment
variables like in ${USER}. Filenames can also contain environment variables
like in /home/${USER}/myapp.properties.

%files
%license LICENSE*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
