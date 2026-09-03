# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           str
%define go_import_path  github.com/mgutz/str

Name:           go-github-mgutz-str
Version:        1.2.0
Release:        %autorelease
Summary:        Package str is a string library to build more Go awesomeness
License:        MIT
URL:            https://github.com/mgutz/str
#!RemoteAsset:  sha256:8d03c5aa2ea6de04d07a59bc7a722fdc3215d9ba117df424b227c530bf36b221
Source0:        https://github.com/mgutz/str/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/mgutz/str) = %{version}

%description
str is a comprehensive set of string manipulation functions for Go,
modeled after the underscore.string JavaScript library.

# Gododir/ is upstream's task-runner tooling (imports mgutz/goa, godo.v2)
# which is unrelated to the library; drop it so %%check does not pull it in.
%prep -a
rm -rf Gododir

%files
%doc README*
%license LICENSE*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
