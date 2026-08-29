# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: panglars <panghao.riscv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           fastwalk
%define go_import_path  github.com/charlievieth/fastwalk

Name:           go-github-charlievieth-fastwalk
Version:        1.0.14
Release:        %autorelease
Summary:        Fast parallel directory traversal for Go
License:        MIT
URL:            https://github.com/charlievieth/fastwalk
#!RemoteAsset:  sha256:e5bba50b0239b74113a218cb11db00fc3dbaf81fdb155cb7e1573cdbd82d9f86
Source0:        https://github.com/charlievieth/fastwalk/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n %{_name}-%{version}

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/charlievieth/fastwalk) = %{version}

%description
Package fastwalk provides a fast parallel version of filepath.WalkDir with
support for concurrent traversal and optional symbolic link handling.

%files
%doc README*
%license LICENSE*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
