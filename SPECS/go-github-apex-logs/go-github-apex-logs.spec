# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           logs
%define go_import_path  github.com/apex/logs
# This integration test needs a live Apex Logs URL and AUTH_TOKEN; without them
# it fails with Post "/get_projects": unsupported protocol scheme "".
%global go_test_flags_default -v -skip '^TestService_GetProjects$'

Name:           go-github-apex-logs
Version:        1.1.0
Release:        %autorelease
Summary:        Go client for Apex Logs
License:        MIT
URL:            https://github.com/apex/logs
#!RemoteAsset:  sha256:509f5c0b89cdcb47d78e18e9e6573c72d1914d3f885b1aa7514f0a8863b528ec
Source0:        https://github.com/apex/logs/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n logs-%{version}

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/tj/assert)

Provides:       go(github.com/apex/logs) = %{version}

%description
This package provides the Go client for the Apex Logs service.

%check -p
# TestHTTP only checks rejection of plain HTTP and does not contact the endpoint.
export URL=https://example.invalid

%files
%doc Readme.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
