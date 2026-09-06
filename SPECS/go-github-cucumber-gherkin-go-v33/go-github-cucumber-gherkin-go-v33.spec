# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           gherkin
%define go_import_path  github.com/cucumber/gherkin/go/v33

Name:           go-github-cucumber-gherkin-go-v33
Version:        33.1.0
Release:        %autorelease
Summary:        Gherkin parser and compiler for Go
License:        MIT
URL:            https://github.com/cucumber/gherkin
#!RemoteAsset:  sha256:7a4c450b5a933841685983767606ae910a07a1d63d95332fba9850db090ba41b
Source0:        https://github.com/cucumber/gherkin/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

# Use Fprint because the marshaled JSON is data, not a format string.
Patch2000:      2000-go-avoid-a-dynamic-format-string-in-pickle-example.patch

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/cucumber/messages/go/v28)
BuildRequires:  go(github.com/davecgh/go-spew)
BuildRequires:  go(github.com/google/uuid)
BuildRequires:  go(github.com/pmezard/go-difflib)
BuildRequires:  go(github.com/stretchr/testify)
BuildRequires:  go(gopkg.in/yaml.v3)

Provides:       go(%{go_import_path}) = %{version}

Requires:       go(github.com/cucumber/messages/go/v28)

%description
This package provides the Go Gherkin parser and compiler from the upstream
multi-language Gherkin repository.

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
