# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           wmi
%define go_import_path  github.com/StackExchange/wmi
# This is a package for windows
# However, it's depended by certtostore
%define go_test_ignore_failure 1

Name:           go-github-stackexchange-wmi
Version:        1.1.0
Release:        %autorelease
Summary:        WMI client library for Go
License:        MIT
URL:            https://github.com/StackExchange/wmi
#!RemoteAsset:  sha256:e5e7537a37b205eedc30b0bd21991dbe7146b9a7ae902fd20080e0d33006a2f8
Source0:        https://github.com/StackExchange/wmi/archive/refs/tags/%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/go-ole/go-ole)

Provides:       go(github.com/StackExchange/wmi) = %{version}

Requires:       go(github.com/go-ole/go-ole)

%description
Package wmi provides a Windows Management Instrumentation client for Go.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
