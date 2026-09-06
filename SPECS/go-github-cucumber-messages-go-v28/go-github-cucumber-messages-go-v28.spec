# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           messages
%define go_import_path  github.com/cucumber/messages/go/v28

Name:           go-github-cucumber-messages-go-v28
Version:        28.1.0
Release:        %autorelease
Summary:        Cucumber message protocol types for Go
License:        MIT
URL:            https://github.com/cucumber/messages
#!RemoteAsset:  sha256:2c2e0b07fffb78e028fb61d1cf1d3678078483b89aa66ab0ae0261b54e3e8eed
Source0:        https://github.com/cucumber/messages/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/davecgh/go-spew)
BuildRequires:  go(github.com/google/uuid)
BuildRequires:  go(github.com/pmezard/go-difflib)
BuildRequires:  go(github.com/stretchr/testify)
BuildRequires:  go(gopkg.in/yaml.v3)

Provides:       go(%{go_import_path}) = %{version}

Requires:       go(github.com/google/uuid)

%description
This package provides the Go implementation of Cucumber's cross-language
message protocol from the upstream messages repository.

%install
pushd go
%buildsystem_golangmodules_install
popd

%check
pushd go
%buildsystem_golangmodules_check
popd

%files
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
