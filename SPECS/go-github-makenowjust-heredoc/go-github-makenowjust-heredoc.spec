# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           heredoc
%define go_import_path  github.com/MakeNowJust/heredoc

Name:           go-github-makenowjust-heredoc
Version:        1.0.0
Release:        %autorelease
Summary:        Here-document support with indentation handling for Go
License:        MIT
URL:            https://github.com/MakeNowJust/heredoc
#!RemoteAsset:  sha256:3703d1c9e659c274c5e2d712e4d66f60620e03513fc380b1d3acafb3ca037400
Source0:        https://github.com/MakeNowJust/heredoc/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(check):  -vet=off

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/MakeNowJust/heredoc) = %{version}

%description
heredoc provides Go helpers for defining indented here-document strings while
removing common leading whitespace.

%files
%doc README*
%license LICENSE*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
