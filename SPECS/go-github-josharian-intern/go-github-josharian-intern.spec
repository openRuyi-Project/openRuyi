# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Julian Zhu <julian.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: HNO3Miracle <xiangao.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           intern
%define go_import_path  github.com/josharian/intern

Name:           go-github-josharian-intern
Version:        1.0.0
Release:        %autorelease
Summary:        Intern Go strings
License:        MIT
URL:            https://github.com/josharian/intern
#!RemoteAsset:  sha256:7c7df6e792ed5db0b1a63c8ec74236b70958ad36c9fe5a02b52b1a418b177b5e
Source0:        https://github.com/josharian/intern/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/josharian/intern) = %{version}

%description
Package intern interns strings. Interning is best
effort only. Interned strings may be removed
automatically at any time without notification.
All functions may be called concurrently with
themselves and each other.

%files
%doc README*
%license license*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
