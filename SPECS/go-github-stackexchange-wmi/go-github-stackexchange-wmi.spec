# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           wmi
%define go_import_path  github.com/StackExchange/wmi

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

%prep -a
%go_prep

%check
# WMI has no Linux buildable files; cross-compile its tests for Windows.
%go_common
cd %{_builddir}/go/src/%{go_import_path}
GOOS=windows %__go test -c -o %{_builddir}/wmi.test.exe %{go_import_path}
rm -f %{_builddir}/wmi.test.exe

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
