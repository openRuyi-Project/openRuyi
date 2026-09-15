# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: HNO3Miracle <xiangao.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           sessions
%define go_import_path  github.com/gorilla/sessions

Name:           go-github-gorilla-sessions
Version:        1.4.0
Release:        %autorelease
Summary:        Session management for Go web applications
License:        BSD-3-Clause
URL:            https://github.com/gorilla/sessions
#!RemoteAsset:  sha256:77b8e99717c5af30f3a6be5d2418397c8f5ef298c0fc40c5ce5158781ea67001
Source0:        https://github.com/gorilla/sessions/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

# Fix integer format verbs in the cookie option test.
# https://github.com/gorilla/sessions/pull/293
Patch2000:      2000-use-integer-formats-for-cookie-maxage.patch

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/gorilla/securecookie)

Provides:       go(github.com/gorilla/sessions) = %{version}

Requires:       go(github.com/gorilla/securecookie)

%description
Sessions provides cookie and filesystem-backed session management for Go HTTP
applications.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
