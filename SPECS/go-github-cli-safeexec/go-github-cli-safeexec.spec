# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           safeexec
%define go_import_path  github.com/cli/safeexec

Name:           go-github-cli-safeexec
Version:        1.0.1
Release:        %autorelease
Summary:        A safer version of exec.LookPath on Windows
License:        BSD-2-Clause
URL:            https://github.com/cli/safeexec
#!RemoteAsset:  sha256:9fea01cbc9703c618961dc93dcffd21473af4a7ab0345efcbac479e711b6a776
Source0:        https://github.com/cli/safeexec/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/cli/safeexec) = %{version}

%description
safeexec provides a safe alternative to Go's os/exec.LookPath, avoiding
the insecure behavior of resolving executables from the current directory
on Windows.

%files
%doc README*
%license LICENSE*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
