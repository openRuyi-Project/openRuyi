# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           wmi
%define go_import_path  github.com/StackExchange/wmi
# WMI requires Windows; tolerate failures from the default checks on Linux.
%define go_test_ignore_failure  1

Name:           go-github-stackexchange-wmi
Version:        1.2.1
Release:        %autorelease
Summary:        WMI query library for Go
License:        MIT
URL:            https://github.com/StackExchange/wmi
#!RemoteAsset:  sha256:a90126aa4c4defa7455be9610e84b0606972eccfa4111c2ec97179691d240b5a
Source0:        https://github.com/StackExchange/wmi/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/go-ole/go-ole)

Provides:       go(%{go_import_path}) = %{version}

Requires:       go(github.com/go-ole/go-ole)

%description
This package provides a WQL interface for querying Windows Management
Instrumentation from Go.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
