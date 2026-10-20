# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           libraries
%define go_import_path  github.com/standard-webhooks/standard-webhooks/libraries

Name:           go-github-standard-webhooks-standard-webhooks-libraries
Version:        0.0.1
Release:        %autorelease
Summary:        Libraries for signing/verifying webhook messages
License:        MIT
URL:            https://github.com/standard-webhooks/standard-webhooks
#!RemoteAsset:  sha256:bf8945e2dc4605c8202de48ca78819572428a2eb1477edd8c889b2457bbc237b
Source0:        https://github.com/standard-webhooks/standard-webhooks/archive/refs/tags/libraries/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n standard-webhooks-libraries-v%{version}

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/standard-webhooks/standard-webhooks/libraries) = %{version}

%description
Standard Webhooks Libraries
Libraries for signing/verifying webhook messages

%install
pushd libraries
%buildsystem_golangmodules_install
popd

%check
pushd libraries
%buildsystem_golangmodules_check
popd

%files
%doc libraries/README.md
%license libraries/LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
