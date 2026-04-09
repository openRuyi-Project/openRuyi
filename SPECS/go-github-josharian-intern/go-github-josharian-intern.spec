# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Julian Zhu <julian.oerv@isrc.iscas.ac.cn>
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
#!RemoteAsset
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
%license license*
%doc README*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
