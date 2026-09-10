# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           datadog-go
%define go_import_path  github.com/DataDog/datadog-go/v5

Name:           go-github-datadog-datadog-go-v5
Version:        5.9.0
Release:        %autorelease
Summary:        DogStatsD client library for Go
License:        MIT
URL:            https://github.com/DataDog/datadog-go
#!RemoteAsset:  sha256:bad211e683f873438a39f755c9e1623cbeeab29cbe9481d7af8dcfccb3f32d4a
Source0:        https://github.com/DataDog/datadog-go/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

# Make container-origin tests independent of the build host and test order.
Patch2000:      2000-statsd-make-container-origin-tests-hermetic.patch

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/golang/mock)
BuildRequires:  go(github.com/stretchr/testify)
BuildRequires:  go(golang.org/x/net)

Provides:       go(%{go_import_path}) = %{version}

Requires:       go(github.com/golang/mock)
Requires:       go(golang.org/x/net)

%description
This package provides a Go client for submitting metrics, events, and service
checks to Datadog through DogStatsD.

%files
%doc CHANGELOG.md
%doc README.md
%license LICENSE.txt
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
