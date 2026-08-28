# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           dd-sdk-go-testing
%define go_import_path  github.com/DataDog/dd-sdk-go-testing

Name:           go-github-datadog-dd-sdk-go-testing
Version:        0.0.3
Release:        %autorelease
Summary:        Datadog CI visibility SDK for Go tests
License:        Apache-2.0 OR BSD-3-Clause
URL:            https://github.com/DataDog/dd-sdk-go-testing
#!RemoteAsset:  sha256:9df217be8c839fcf4fa6af6b2d029f949c8347ebe29fde92704c56beac5f4b75
Source0:        https://github.com/DataDog/dd-sdk-go-testing/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
# For tests
BuildRequires:  git
BuildRequires:  go(github.com/Microsoft/go-winio)
BuildRequires:  go(github.com/google/uuid)
BuildRequires:  go(github.com/mitchellh/go-homedir)
BuildRequires:  go(github.com/onsi/ginkgo)
BuildRequires:  go(github.com/onsi/ginkgo/v2)
BuildRequires:  go(github.com/onsi/gomega)
BuildRequires:  go(github.com/philhofer/fwd)
BuildRequires:  go(golang.org/x/sys)
BuildRequires:  go(golang.org/x/time)
BuildRequires:  go(gopkg.in/DataDog/dd-trace-go.v1)

Provides:       go(%{go_import_path}) = %{version}

Requires:       go(github.com/Microsoft/go-winio)
Requires:       go(github.com/google/uuid)
Requires:       go(github.com/mitchellh/go-homedir)
Requires:       go(github.com/onsi/ginkgo)
Requires:       go(github.com/onsi/ginkgo/v2)
Requires:       go(github.com/onsi/gomega)
Requires:       go(github.com/philhofer/fwd)
Requires:       go(golang.org/x/sys)
Requires:       go(golang.org/x/time)
Requires:       go(gopkg.in/DataDog/dd-trace-go.v1)

%description
This SDK instruments Go tests for Datadog CI visibility and propagates test
trace context to instrumented application requests.

%check
# The SDK's tests validate metadata discovered from the current Git checkout.
git init
git config user.name "OBS Builder"
git config user.email "obs-builder@localhost"
git remote add origin https://github.com/DataDog/dd-sdk-go-testing.git
git add .
git commit -m "OBS test source"
%buildsystem_golangmodules_check

%files
%doc README.md
%license LICENSE*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
