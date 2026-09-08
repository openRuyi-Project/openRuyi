# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           gherkin-go
%define go_import_path  github.com/cucumber/gherkin-go/v13

Name:           go-github-cucumber-gherkin-go-v13
Version:        13.0.0
Release:        %autorelease
Summary:        Gherkin parser and compiler for Go
License:        MIT
URL:            https://github.com/cucumber/gherkin-go
#!RemoteAsset:  sha256:691b1170ac830f16e638ad2505c11b4d457a4163eb8d7689c2fa9d1ade4beed2
Source0:        https://github.com/cucumber/gherkin-go/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

# Associate the example with the Pickles function for current Go vet.
Patch1:         2000-tests-associate-pickle-example-with-exported-function.patch

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/cucumber/messages-go/v12)
BuildRequires:  go(github.com/gogo/protobuf)
BuildRequires:  go(github.com/stretchr/testify)

Provides:       go(%{go_import_path}) = %{version}

Requires:       go(github.com/cucumber/messages-go/v12)
Requires:       go(github.com/gogo/protobuf)

%description
Gherkin-go parses and compiles Gherkin feature documents into Cucumber
messages for Go applications.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
