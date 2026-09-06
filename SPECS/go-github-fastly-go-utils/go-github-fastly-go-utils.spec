# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           go-utils
%define go_import_path  github.com/fastly/go-utils
# The executable test assumes GOPATH-era test binary paths, while lifecycle
# intentionally calls os.Exit from the test process.
%define go_test_exclude %{shrink:
    %{go_import_path}/executable
    %{go_import_path}/lifecycle
    %{go_import_path}/tls
}
%define commit_id       d95a45783239f69a867fec572fb7675bcee07d88

Name:           go-github-fastly-go-utils
Version:        0+git20260819.d95a457
Release:        %autorelease
Summary:        Collection of utility libraries for Go
License:        MIT
URL:            https://github.com/fastly/go-utils
#!RemoteAsset:  sha256:2e0a5d0ad6582857d50cb4973ac27b184e302d1280a7ef328eb3c6726639b5cb
Source0:        https://github.com/fastly/go-utils/archive/%{commit_id}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules
BuildOption(prep):  -n %{_name}-%{commit_id}
BuildOption(check):  -vet=off

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/jbuchbinder/go-gmetric)
BuildRequires:  tzdata

Provides:       go(%{go_import_path}) = %{version}

Requires:       go(github.com/jbuchbinder/go-gmetric)

%description
Go-utils is a collection of utility packages for time formatting, process
management, instrumentation, logging, networking, and related tasks.

%check -a
for package in %{go_test_exclude}; do
    go test -vet=off -c -o /dev/null "${package}"
done

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
