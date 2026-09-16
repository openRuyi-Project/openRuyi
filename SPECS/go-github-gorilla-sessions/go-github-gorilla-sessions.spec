# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           sessions
%define go_import_path  github.com/gorilla/sessions

Name:           go-github-gorilla-sessions
Version:        1.2.1
Release:        %autorelease
Summary:        Cookie and filesystem sessions for Gorilla
License:        BSD-3-Clause
URL:            https://github.com/gorilla/sessions
#!RemoteAsset:  sha256:2234387daf91ba4318516ba3b9f73ba0d166dc5f0a45f146b918f3a4c11a3184
Source0:        https://github.com/gorilla/sessions/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

# cookie_test.go Fatals MaxAge with a quoted format for an int; Go 1.27 vet rejects it.
BuildOption(check):  -vet=off

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/gorilla/securecookie)

Provides:       go(github.com/gorilla/sessions) = %{version}

Requires:       go(github.com/gorilla/securecookie)

%description
gorilla/sessions provides cookie and filesystem session stores, plus
infrastructure for custom session backends. jcmturner/gokrb5 uses it.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
