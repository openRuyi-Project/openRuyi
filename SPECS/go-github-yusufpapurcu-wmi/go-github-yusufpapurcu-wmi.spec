# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           wmi
%define go_import_path  github.com/yusufpapurcu/wmi

Name:           go-github-yusufpapurcu-wmi
Version:        1.2.2
Release:        %autorelease
Summary:        WQL interface for Windows WMI
License:        MIT
URL:            https://github.com/yusufpapurcu/wmi
#!RemoteAsset:  sha256:334baf5692c9b74e4a8b22b75901896f3832b2a38ba9c343c5bdcd2e721f63df
Source0:        https://github.com/yusufpapurcu/wmi/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/go-ole/go-ole)

Provides:       go(github.com/yusufpapurcu/wmi) = %{version}

Requires:       go(github.com/go-ole/go-ole)

%description
This package provides a WQL interface to Windows Management Instrumentation on
the local machine.

%check
export GO111MODULE=off
export GOPATH=%{_builddir}/go:%{_datadir}/gocode
install -d "%{_builddir}/go/src/%{go_import_path}"
cp -a ./. "%{_builddir}/go/src/%{go_import_path}/"
GOOS=windows go test -c -o "%{_builddir}/wmi.test.exe" %{go_import_path}

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
