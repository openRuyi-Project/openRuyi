# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           wmi
%define go_import_path  github.com/yusufpapurcu/wmi
# Linux/riscv compile no Windows-tagged packages, so go test ./...
# reports "no packages to test" and exits non-zero.
%define go_test_ignore_failure 1

Name:           go-github-yusufpapurcu-wmi
Version:        1.2.4
Release:        %autorelease
Summary:        WQL interface for Windows WMI
License:        MIT
URL:            https://github.com/yusufpapurcu/wmi
#!RemoteAsset:  sha256:c7bb668db5dffd97ade4076acd361d21912525d22fd5608c8689191f4b7d5e26
Source0:        https://github.com/yusufpapurcu/wmi/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/go-ole/go-ole)

Provides:       go(github.com/yusufpapurcu/wmi) = %{version}

Requires:       go(github.com/go-ole/go-ole)

%description
Package wmi provides a WQL interface to Windows WMI. The implementation
is Windows-only; other GOOS values compile to empty source via build
tags. The go-ole dependency is retained for Windows consumers even though
the Linux build has no runnable WMI implementation.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
