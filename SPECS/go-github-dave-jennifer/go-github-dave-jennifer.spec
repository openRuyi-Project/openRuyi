# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           jennifer
%define go_import_path  github.com/dave/jennifer

Name:           go-github-dave-jennifer
Version:        1.7.1
Release:        %autorelease
Summary:        Generate Go source code with a fluent API
License:        MIT
URL:            https://github.com/dave/jennifer
#!RemoteAsset:  sha256:c7978547256ce03c3897df326e7d7ba9692cdcc6d417471e78f3a767f742fcce
Source0:        https://github.com/dave/jennifer/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

# Keep all examples enabled with current Go vet's example-name validation.
Patch2000:      2000-tests-use-valid-example-names.patch

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/dave/jennifer) = %{version}
Provides:       go(github.com/dave/jennifer/jen) = %{version}

%description
Jennifer builds and formats Go source files with automatic import
management and a fluent code-generation API.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
