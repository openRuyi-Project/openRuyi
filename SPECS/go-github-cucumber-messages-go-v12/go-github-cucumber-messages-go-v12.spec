# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           messages-go
%define go_import_path  github.com/cucumber/messages-go/v12

Name:           go-github-cucumber-messages-go-v12
Version:        12.0.0
Release:        %autorelease
Summary:        Cucumber message protocol types for Go
License:        MIT
URL:            https://github.com/cucumber/messages-go
#!RemoteAsset:  sha256:5b302721ce965f5df13d3ce5820ce88e7bee452300af273c12c80aaae02e342a
Source0:        https://github.com/cucumber/messages-go/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/gofrs/uuid)
BuildRequires:  go(github.com/gogo/protobuf)
BuildRequires:  go(github.com/stretchr/testify)

Provides:       go(%{go_import_path}) = %{version}

Requires:       go(github.com/gofrs/uuid)
Requires:       go(github.com/gogo/protobuf)

%description
Messages-go provides Go types for the Cucumber message protocol used to
exchange Gherkin documents, pickles, attachments, and test results.

%files
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
